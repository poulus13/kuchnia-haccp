import sys
import io
import os
from dotenv import load_dotenv
from datetime import datetime

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

load_dotenv()

from config import FRAZY_DDGO
from scrapers.duckduckgo import szukaj_ddgo
from bot.telegram_bot import wyslij_leady
from dashboard import generuj_dashboard


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

    print("[1/1] Przeszukuje web (DuckDuckGo)...")
    leady_ddgo = szukaj_ddgo(FRAZY_DDGO)
    drukuj_leady(leady_ddgo, "Web / DuckDuckGo")

    wszystkie = leady_ddgo
    print(f"\n{'='*60}")
    print(f"  RAZEM znaleziono: {len(wszystkie)} potencjalnych leadow")
    print(f"{'='*60}")

    if wszystkie:
        print("\nWysylam do Telegrama...")
        wyslij_leady(wszystkie)

    print("\nGeneruje dashboard...")
    generuj_dashboard(wszystkie)

    print("\n[OK] Gotowe!\n")


if __name__ == "__main__":
    main()
