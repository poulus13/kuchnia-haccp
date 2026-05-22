from ddgs import DDGS
from datetime import datetime, timedelta
from config import ETYKIETY_LEADOW
import re

MAX_WIEK_DNI = 14


def szukaj_ddgo(frazy: list[str], max_na_fraze: int = 5) -> list[dict]:
    leady = []
    seen = set()
    granica = datetime.now() - timedelta(days=MAX_WIEK_DNI)

    with DDGS() as ddgs:
        for fraza in frazy:
            try:
                # timelimit="m" = ostatni miesiąc, potem filtrujemy do 14 dni
                wyniki = ddgs.text(fraza, region="pl-pl", max_results=max_na_fraze, timelimit="m")
                for w in wyniki:
                    link = w.get("href", "")
                    if link in seen:
                        continue
                    seen.add(link)
                    tytul = w.get("title", "")
                    opis = w.get("body", "")
                    data_str, data = _wyciagnij_date(opis + " " + tytul)

                    # odrzuć jeśli data jest znana i starsza niż 14 dni
                    if data and data < granica:
                        continue

                    if _czy_lead(tytul + " " + opis):
                        leady.append({
                            "zrodlo": "Web",
                            "tytul": tytul,
                            "link": link,
                            "opis": opis[:200],
                            "data": data_str or "?",
                        })
            except Exception as e:
                print(f"  [DDG] Blad dla '{fraza}': {e}")
    return leady


def _czy_lead(tekst: str) -> bool:
    tekst_lower = tekst.lower()
    return any(etk in tekst_lower for etk in ETYKIETY_LEADOW)


def _wyciagnij_date(tekst: str) -> tuple[str | None, datetime | None]:
    now = datetime.now()

    # względne: "3 days ago", "2 weeks ago", "1 month ago"
    m = re.search(r"(\d+)\s+day[s]?\s+ago", tekst, re.IGNORECASE)
    if m:
        d = now - timedelta(days=int(m.group(1)))
        return d.strftime("%Y-%m-%d"), d

    m = re.search(r"(\d+)\s+week[s]?\s+ago", tekst, re.IGNORECASE)
    if m:
        d = now - timedelta(weeks=int(m.group(1)))
        return d.strftime("%Y-%m-%d"), d

    m = re.search(r"(\d+)\s+month[s]?\s+ago", tekst, re.IGNORECASE)
    if m:
        d = now - timedelta(days=int(m.group(1)) * 30)
        return d.strftime("%Y-%m-%d"), d

    # bezwzględne daty
    wzorce_fmt = [
        (r"\b(202[5-6]-\d{2}-\d{2})\b", "%Y-%m-%d"),
        (r"\b(\w+\s+\d{1,2},\s+202[5-6])\b", "%B %d, %Y"),
        (r"\b(\d{1,2}\.\d{2}\.202[5-6])\b", "%d.%m.%Y"),
    ]
    miesiace_pl = {
        "stycznia": "January", "lutego": "February", "marca": "March",
        "kwietnia": "April", "maja": "May", "czerwca": "June",
        "lipca": "July", "sierpnia": "August", "września": "September",
        "października": "October", "listopada": "November", "grudnia": "December",
    }
    for wzorzec, fmt in wzorce_fmt:
        m = re.search(wzorzec, tekst, re.IGNORECASE)
        if m:
            s = m.group(1)
            for pl, en in miesiace_pl.items():
                s = s.lower().replace(pl, en)
            try:
                d = datetime.strptime(s.strip(), fmt)
                return d.strftime("%Y-%m-%d"), d
            except ValueError:
                continue

    return None, None
