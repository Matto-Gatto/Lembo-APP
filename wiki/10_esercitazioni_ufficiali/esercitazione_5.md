# Esercitazione Ufficiale n. 5 — 3 Novembre 2025
> **Argomenti:** Cicli `while` e `for`, accumulatori, manipolazioni di stringhe e disegno figure geometriche con contorni e diagonali.

---

## 1. Caratteri Alternati di Due Stringhe di Pari Lunghezza
**Traccia:** Date due stringhe $s_1, s_2$ di pari lunghezza, stampa la stringa con caratteri alternati.  
*Esempi:* `'casa'`, `'mora'` $\rightarrow$ `'cmaosraa'`; `'pippo'`, `'pluto'` $\rightarrow$ `'ppilpuptoo'`.
```python
s1 = input("Prima stringa: ")
s2 = input("Seconda stringa: ")

risultato = ""
for i in range(len(s1)):
    risultato += s1[i] + s2[i]

print(risultato)
```

---

## 2. Caratteri Ripetuti $n$ Volte Ciascuno
**Traccia:** Data una stringa $s$ e un intero positivo $n$, stampa una nuova stringa in cui ogni carattere di $s$ è ripetuto $n$ volte (es. `'casa'`, $2 \rightarrow$ `'ccaassaa'`).
```python
s = input("Stringa: ")
n = int(input("Intero n: "))

risultato = ""
for c in s:
    risultato += c * n

print(risultato)
```

---

## 3. Caratteri di $s_1$ che NON Appaiono in $s_2$
**Traccia:** Date due stringhe $s_1$ ed $s_2$, stampa la stringa composta da tutti i caratteri di $s_1$ che non compaiono in $s_2$, nello stesso ordine di $s_1$ (es. `'casa'`, `'martellare'` $\rightarrow$ `'cs'`; `'cassa'`, `'martello'` $\rightarrow$ `'css'`).
```python
s1 = input("s1: ")
s2 = input("s2: ")

risultato = ""
for c in s1:
    if c not in s2:
        risultato += c

print(risultato)
```

---

## 4. Multipli di $n_1$ Strettamente Minori di $n_2$
**Traccia:** Dati due interi positivi $n_1, n_2$, stampa uno per riga i multipli di $n_1$ (incluso $n_1$) strettamente minori di $n_2$ (es. $5, 16 \rightarrow 5, 10, 15$; $3, 15 \rightarrow 3, 6, 9, 12$; $7, 8 \rightarrow 7$).
```python
n1 = int(input("n1: "))
n2 = int(input("n2: "))

multiplo = n1
while multiplo < n2:
    print(multiplo)
    multiplo += n1
```

---

## 5. Due Lettere Uguali a Distanza Esattamente $n$
**Traccia:** Data una stringa $s$ (almeno 2 caratteri) e un intero $n > 0$, stampa `True` se compaiono due lettere uguali separate da una distanza pari ad $n$ ($s[i] == s[i+n]$), altrimenti `False`.  
*Esempi:* `'casa'`, $2 \rightarrow$ `True` ($s[0]=='c', s[2]=='s'$ no; $s[1]=='a', s[3]=='a'$ sì!); `'cassa'`, $2 \rightarrow$ `False`; `'abba'`, $1 \rightarrow$ `True`.
```python
s = input("Stringa: ")
n = int(input("Distanza n: "))

trovato = False
for i in range(len(s) - n):
    if s[i] == s[i + n]:
        trovato = True
        break

print(trovato)
```

---

## 6. Massima Distanza tra Due Caratteri Uguali
**Traccia:** Data una stringa, stampa la più lunga distanza tra due caratteri uguali ($rfind(c) - find(c)$). Se nessun carattere si ripete, stampa `0`.  
*Esempi:* `'abracadabra'` $\rightarrow 10$ (tra prima e ultima `'a'`); `'mamma'` $\rightarrow 3$ (tra indice 1 e 4 per `'m'`).
```python
s = input("Stringa: ")

max_distanza = 0
for c in s:
    prima = s.find(c)
    ultima = s.rfind(c)
    distanza = ultima - prima
    if distanza > max_distanza:
        max_distanza = distanza

print(max_distanza)
```

---

## 7. Verifica Presenza di Almeno un Carattere Duplicato
**Traccia:** Stampa `True` se nella stringa c'è almeno un carattere che compare più di una volta, altrimenti `False` (es. `'casa'` $\rightarrow$ `True`, `'tre'` $\rightarrow$ `False`).
```python
s = input("Stringa: ")

ha_duplicati = False
for c in s:
    if s.count(c) > 1:
        ha_duplicati = True
        break

print(ha_duplicati)
```

---

## 8. Massimo Comun Divisore (MCD)
**Traccia:** Dati due interi positivi $n_1, n_2$, stampa il loro Massimo Comun Divisore.
```python
n1 = int(input("n1: "))
n2 = int(input("n2: "))

# Algoritmo a ritroso partendo dal minimo
for d in range(min(n1, n2), 0, -1):
    if n1 % d == 0 and n2 % d == 0:
        print(d)
        break
```

---

## 9. Disegno del Solo Contorno di un Quadrato con `*`
**Traccia:** Dato il lato $n$, disegna a schermo il contorno di un quadrato con `*`. Se $n < 3$ disegna il quadrato pieno.  
*Esempio per $n=5$:*
```
*****
*   *
*   *
*   *
*****
```
```python
n = int(input("Lato: "))

if n <= 0:
    pass
elif n < 3:
    for i in range(n):
        print("*" * n)
else:
    print("*" * n)  # Prima riga
    for i in range(n - 2):
        print("*" + " " * (n - 2) + "*")
    print("*" * n)  # Ultima riga
```

---

## 10. Contorno del Quadrato e Diagonale Principale
**Traccia:** Dato il lato $n$, disegna il contorno e la diagonale che va dallo spigolo in alto a sinistra a quello in basso a destra con `*`.  
*Esempio per $n=5$:*
```
*****
**  *
* * *
*  **
*****
```
```python
n = int(input("Lato: "))

if n <= 0:
    pass
elif n < 3:
    for i in range(n):
        print("*" * n)
else:
    for i in range(n):
        for j in range(n):
            # Condizioni: prima o ultima riga, prima o ultima colonna, o diagonale (i == j)
            if i == 0 or i == n - 1 or j == 0 or j == n - 1 or i == j:
                print("*", end='')
            else:
                print(" ", end='')
        print()
```
