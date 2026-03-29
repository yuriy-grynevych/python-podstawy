# Python – Podstawy

Materiały z zajęć – Katedra Systemów Obliczeniowych (29.03.2026)

## Zawartość repozytorium

| Plik                      | Temat                                                              |
|---------------------------|--------------------------------------------------------------------|
| `typy_petle_listy.py`     | Typy danych, stringi, warunki, pętle for/while, listy, krotki     |
| `zbiory_i_slowniki.py`    | Zbiory (set) i słowniki (dict)                                     |

---

## TYPY DANYCH

```python
i = 5          # int
cena = 2.5     # float
c = 2 + 5j     # complex
b = True       # bool
s = "Tekst"    # str
n = None       # NoneType
```

Sprawdzanie typu: `isinstance(i, int)` → `True`

### Konwersja typów

```python
int(True)    # 1
float(False) # 0.0
str(True)    # 'True'
bool(0)      # False
bool("")     # False  – pusty string to False
bool("abc")  # True   – niepusty string to True
bool(None)   # False
```

---

## STRINGI (`str`)

### Tworzenie

```python
s1 = 'tekst jednoliniowy'
s2 = """tekst
wieloliniowy"""
s3 = 'tekst z\nnową linią'
```

### Formatowanie

```python
print('wartość: %.1f' % cena)             # stary styl
print(s1.format("Katarzyna", 18))         # .format()
print(f'{x} + {y} = {x+y}')              # f-string (zalecane)
```

### Metody

| Metoda              | Opis                              |
|---------------------|-----------------------------------|
| `s.upper()`         | Wielkie litery (oryginał bez zmian) |
| `s.lower()`         | Małe litery (oryginał bez zmian)  |
| `s.replace(a, b)`   | Zamienia `a` na `b`; można łączyć: `.replace(...).replace(...)` |

---

## WARUNKI

```python
if i < 0:
    print("ujemna")
elif i == 0:
    pass          # nic nie rób
else:
    print("dodatnia")
```

---

## PĘTLE

### `for` z `range()`

```python
for i in range(1, n+1):    # od 1 do n włącznie
    factorial *= i

for i in range(2, n):
    if n % i == 0:
        print("nie pierwsza"); break
else:
    print("pierwsza")      # else wykonuje się gdy pętla skończyła się BEZ break
```

Instrukcje sterujące:
- `break` – przerywa pętlę
- `continue` – przechodzi do następnej iteracji

### `while`

```python
while n > 0:
    factorial *= n
    n -= 1

while i < n:
    if n % i == 0:
        print("nie pierwsza"); break
    i += 1
else:
    print("pierwsza")      # else jak w for – gdy brak break
```

---

## LISTY (`list`)

### Tworzenie i dostęp

```python
list1 = ["ala", "ola", "krzys", "kubus"]
list1[0]      # pierwszy element
list1[-1]     # ostatni
list1[1:-1]   # slice (bez pierwszego i ostatniego)
```

### Iterowanie

```python
for n in list1:   print(n)   # po jednym
print(*list1)                # wszystkie w jednej linii
```

### Modyfikacja

| Operacja                  | Opis                                        |
|---------------------------|---------------------------------------------|
| `list1[1] = "ania"`       | Zmiana elementu na indeksie                 |
| `list1.append(x)`         | Dodaje na koniec                            |
| `list1.insert(i, x)`      | Wstawia na pozycję `i`                      |
| `list1.remove(x)`         | Usuwa pierwsze wystąpienie `x`              |
| `list1.pop()`             | Usuwa i zwraca ostatni element              |
| `list1.pop(i)`            | Usuwa i zwraca element z indeksu `i`        |
| `list1.clear()`           | Czyści listę → `[]`                         |
| `del list1`               | Usuwa zmienną                               |
| `list1.copy()`            | Niezależna kopia                            |
| `list1 + list2`           | Łączenie list                               |
| `list1.sort()`            | Sortowanie rosnąco                          |
| `list1.sort(reverse=True)`| Sortowanie malejąco                         |
| `list1.count(x)`          | Liczba wystąpień `x`                        |
| `list1.index(x)`          | Indeks pierwszego wystąpienia `x`           |

> `list2 = list1` → referencja (zmiany widać w obu)
> `list2 = list1.copy()` → niezależna kopia

---

## KROTKI (`tuple`)

```python
tuple1 = ("ala", "ola", "krzys", "kubus")
tuple1[0]     # pierwszy element
tuple1[-1]    # ostatni
tuple1[1:-1]  # slice
```

Krotka jest **niemutowalna** – po utworzeniu nie można zmieniać jej elementów.

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
python typy_petle_listy.py
python zbiory_i_slowniki.py
```
