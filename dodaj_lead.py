import sys
import io
import os
from dotenv import load_dotenv

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
sys.stdin  = io.TextIOWrapper(sys.stdin.buffer,  encoding="utf-8", errors="replace")

load_dotenv()

from historia import zaladuj_widziane, zapisz_widziane
from bot.telegram_bot import wyslij_leady
from dashboard import generuj_dashboard
import json
from pathlib import Path


def wczytaj_leady_json() -> list[dict]:
    p = Path("leads.json")
    if p.exists():
        try:
            return json.loads(p.read_text(encoding="utf-8"))
        except Exception:
            return []
    return []


def main():
    print("\n=== Dodaj lead ręcznie (Facebook / inne) ===\n")

    link = input("Link (URL posta): ").strip()
    if not link:
        print("Brak linku — anulowano.")
        return

    widziane = zaladuj_widziane()
    if link in widziane:
        print("Ten link był już wysłany — pominięto.")
        return

    tytul = input("Tytuł / krótki opis (Enter = brak): ").strip() or "Lead z Facebook"
    opis  = input("Treść / notatka (Enter = brak): ").strip() or ""

    lead = {
        "zrodlo": "Facebook (ręcznie)",
        "tytul": tytul,
        "link": link,
        "opis": opis[:200],
        "data": __import__("datetime").datetime.now().strftime("%Y-%m-%d"),
    }

    print(f"\nDodaję: {lead['tytul']}")

    # Wyślij na Telegram
    wyslij_leady([lead])

    # Zapisz do historii
    widziane.add(link)
    zapisz_widziane(widziane)

    # Dorzuć do leads.json i odśwież dashboard
    wszystkie = wczytaj_leady_json() + [lead]
    generuj_dashboard(wszystkie)

    print("\n[OK] Lead dodany, dashboard odświeżony.\n")


if __name__ == "__main__":
    main()
