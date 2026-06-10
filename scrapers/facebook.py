from ddgs import DDGS
from config import FRAZY_FACEBOOK, SYGNALY_POTRZEBY, SYGNALY_TEMATU, SLOWA_OFERTY


def szukaj_facebook(max_na_fraze: int = 10) -> list[dict]:
    leady = []
    seen = set()

    with DDGS() as ddgs:
        for fraza in FRAZY_FACEBOOK:
            try:
                wyniki = ddgs.text(fraza, region="pl-pl", max_results=max_na_fraze)
                for w in wyniki:
                    link = w.get("href", "")
                    if link in seen:
                        continue
                    if "facebook.com" not in link:
                        continue
                    seen.add(link)
                    tytul = w.get("title", "")
                    opis = w.get("body", "")
                    tekst = tytul + " " + opis
                    if _czy_lead(tekst) and not _czy_oferta(tekst):
                        leady.append({
                            "zrodlo": "Facebook",
                            "tytul": tytul,
                            "link": link,
                            "opis": opis[:200],
                            "data": "?",
                        })
            except Exception as e:
                print(f"  [FB] Blad dla '{fraza}': {e}")
    return leady


def _czy_lead(tekst: str) -> bool:
    t = tekst.lower()
    ma_potrzebe = any(s in t for s in SYGNALY_POTRZEBY)
    ma_temat = any(s in t for s in SYGNALY_TEMATU)
    return ma_potrzebe and ma_temat


def _czy_oferta(tekst: str) -> bool:
    return any(s in tekst.lower() for s in SLOWA_OFERTY)
