# Esercizi Risolti — Cicli `while`, `for`, `break` e `continue`

Raccolta completa di tutti gli esercizi proposti nei tre notebook su cicli e iterazioni.

---

## 1. Lettura Stringhe fino a Stringa Vuota
**Testo:** Legge una sequenza di stringhe da tastiera, stampa la lunghezza di ciascuna e termina quando l'utente preme solo invio (stringa vuota).

### Soluzione A (Lettura prima e poi in fondo al ciclo):
```python
s = input("Inserisci stringa (invio per terminare): ")
while s != "":
    print("Lunghezza:", len(s))
    s = input("Inserisci stringa (invio per terminare): ")
```

### Soluzione B (Lettura solo dentro il ciclo):
```python
while True:
    s = input("Inserisci stringa (invio per terminare): ")
    if s == "":
        break
    print("Lunghezza:", len(s))
```

---

## 2. Sequenza di Interi Positivi con Sentinella `*`
**Testo:** Legge interi positivi fino all'inserimento di `'*'` e stampa per ognuno se è pari o dispari.

```python
val = input("Inserisci intero positivo (* per finire): ")
while val != "*":
    num = int(val)
    if num % 2 == 0:
        print(num, "è PARI")
    else:
        print(num, "è DISPARI")
    val = input("Inserisci intero positivo (* per finire): ")
```

---

## 3. Rimuovere la Prima Occorrenza di un Carattere
**Testo:** Legge `s` e `c`. Stampa la stringa senza la prima occorrenza di `c` (es. `'casa', 'a' -> 'csa'`).

### Versione con Slicing & `find`:
```python
s = input("Stringa: ")
c = input("Carattere: ")

pos = s.find(c)
if pos != -1:
    print(s[:pos] + s[pos+1:])
else:
    print(s)
```

### Versione con `while`:
```python
s = input("Stringa: ")
c = input("Carattere: ")

risultato = ""
trovato = False
i = 0
while i < len(s):
    if s[i] == c and not trovato:
        trovato = True  # Salta solo la prima occorrenza
    else:
        risultato += s[i]
    i += 1
print(risultato)
```

---

## 4. Somma della Serie Armonica ($\sum_{k=1}^m \frac{1}{k}$)
**Testo:** Calcola la somma dei primi $m$ termini della serie armonica per un dato $m$.

```python
m = int(input("Inserisci m: "))
somma = 0.0
for k in range(1, m + 1):
    somma += 1.0 / k
print("Somma serie armonica:", somma)
```

---

## 5. Calcolo del Valore di un Polinomio di Grado Qualsiasi
**Testo:** Dato il grado $n$, il valore di $x$, e i coefficienti $a_0, a_1, \dots, a_n$ inseriti dall'utente, calcolare il valore del polinomio:
$$P(x) = a_n x^n + a_{n-1} x^{n-1} + \dots + a_1 x + a_0$$

```python
grado = int(input("Inserisci grado del polinomio: "))
x = float(input("Inserisci il valore di x: "))

risultato = 0.0
for i in range(grado + 1):
    coeff = float(input(f"Inserisci coefficiente per grado {i} (a_{i}): "))
    risultato += coeff * (x ** i)

print("Il valore del polinomio è:", risultato)
```

---

## 6. Conversione da Base 2 a Base 8 (a gruppi di 3 bit)
**Testo:** Converte una stringa binaria in ottale raggruppando i bit a terzetti da destra verso sinistra.

```python
b = input("Inserisci numero binario: ")

# Aggiunge zeri in testa per renderlo divisibile per 3
resto = len(b) % 3
if resto != 0:
    b = "0" * (3 - resto) + b

ottale = ""
for i in range(0, len(b), 3):
    gruppo = b[i : i + 3]
    valore = int(gruppo[0]) * 4 + int(gruppo[1]) * 2 + int(gruppo[2]) * 1
    ottale += str(valore)

print("Numero in ottale (base 8):", ottale)
```

---

## 7. Carattere con Codice Unicode Minimo
**Testo:** Trova il carattere con il codice Unicode minore all'interno di una stringa.

### Con ciclo sui caratteri:
```python
s = input("Inserisci stringa: ")
if len(s) > 0:
    min_car = s[0]
    for c in s:
        if ord(c) < ord(min_car):
            min_car = c
    print("Carattere minimo:", min_car, "con codice:", ord(min_car))
```

---

## 8. Verifica Presenza di Lettere Doppie Consecutive
**Testo:** Verifica con un ciclo se nella stringa ci sono due lettere alfabetiche uguali consecutive. Stampa `'SI'` o `'NO'`.

```python
s = input("Inserisci stringa: ")
trovata_doppia = False

for i in range(len(s) - 1):
    if s[i].isalpha() and s[i] == s[i+1]:
        trovata_doppia = True
        break

if trovata_doppia:
    print("SI")
else:
    print("NO")
```
