import json
import os
import webbrowser
from pathlib import Path
from datetime import datetime

CI = os.getenv("CI") == "true"


def generuj_dashboard(leady: list[dict]):
    data_run = datetime.now().strftime("%Y-%m-%d %H:%M")
    liczba = len(leady)

    karty = ""
    for l in leady:
        zrodlo = l.get("zrodlo", "")
        data = l.get("data", "?")
        tytul = l.get("tytul", "")
        opis = l.get("opis", "")
        link = l.get("link", "#")

        data_badge = f'<span class="badge">{data}</span>' if data != "?" else '<span class="badge unknown">brak daty</span>'
        karty += f"""
        <div class="card">
          <div class="card-header">
            <span class="source">{zrodlo}</span>
            {data_badge}
          </div>
          <h3><a href="{link}" target="_blank">{tytul}</a></h3>
          <p>{opis}</p>
          <a href="{link}" target="_blank" class="btn">Otwórz &rarr;</a>
        </div>
        """

    if not leady:
        karty = '<div class="empty">Brak leadów w tym uruchomieniu.</div>'

    html = f"""<!DOCTYPE html>
<html lang="pl">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>KuchniaHACCP — Leady</title>
<style>
  * {{ box-sizing: border-box; margin: 0; padding: 0; }}
  body {{ font-family: 'Segoe UI', sans-serif; background: #f4f6f9; color: #222; }}
  header {{ background: #1a3a5c; color: white; padding: 24px 32px; display: flex; justify-content: space-between; align-items: center; }}
  header h1 {{ font-size: 1.4rem; font-weight: 600; }}
  header .meta {{ font-size: 0.85rem; opacity: 0.75; }}
  .stats {{ background: #fff; border-bottom: 1px solid #e0e4ea; padding: 16px 32px; display: flex; gap: 32px; }}
  .stat {{ display: flex; flex-direction: column; }}
  .stat span:first-child {{ font-size: 1.8rem; font-weight: 700; color: #1a3a5c; }}
  .stat span:last-child {{ font-size: 0.8rem; color: #888; text-transform: uppercase; letter-spacing: .05em; }}
  .grid {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(380px, 1fr)); gap: 20px; padding: 28px 32px; max-width: 1400px; margin: 0 auto; }}
  .card {{ background: white; border-radius: 10px; padding: 20px; box-shadow: 0 2px 8px rgba(0,0,0,.07); border-left: 4px solid #1a3a5c; }}
  .card-header {{ display: flex; align-items: center; gap: 10px; margin-bottom: 10px; }}
  .source {{ font-size: 0.75rem; font-weight: 600; background: #e8f0fe; color: #1a3a5c; padding: 2px 8px; border-radius: 4px; text-transform: uppercase; }}
  .badge {{ font-size: 0.75rem; color: #555; background: #f0f0f0; padding: 2px 8px; border-radius: 4px; }}
  .badge.unknown {{ color: #aaa; }}
  .card h3 {{ font-size: 1rem; margin-bottom: 8px; line-height: 1.4; }}
  .card h3 a {{ color: #1a3a5c; text-decoration: none; }}
  .card h3 a:hover {{ text-decoration: underline; }}
  .card p {{ font-size: 0.88rem; color: #555; line-height: 1.6; margin-bottom: 14px; }}
  .btn {{ display: inline-block; font-size: 0.82rem; color: #1a3a5c; border: 1px solid #1a3a5c; padding: 5px 14px; border-radius: 5px; text-decoration: none; }}
  .btn:hover {{ background: #1a3a5c; color: white; }}
  .empty {{ text-align: center; color: #aaa; padding: 80px; font-size: 1.1rem; }}
  footer {{ text-align: center; padding: 24px; color: #bbb; font-size: 0.8rem; }}
</style>
</head>
<body>
<header>
  <h1>KuchniaHACCP — Monitor Leadów</h1>
  <div class="meta">Ostatni run: {data_run}</div>
</header>
<div class="stats">
  <div class="stat"><span>{liczba}</span><span>Leadów</span></div>
  <div class="stat"><span>{sum(1 for l in leady if l.get('data','?') != '?')}</span><span>Z datą</span></div>
  <div class="stat"><span>{data_run[:10]}</span><span>Data runu</span></div>
</div>
<div class="grid">
  {karty}
</div>
<footer>KuchniaHACCP &bull; {data_run}</footer>
</body>
</html>"""

    # docs/index.html — GitHub Pages + lokalnie
    docs = Path("docs")
    docs.mkdir(exist_ok=True)
    pages_path = docs / "index.html"
    pages_path.write_text(html, encoding="utf-8")

    # JSON z leadami (do archiwum i ewentualnego przetwarzania)
    json_path = Path("leads.json")
    json_path.write_text(json.dumps(leady, ensure_ascii=False, indent=2), encoding="utf-8")

    if CI:
        print(f"  [Dashboard] Zapisano: {pages_path}")
    else:
        webbrowser.open(pages_path.resolve().as_uri())
        print(f"  [Dashboard] Otwarty w przegladarce: {pages_path.resolve()}")
