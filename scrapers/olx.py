import feedparser
import requests
from datetime import datetime, timedelta
from config import ETYKIETY_LEADOW
import time

HEADERS = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}
MAX_WIEK_DNI = 14


def szukaj_olx(zapytania: list[str]) -> list[dict]:
    leady = []
    granica = datetime.now() - timedelta(days=MAX_WIEK_DNI)

    for q in zapytania:
        q_url = q.replace(" ", "-")
        url = f"https://www.olx.pl/oferty/q-{q_url}/feed/rss/"
        try:
            r = requests.get(url, headers=HEADERS, timeout=10)
            feed = feedparser.parse(r.text)
            for wpis in feed.entries[:10]:
                # filtr daty
                pub = wpis.get("published_parsed")
                if pub:
                    data = datetime(*pub[:6])
                    if data < granica:
                        continue
                    data_str = data.strftime("%Y-%m-%d")
                else:
                    data_str = "brak daty"

                tytul = wpis.get("title", "")
                opis = wpis.get("summary", "")
                link = wpis.get("link", "")
                if _czy_lead(tytul + " " + opis):
                    leady.append({
                        "zrodlo": "OLX",
                        "tytul": tytul,
                        "link": link,
                        "opis": opis[:200],
                        "data": data_str,
                    })
        except Exception as e:
            print(f"  [OLX] Blad dla '{q}': {e}")
    return leady


def _czy_lead(tekst: str) -> bool:
    tekst_lower = tekst.lower()
    return any(etk in tekst_lower for etk in ETYKIETY_LEADOW)
