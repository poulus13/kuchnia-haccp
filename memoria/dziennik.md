# Dziennik Aktywności — KuchniaHACCP

## [2026-05-22 01:10] — Sesja: budowa MVP
- Omówiono zakres projektu: aplikacja monitorująca leady dla Pawła (HACCP, Sanepid, konsultacje gastronomiczne)
- Wybrano architekturę: Python + scraping (OLX, DuckDuckGo) + Telegram bot
- Zainstalowano Python 3.12 (winget) i GitHub CLI (gh)
- Zbudowano i przetestowano pełne MVP: scrapers/olx.py, scrapers/duckduckgo.py, bot/telegram_bot.py, main.py
- Dodano filtr dat: tylko leady nie starsze niż 14 dni
- Dodano parser dat względnych ("X days/weeks ago") i bezwzględnych
- Demo działa — 28-42 wyników na run, świeże leady z datami
- Telegram gotowy — czeka na token od Pawła
- GitHub CLI zainstalowany — czeka na `gh auth login` (wymaga przeglądarki, zrób ręcznie)

### Następna sesja — priorytety:
1. `gh auth login` → init repo → push na GitHub
2. Blacklista starych domen bez daty
3. Token Telegram od Pawła → test wysyłki

## [2026-06-10] — Sesja: przegląd stanu projektu
- Wznowiono projekt po ~19 dniach przerwy
- Odczytano ENDWORK.md — weryfikacja stanu repo
- Pliki `memoria/` i `.env.example` nadal nieśledzone przez git (niezacommitowane)
- Brak nowych zmian w kodzie w tej sesji
- Projekt czeka na: Token Telegram od Pawła + commit zaległych plików

### Następna sesja — priorytety:
1. Zacommitować `memoria/` i `.env.example`
2. Token Telegram od Pawła → test wysyłki
3. Historia leadów — nie wysyłać dwa razy tego samego linka
