# Progress projektu — KuchniaHACCP

## Zrobione
- [2026-06-10] Wznowienie projektu — przegląd stanu, weryfikacja git, aktualizacja dziennika
- [2026-06-11] Historia leadów — deduplikacja między runami (seen_links.json + monitor.yml)
- [2026-06-11] Scraper Facebook przez DDG (scrapers/facebook.py) — daje 0 wyników (FB za loginem)
- [2026-06-11] Ręczne dodawanie leadów z FB — dodaj_lead.py
- [2026-06-11] Plakat FB — plakat_nowy.html w stylu złoto/czerń + wycięte logo (logo.png)
- [2026-05-22] Konfiguracja środowiska pracy Claude Code
- [2026-05-22] Zainstalowano claude-mem i Python 3.12
- [2026-05-22] Utworzono pliki kontekstowe: PROFILE, CONTEXT, TECHSTACK, PROGRESS, WORKFLOW, ENDWORK
- [2026-05-22] Zbudowano moduł wyszukiwania DuckDuckGo (scrapers/duckduckgo.py) z parserem dat
- [2026-05-22] Zbudowano Telegram bot (bot/telegram_bot.py) — gotowy, czeka na token
- [2026-05-22] Połączono moduły w main.py — aplikacja działa lokalnie
- [2026-05-22] Zainstalowano GitHub CLI (gh) — gotowy do użycia
- [2026-05-22] Zalogowano do GitHub (poulus13), utworzono repo kuchnia-haccp, pierwszy commit + push
- [2026-05-22] OLX usunięty z flow — OLX to tylko firmy oferujące HACCP, nie klienci
- [2026-05-22] Filtr jakości leadów — filtr dwusygnałowy (potrzeba + temat), tylko .pl, blacklista 20 domen
- [2026-05-22] SLOWA_OFERTY — odrzuca blogi, sklepy, reklamy konkurentów
- [2026-05-22] Dashboard HTML (docs/index.html) — karty leadów, otwiera się w przeglądarce po każdym runie
- [2026-05-22] GitHub Actions (monitor.yml) — automatyczny run o 08:00 i 20:00 PL
- [2026-05-22] GitHub Pages aktywne — dashboard dostępny pod linkiem z każdego miejsca
- [2026-05-22] Link do dashboardu: https://poulus13.github.io/kuchnia-haccp/

## Do zrobienia
### Priorytet — Telegram
- [ ] Zebrać Telegram Bot Token od Pawła (konto odblokowane) → wpisać do .env + GitHub Secret
- [ ] Przetestować wysyłkę przez Telegram

### Plakat FB
- [ ] Ocenić plakat_nowy.html w przeglądarce i wprowadzić poprawki
- [ ] Zrzut ekranu do PNG → gotowy do publikacji na FB

### Ulepszenia scrapera
- [ ] Dodać więcej fraz DDG — szukać na innych forach (gastrona.pl, reddit.pl, grupy FB przez Apify)
- [ ] Dodać historię leadów — nie wysyłać drugi raz tego samego linka
- [ ] Poprawić daty — więcej wyników bez daty (oznaczać jako "stare/nieznane")

### Faza 2 (później)
- [ ] Facebook scraping przez Apify (~$5-10/mies)
- [ ] Filtrowanie leadów przez Claude API
- [ ] Historia leadów w bazie (SQLite)

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
