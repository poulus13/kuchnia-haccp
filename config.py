FRAZY_DDGO = [
    # Pytania na forach — ktoś szuka pomocy
    "site:forum.gastro.pl otwieramy lokal",
    "site:forum.gastro.pl sanepid odbiór",
    "site:forumgastronomiczne.pl haccp potrzebuję",
    "site:forumgastronomiczne.pl otwieramy lokal",
    # Szukający pomocy — frazy intencji
    "\"potrzebuję dokumentację haccp\"",
    "\"kto zrobi haccp\" lokal",
    "\"szukam kogoś do haccp\"",
    "\"otwieramy restaurację\" \"co z sanepidem\"",
    "\"otwieramy lokal\" dokumentacja forum",
    "\"odbiór sanepid\" \"co potrzeba\" forum",
    "\"otwieram bar\" sanepid formalności forum",
    "\"projekt technologiczny kuchni\" potrzebuję",
    "\"szkolenie haccp\" kucharze restauracja szukam",
    "\"szukam technologa żywności\" lokal",
    "\"kto może zrobić\" haccp restauracja",
    "\"pomóżcie\" haccp lokal gastronomiczny forum",
]

OLX_ZAPYTANIA = [
    "haccp szukam",
    "dokumentacja haccp",
    "projekt kuchni",
    "technolog żywności",
    "sanepid odbiór",
]

# Sygnały POTRZEBY — ktoś szuka, pyta, nie wie
SYGNALY_POTRZEBY = [
    "szukam", "szukamy", "potrzebuj", "potrzebuję", "potrzebujemy",
    "kto zrobi", "kto wykona", "kto może zrobić",
    "zlec", "zatrudni", "chcę zlecić",
    "nie wiem jak", "od czego zacząć", "co potrzeba", "jak to zrobić",
    "otwieramy lokal", "otwieram lokal", "otwieramy restauracj", "otwieram restauracj",
    "otwieramy bar", "otwieram bar", "otwieramy kawiarni", "otwieram kawiarni",
    "otwieramy gastronomię", "otwieram gastronomię",
]

# Sygnały TEMATU — musi dotyczyć naszej branży
SYGNALY_TEMATU = [
    "haccp", "ghp", "gmp", "sanepid",
    "projekt technologiczny", "projekt kuchni gastronomiczn",
    "dokumentacja sanitarna", "dokumentacja haccp",
    "technolog żywności", "technolog gastronomii",
    "odbiór lokalu", "odbiór sanepid",
    "lokal gastronomiczny", "gastronomii", "gastronomiczn",
]

# Zachowane dla kompatybilności z OLX (używa tej listy)
ETYKIETY_LEADOW = SYGNALY_POTRZEBY + SYGNALY_TEMATU

# Słowa wskazujące że ogłoszenie pochodzi od firmy OFERUJĄCEJ usługę (odrzucamy)
SLOWA_OFERTY = [
    "oferuję", "oferujemy", "nasza oferta", "nasze usługi", "sprawdź ofertę",
    "zamów", "zadzwoń do nas", "skontaktuj się z nami",
    "cena od", "cennik", "pobierz wzór", "pobierz szablon", "wzór do pobrania",
    "sklep", "kup teraz", "dodaj do koszyka",
    "szkolenie online", "kurs online", "e-learning",
    "wykonam dokumentację", "wykonuję haccp", "sporządzam dokumentację",
    "świadczymy usługi", "kompleksowa obsługa", "profesjonalna obsługa",
    "profesjonalny projekt", "profesjonalna dokumentacja",
    "potrzebujesz projektu", "potrzebujesz dokumentacji",
    "sprawdź jak", "dowiedz się", "przeczytaj",
    "skontaktuj", "zapytaj o wycenę", "bezpłatna wycena",
    "nasze doświadczenie", "zaufali nam", "nasi klienci",
    "kompletny przewodnik", "poradnik", "artykuł",
    "100% zgodności", "gwarantujemy",
]
