# Workflow — KuchniaHACCP

## Jak pracujemy
- Każdą sesję zaczynamy od przeczytania PROGRESS.md i memoria/dziennik.md
- Uruchamiamy aplikację: `python main.py`
- Zmiany commitujemy do repo GitHub (konto poulus)
- Przed nadpisaniem istniejącego pliku — zawsze pytaj

## Konwencje
- Daty w nazwach plików: YYYY-MM-DD_nazwa.md
- Tokeny i hasła nigdy nie trafiają do plików ani repo
- Konfiguracja wrażliwa → plik `.env` (dodany do `.gitignore`)

## Struktura projektu (docelowa)
```
kuchnia/
├── main.py              # główny skrypt
├── scrapers/
│   ├── olx.py           # scraping OLX RSS
│   ├── duckduckgo.py    # wyszukiwanie fraz
│   └── facebook.py      # (faza 2 — Apify)
├── bot/
│   └── telegram_bot.py  # wysyłanie leadów
├── config.py            # frazy kluczowe, ustawienia
├── .env                 # tokeny (nie w repo)
├── .gitignore
├── requirements.txt
├── memoria/
│   └── dziennik.md
└── pliki kontekstowe (PROFILE, CONTEXT, TECHSTACK, PROGRESS, WORKFLOW, ENDWORK)
```
