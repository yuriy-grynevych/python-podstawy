import json

# ===========================================================================
# ZBIORY (set)
# ===========================================================================

# ── 1. Tworzenie zbiorów ────────────────────────────────────────────────────
set1 = {"ala", "ola", "krzyś", "kubuś"}
set2 = {1, 2, 3, 4, 5}
set3 = {True, False, True, True, False}   # duplikaty usunięte → {False, True}
set4 = {"ala", 5, 2.5, True, None}

print(set1)
print(set2)
print(set3)
print(set4)

for n in set4:
    print(n)

# ── 2. Sprawdzanie elementów i długość zbioru ───────────────────────────────
if "ala" in set1:
    print("\"ala\" jest w zbiorze")
if "ola" in set1:
    print("\"ola\" jest w zbiorze")
if "ania" in set1:
    print("\"ania\" jest w zbiorze")
print("długość zbioru:", len(set1))

# ── 3. Dodawanie jednego elementu: add() ────────────────────────────────────
print(set1)
set1.add("piotruś")
print(set1)
set1.add("piotruś")   # duplikat – zbiór się nie zmieni
print(set1)

# ── 4. Dodawanie wielu elementów: update() ──────────────────────────────────
set1.update({"ania", "piotruś", "zosia", "jaś"})
print(set1)

# ── 5. Usuwanie elementu: discard() ─────────────────────────────────────────
print(set1)
set1.discard("piotruś")   # nie rzuca błędu gdy elementu nie ma
print(set1)

# ── 6. Czyszczenie zbioru i usuwanie zmiennej ───────────────────────────────
set1 = {"ala", "ola", "krzyś", "kubuś"}
print(set1)
set1.clear()              # zbiór pusty → set()
print(set1)

del set1                  # usuwa zmienną całkowicie
# print(set1)             # NameError – zmienna nie istnieje

# ── 7. Porównywanie zbiorów ─────────────────────────────────────────────────
set1 = {"ala", "ola", "krzyś", "kubuś"}
set2 = {"ala", "ola", "krzyś", "kubuś"}
set3 = {"ala", "krzyś", "ola", "kubuś"}   # ta sama zawartość, inna kolejność
set4 = {"1", "2", "3", "4"}               # cyfry jako stringi
set5 = {1, 2, 3, 4}                       # cyfry jako int

print(set1 == set2)   # True
print(set1 == set3)   # True  – kolejność nie ma znaczenia
print(set4 == set5)   # False – inne typy danych

# ── 8. Kopiowanie zbiorów ───────────────────────────────────────────────────
set1 = {"ala", "ola", "krzyś", "kubuś"}
set2 = set1              # przypisanie referencji – oba wskazują ten sam obiekt
set1.discard("ola")
print(set1)              # {'kubuś', 'ala', 'krzyś'}
print(set2)              # {'kubuś', 'ala', 'krzyś'} – też zmieniony!

set1 = {"ala", "ola", "krzyś", "kubuś"}
set2 = set1.copy()       # kopia niezależna
set1.discard("ola")
print(set1)              # {'kubuś', 'ala', 'krzyś'}
print(set2)              # {'kubuś', 'ola', 'ala', 'krzyś'} – bez zmian

# ── 9. Operacje matematyczne na zbiorach ────────────────────────────────────
set1 = {"ala", "ola", "krzyś", "kubuś"}
set2 = {"ania", "piotruś", "ola", "krzyś"}

print("suma:      ", set1.union(set2))          # wszystkie unikalne elementy
print("przecięcie:", set1.intersection(set2))   # tylko wspólne elementy
# suma i przecięcie zbiorów są przemienne


# ===========================================================================
# SŁOWNIKI (dict)
# ===========================================================================

# ── 10. Definicja słowników ─────────────────────────────────────────────────
oceny = {
    2: "ndst", 3: "dst", 3.5: "+dst",
    4: "db", 4.5: "+db", 5: "bdb",
    5.5: "cel", "z": "zal", "nk": "nieklasyfikowany"
}

osoba = {
    "imię": "Jan",
    "nazwisko": "Kowalski",
    "wiek": 18,
    "adres": {
        "ulica": "Rakowicka",
        "numer domu": 27,
        "kod pocztowy": "31-510",
        "miejscowość": "Kraków"
    }
}

opinia = {
    "author": "Anonim",
    "recommendation": True,
    "stars": 4.5,
    "purchased": False,
    "useful": 3,
    "unuseful": 0,
    "content": "super produkt",
    "advantages": ["cena", "jakość"],
    "disadvantages": [],
    "submit_date": "2021-04-01 12:00:00",
    "purchase_date": None
}

# ── 11. Wyświetlanie słownika i jego elementów ──────────────────────────────
print(oceny)
print(oceny[4.5])          # dostęp przez klucz → +db
print(oceny.get("nk"))     # bezpieczny dostęp  → nieklasyfikowany

print(osoba)
print(osoba["adres"])                             # zagnieżdżony słownik
print(osoba["adres"]["miejscowość"])              # dostęp przez [][]
print(osoba.get("adres").get("miejscowość"))      # dostęp przez get().get()

print(opinia)
print(opinia["advantages"])      # ['cena', 'jakość']
print(opinia.get("stars"))       # 4.5

# ── 12. Czytelne wyświetlanie (pretty print) ────────────────────────────────
print(json.dumps(oceny,  indent=4, ensure_ascii=False))
print(json.dumps(osoba,  indent=4, ensure_ascii=False))
print(json.dumps(opinia, indent=4, ensure_ascii=False))

# ── 13. Iterowanie po kluczach ──────────────────────────────────────────────
for ocena in oceny:           # domyślnie iteruje po kluczach
    print(ocena)

for key in oceny.keys():      # jawnie po kluczach
    print(key)

# ── 14. Iterowanie po wartościach ───────────────────────────────────────────
for ocena in oceny:
    print(oceny.get(ocena))

for value in oceny.values():  # jawnie po wartościach
    print(value)

# ── 15. Iterowanie po parach klucz-wartość ──────────────────────────────────
for item in oceny.items():    # zwraca krotki (klucz, wartość)
    print(item)

# ── 16. Zmiana wartości ─────────────────────────────────────────────────────
print(oceny)
oceny["z"] = "zaliczenie"     # zmiana istniejącego klucza
print(oceny)

# ── 17. Sprawdzanie, czy klucz istnieje ─────────────────────────────────────
if "z" in oceny:
    print("Stopień jest w słowniku")
else:
    print("Stopnia nie ma w słowniku")

if "bz" in oceny:
    print("Stopień jest w słowniku")
else:
    print("Stopnia nie ma w słowniku")

# ── 18. Dodawanie nowego elementu ───────────────────────────────────────────
print(oceny)
oceny["bz"] = "brak zaliczenia"   # nowy klucz → nowy element
print(oceny)

# ── 19. Pobieranie i usuwanie elementu: pop() ───────────────────────────────
print(len(oceny))             # liczba elementów
print(oceny.pop(5.5))         # usuwa klucz 5.5 i zwraca jego wartość → cel
print(len(oceny))             # o 1 mniej

# ── 20. Kopiowanie słowników ────────────────────────────────────────────────
dict1 = {"name": "Ala", "pet": "kot"}
dict2 = dict1              # referencja – zmiany w dict1 widać w dict2
dict1.pop("name")
print(dict1)               # {'pet': 'kot'}
print(dict2)               # {'pet': 'kot'} – też zmieniony!

dict1 = {"name": "Ala", "pet": "kot"}
dict2 = dict1.copy()       # niezależna kopia
dict1.pop("name")
print(dict1)               # {'pet': 'kot'}
print(dict2)               # {'name': 'Ala', 'pet': 'kot'} – bez zmian
