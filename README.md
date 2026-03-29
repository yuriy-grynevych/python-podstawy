# Python – Zbiory i Słowniki

Materiały z zajęć – Katedra Systemów Obliczeniowych (29.03.2026)

## Zawartość repozytorium

| Plik                      | Temat                                    |
|---------------------------|------------------------------------------|
| `zbiory_i_slowniki.py`    | Kompletny przykład zbiorów i słowników   |

---

## ZBIORY (`set`)

### Tworzenie

```python
set1 = {"ala", "ola", "krzyś", "kubuś"}   # stringi
set2 = {1, 2, 3, 4, 5}                    # liczby całkowite
set3 = {True, False, True, True, False}   # bool – duplikaty usunięte → {False, True}
set4 = {"ala", 5, 2.5, True, None}        # typy mieszane
```

**Cechy zbioru:**
- Brak duplikatów – powtarzające się wartości są automatycznie usuwane
- Brak ustalonej kolejności – elementy mogą wyświetlać się w dowolnej kolejności
- Może zawierać różne typy danych

### Sprawdzanie elementów

```python
if "ala" in set1:
    print("ala jest w zbiorze")
print(len(set1))    # liczba elementów
```

### Dodawanie elementów

| Metoda          | Opis                                  |
|-----------------|---------------------------------------|
| `add(x)`        | Dodaje jeden element                  |
| `update({…})`   | Dodaje wiele elementów naraz          |

### Usuwanie elementów

| Metoda / Instrukcja | Opis                                          |
|---------------------|-----------------------------------------------|
| `discard(x)`        | Usuwa element; brak błędu gdy nie istnieje    |
| `clear()`           | Czyści zbiór → `set()`                        |
| `del zmienna`       | Usuwa zmienną całkowicie → `NameError`        |

### Porównywanie

```python
set1 = {"ala", "ola"}
set2 = {"ola", "ala"}
print(set1 == set2)   # True – kolejność nie ma znaczenia
```

> `{"1", "2"} != {1, 2}` – stringi i liczby to różne typy

### Kopiowanie

```python
set2 = set1          # referencja – zmiany w set1 widać w set2
set2 = set1.copy()   # niezależna kopia
```

### Operacje matematyczne

| Metoda                | Wynik                                   |
|-----------------------|-----------------------------------------|
| `union(set2)`         | Suma – wszystkie unikalne elementy      |
| `intersection(set2)`  | Przecięcie – tylko wspólne elementy     |

> Suma i przecięcie są **przemienne**: `A.union(B) == B.union(A)`

---

## SŁOWNIKI (`dict`)

Słownik przechowuje pary **klucz: wartość**. Klucze muszą być unikalne i niezmienne (`int`, `float`, `str`). Wartości mogą być dowolnego typu.

### Tworzenie

```python
oceny = {
    2: "ndst", 3: "dst", 3.5: "+dst",
    4: "db", 4.5: "+db", 5: "bdb",
    5.5: "cel", "z": "zal", "nk": "nieklasyfikowany"
}
```

Słownik może zawierać zagnieżdżone słowniki, listy i wartości `None`:

```python
osoba = {
    "imię": "Jan",
    "wiek": 18,
    "adres": {
        "ulica": "Rakowicka",
        "miejscowość": "Kraków"
    }
}
```

### Odczyt wartości

| Sposób                        | Opis                                          |
|-------------------------------|-----------------------------------------------|
| `slownik[klucz]`              | Bezpośredni – `KeyError` gdy brak klucza      |
| `slownik.get(klucz)`          | Bezpieczny – zwraca `None` gdy brak klucza    |
| `slownik["a"]["b"]`           | Zagnieżdżony dostęp przez `[][]`              |
| `slownik.get("a").get("b")`   | Zagnieżdżony dostęp przez `get().get()`       |

### Iterowanie

```python
for k in slownik:             # klucze (domyślnie)
for k in slownik.keys():      # klucze (jawnie)
for v in slownik.values():    # wartości
for item in slownik.items():  # krotki (klucz, wartość)
```

### Modyfikacja i zarządzanie

| Operacja                     | Efekt                                       |
|------------------------------|---------------------------------------------|
| `slownik[klucz] = wartość`   | Zmiana istniejącego lub dodanie nowego      |
| `slownik.pop(klucz)`         | Usuwa element i **zwraca** jego wartość     |
| `"klucz" in slownik`         | Sprawdza istnienie klucza (`True`/`False`)  |
| `len(slownik)`               | Liczba par klucz-wartość                    |

### Kopiowanie słowników

```python
dict2 = dict1          # referencja – zmiany w dict1 widać w dict2
dict2 = dict1.copy()   # niezależna kopia
```

### Pretty print (czytelny wydruk)

```python
import json
print(json.dumps(slownik, indent=4, ensure_ascii=False))
```

`ensure_ascii=False` – poprawne wyświetlanie polskich znaków.

---

## Uruchomienie

```bash
python zbiory_i_slowniki.py
```
