from ddgs import DDGS
from datetime import datetime, timedelta
from config import SYGNALY_POTRZEBY, SYGNALY_TEMATU, SLOWA_OFERTY
from urllib.parse import urlparse
import re

MAX_WIEK_DNI = 14

BLACKLISTA_DOMEN = [
    "goldenline.pl",
    "kafeteria.pl",
    "jbzd.com.pl",
    "wloski.ang.pl",
    "wikipedia.org",
    "wikipedia.com",
    "allmo.pl",
    "tanake.com.pl",
    "restobusiness.pl",
    "agusto.pl",
    "niepoddawajsie.pl",
    "lsi-lublin.pl",
    "bhpomocnik.pl",
    "goga-gastro.pl",
    "franchising.pl",
    "praca-biznes.pl",
    "englishmyway.pl",
    "marketing-arlek.pl",
    "wizaz.pl",
    "samequizy.pl",
]


def _czy_pl(link: str) -> bool:
    try:
        domena = urlparse(link).netloc.lower().removeprefix("www.")
        # sprawdź blacklistę — obsługuje też subdomeny (f.kafeteria.pl)
        if any(domena == b or domena.endswith("." + b) for b in BLACKLISTA_DOMEN):
            return False
        return domena.endswith(".pl")
    except Exception:
        return False


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
                    if not _czy_pl(link):
                        continue
                    seen.add(link)
                    tytul = w.get("title", "")
                    opis = w.get("body", "")
                    data_str, data = _wyciagnij_date(opis + " " + tytul)

                    # odrzuć jeśli data jest znana i starsza niż 14 dni
                    if data and data < granica:
                        continue

                    tekst = tytul + " " + opis
                    if _czy_lead(tekst) and not _czy_oferta(tekst):
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
    t = tekst.lower()
    ma_potrzebe = any(s in t for s in SYGNALY_POTRZEBY)
    ma_temat = any(s in t for s in SYGNALY_TEMATU)
    return ma_potrzebe and ma_temat


def _czy_oferta(tekst: str) -> bool:
    tekst_lower = tekst.lower()
    return any(s in tekst_lower for s in SLOWA_OFERTY)


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
