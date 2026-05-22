# Progress projektu — KuchniaHACCP

## Zrobione
- [2026-05-22] Konfiguracja środowiska pracy Claude Code
- [2026-05-22] Zainstalowano claude-mem i Python 3.12
- [2026-05-22] Utworzono pliki kontekstowe: PROFILE, CONTEXT, TECHSTACK, PROGRESS, WORKFLOW, ENDWORK
- [2026-05-22] Zbudowano moduł scrapingu OLX RSS (scrapers/olx.py) z filtrem daty 14 dni
- [2026-05-22] Zbudowano moduł wyszukiwania DuckDuckGo (scrapers/duckduckgo.py) z parserem dat (bezwzględnych i względnych: "X days/weeks ago")
- [2026-05-22] Zbudowano Telegram bot (bot/telegram_bot.py) — gotowy, czeka na token
- [2026-05-22] Połączono moduły w main.py — aplikacja działa lokalnie
- [2026-05-22] Zainstalowano GitHub CLI (gh) — gotowy do użycia
- [2026-05-22] Przetestowano demo — 28-42 wyników na run, świeże leady z datami

## Do zrobienia
### Git / GitHub (priorytet)
- [ ] Zalogować się do GitHub: `gh auth login` (wymaga przeglądarki — zrób ręcznie)
- [ ] Utworzyć repo na GitHub: `gh repo create kuchnia-haccp --private`
- [ ] Init + pierwszy commit + push
- [ ] Dodać README.md z instrukcją uruchamiania

### Aplikacja — poprawki jakości
- [ ] Dodać blacklistę domen (stare fora bez daty: kafeteria, jbzd, wloski.ang.pl)
- [ ] Filtrować wyniki tylko do polskich domen (.pl) lub znanych forów
- [ ] Zebrać Telegram Bot Token od Pawła i skonfigurować .env
- [ ] Dodać harmonogram APScheduler (np. co 12h automatyczny run)
- [ ] Przetestować wysyłkę przez Telegram

### Faza 2 (później)
- [ ] Facebook scraping przez Apify (~$5-10/mies)
- [ ] Filtrowanie leadów przez Claude API
- [ ] Dashboard webowy z historią leadów

## Ważne decyzje
- [2026-05-22] Zaczynamy od darmowego MVP: OLX + DuckDuckGo + Telegram
- [2026-05-22] Facebook przez Apify — faza 2 (płatna, po weryfikacji wartości MVP)
- [2026-05-22] Filtrowanie AI (Claude API) — faza 2

## Otwarte pytania
- Jak Paweł chce otrzymywać powiadomienia — ile razy dziennie?
- Czy chce filtrować leady po regionie czy cała Polska?
- Jakie frazy kluczowe są najważniejsze?
