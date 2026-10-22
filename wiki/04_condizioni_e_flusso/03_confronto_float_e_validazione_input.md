# Confronto tra Numeri Reali (`float`) e Validazione dell'Input

## 1. Il Problema dell'Uguaglianza tra Numeri Reali
Nei calcolatori i numeri reali (`float`) sono rappresentati con un numero limitato di bit (standard IEEE 754), provocando piccoli errori di troncamento o arrotondamento binario.

### Esempio Pratico:
```python
import math
x = math.sqrt(2)
print(x ** 2 == 2)  # Produce False! Infatti x**2 vale 2.0000000000000004
```

> [!CAUTION]
> **MAI usare `==` per confrontare numeri a virgola mobile (`float`)!**

---

## 2. Le Due Soluzioni Corrette

### Metodo 1: Tolleranza Epsilon con `abs()`
Si controlla se la differenza in valore assoluto è inferiore a una soglia microscopica (es. $\epsilon = 10^{-6}$):
```python
epsilon = 1e-6
if abs((x ** 2) - 2) < epsilon:
    print("Uguali entro la tolleranza!")
```

### Metodo 2: Funzione `math.isclose()`
La funzione standard del modulo `math`:
```python
from math import isclose

if isclose(x ** 2, 2):
    print("Uguali con isclose!")
```

---

## 3. Algoritmo di Validazione Input: Numero Reale con Segno
Uno degli esercizi/esempi più importanti trattati nelle dispense del docente: verificare se una stringa inserita dall'utente rappresenta un numero reale valido (es. `-34.567`, `+4.`, `.5`).

### Logica Algoritmica:
1. Rimuovere gli spazi esterni con `strip()`.
2. Se il primo carattere è `+` o `-`, rimuoverlo dalla stringa da controllare.
3. Se non c'è il punto `.` $\rightarrow$ deve essere un intero valido (`s.isdecimal()`).
4. Se c'è il punto:
   - Trovare l'indice del punto: `iP = s.find('.')`.
   - Suddividere in parte intera `pi = s[:iP]` e parte frazionaria `pf = s[iP+1:]`.
   - Se `len(pi) == 0`: valido se `pf.isdecimal()` (es. `.5`).
   - Se `len(pf) == 0`: valido se `pi.isdecimal()` (es. `4.`).
   - Se entrambe le parti hanno caratteri: valido se `pi.isdecimal() and pf.isdecimal()`.

```python
s1 = input("Inserisci un numero reale: ").strip()

# Gestione segno opzionale
if len(s1) > 0 and s1[0] in '+-':
    s = s1[1:]
else:
    s = s1

if '.' not in s:
    convertibile = s.isdecimal()
else:
    iP = s.find('.')
    pi = s[:iP]      # Parte intera
    pf = s[iP + 1:]  # Parte frazionaria
    
    if len(pi) == 0:
        convertibile = pf.isdecimal()
    elif len(pf) == 0:
        convertibile = pi.isdecimal()
    else:
        convertibile = pi.isdecimal() and pf.isdecimal()

print("Convertibile?", convertibile)
```
