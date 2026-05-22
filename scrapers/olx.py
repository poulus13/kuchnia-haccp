import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
from config import SYGNALY_POTRZEBY, SYGNALY_TEMATU, SLOWA_OFERTY

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
}
MAX_WIEK_DNI = 14
BASE = "https://www.olx.pl"

OLX_FRAZY = [
    "szukam haccp",
    "potrzebuję dokumentację haccp",
    "kto zrobi haccp",
    "projekt technologiczny kuchni",
    "szukam technologa żywności",
    "odbiór sanepid lokal",
]


def szukaj_olx(zapytania: list[str]) -> list[dict]:
    leady = []
    seen = set()

    for q in zapytania + OLX_FRAZY:
        q_url = q.replace(" ", "-")
        url = f"{BASE}/oferty/q-{q_url}/"
        try:
            r = requests.get(url, headers=HEADERS, timeout=15)
            if r.status_code != 200:
                continue
            soup = BeautifulSoup(r.text, "html.parser")
            cards = soup.select('[data-cy="l-card"]')

            for card in cards:
                link_tag = card.select_one("a[href]")
                if not link_tag:
                    continue
                href = link_tag["href"]
                link = href if href.startswith("http") else BASE + href
                if link in seen:
                    continue
                seen.add(link)

                title_tag = card.select_one("h4, h6")
                tytul = title_tag.text.strip() if title_tag else ""
                desc_tag = card.select_one("p")
                opis = desc_tag.text.strip() if desc_tag else ""
                tekst = tytul + " " + opis

                if _czy_lead(tekst) and not _czy_oferta(tekst):
                    leady.append({
                        "zrodlo": "OLX",
                        "tytul": tytul,
                        "link": link,
                        "opis": opis[:200],
                        "data": "?",
                    })
        except Exception as e:
            print(f"  [OLX] Blad dla '{q}': {e}")
    return leady


def _czy_lead(tekst: str) -> bool:
    t = tekst.lower()
    ma_potrzebe = any(s in t for s in SYGNALY_POTRZEBY)
    ma_temat = any(s in t for s in SYGNALY_TEMATU)
    return ma_potrzebe and ma_temat


def _czy_oferta(tekst: str) -> bool:
    t = tekst.lower()
    return any(s in t for s in SLOWA_OFERTY)
