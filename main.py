import sys
import io
import os
from dotenv import load_dotenv
from datetime import datetime

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

load_dotenv()

from config import FRAZY_DDGO
from scrapers.duckduckgo import szukaj_ddgo
from scrapers.facebook import szukaj_facebook
from bot.telegram_bot import wyslij_leady
from dashboard import generuj_dashboard
from historia import zaladuj_widziane, zapisz_widziane


def drukuj_leady(leady: list[dict], naglowek: str):
    print(f"\n{'='*60}")
    print(f"  {naglowek} ({len(leady)} wynikow)")
    print(f"{'='*60}")
    if not leady:
        print("  Brak pasujacych leadow.")
        return
    for i, l in enumerate(leady, 1):
        data = l.get("data", "brak daty")
        print(f"\n  [{i}] {l['zrodlo']} | {data} -- {l['tytul']}")
        print(f"       {l['opis'][:120]}")
        print(f"       >> {l['link']}")


def main():
    ci_mode = "--ci" in sys.argv or os.getenv("CI") == "true"

    print(f"\n=== KuchniaHACCP Lead Monitor === {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    print("Szukam potencjalnych klientow...\n")

    widziane = zaladuj_widziane()
    print(f"[Historia] Zaladowano {len(widziane)} znanych linkow.\n")

    print("[1/2] Przeszukuje Facebook (przez DDG)...")
    leady_fb = szukaj_facebook()
    drukuj_leady(leady_fb, "Facebook / DDG")

    print("[2/2] Przeszukuje web (DuckDuckGo)...")
    leady_ddgo = szukaj_ddgo(FRAZY_DDGO)
    drukuj_leady(leady_ddgo, "Web / DuckDuckGo")

    wszystkie = leady_fb + leady_ddgo

    # Filtruj leady już wcześniej wysłane
    nowe = [l for l in wszystkie if l["link"] not in widziane]
    duplikaty = len(wszystkie) - len(nowe)

    print(f"\n{'='*60}")
    print(f"  Znaleziono: {len(wszystkie)} | Nowe: {len(nowe)} | Pominiete (juz widziane): {duplikaty}")
    print(f"{'='*60}")

    if nowe:
        print("\nWysylam do Telegrama...")
        wyslij_leady(nowe)
        widziane.update(l["link"] for l in nowe)
        zapisz_widziane(widziane)
        print(f"  [Historia] Zapisano {len(widziane)} linkow.")
    else:
        print("\nBrak nowych leadow do wyslania.")

    print("\nGeneruje dashboard...")
    generuj_dashboard(nowe)

    print("\n[OK] Gotowe!\n")


if __name__ == "__main__":
    main()
