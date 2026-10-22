# Esercitazione Ufficiale n. 1 — 6 Ottobre 2025
> **Argomenti:** Familiarizzazione con Python, Spyder, I/O di base, espressioni numeriche e stringhe.  
> **Regola generale:** Input coerente con la traccia (assumere tipi validi).

---

## Esercizio 1: Quadrato di un Intero
**Traccia:** Chiede all’utente un intero e ne stampa il quadrato (es. $9 \rightarrow 81$).
```python
n = int(input("Inserisci un intero: "))
print(n ** 2)
```

---

## Esercizio 2: Somma di Due Interi
**Traccia:** Chiede due interi e ne stampa la somma (es. $3, 2 \rightarrow 5$).
```python
a = int(input("Inserisci il primo intero: "))
b = int(input("Inserisci il secondo intero: "))
print(a + b)
```

---

## Esercizio 3: Divisione Reale Primo / Secondo
**Traccia:** Chiede due interi e stampa il risultato del primo diviso il secondo (es. $18, 3 \rightarrow 6.0$).
```python
a = int(input("Inserisci il primo intero: "))
b = int(input("Inserisci il secondo intero: "))
print(a / b)
```

---

## Esercizio 4: Divisione Reale Secondo / Primo
**Traccia:** Chiede due interi e stampa il risultato del secondo diviso il primo (es. $18, 3 \rightarrow 0.16666666666$).
```python
a = int(input("Inserisci il primo intero: "))
b = int(input("Inserisci il secondo intero: "))
print(b / a)
```

---

## Esercizio 5: Concatenazione Stringhe con Spazio
**Traccia:** Chiede due stringhe e stampa la loro concatenazione separata da uno spazio (es. `'casa'`, `'bella'` $\rightarrow$ `'casa bella'`).
```python
s1 = input("Inserisci prima stringa: ")
s2 = input("Inserisci seconda stringa: ")
print(s1 + " " + s2)
```

---

## Esercizio 6: Massimo, Minimo e Media di Tre Interi
**Traccia:** Chiede tre interi e stampa su 3 righe differenti il valore massimo, minimo e la media aritmetica (float).
*Esempio con $10, -2, 1$:*
```
10
-2
3.0
```
```python
a = int(input("Primo intero: "))
b = int(input("Secondo intero: "))
c = int(input("Terzo intero: "))

print(max(a, b, c))
print(min(a, b, c))
print((a + b + c) / 3)
```

---

## Esercizio 7: Ripetizione di una Stringa $n$ Volte
**Traccia:** Chiede una stringa $s$ e un intero $n$ e stampa $s$ ripetuta $n$ volte (es. `'casa'`, $3 \rightarrow$ `'casacasacasa'`).
```python
s = input("Inserisci stringa: ")
n = int(input("Inserisci numero ripetizioni: "))
print(s * n)
```

---

## Esercizio 8: Risoluzione Equazione di Secondo Grado ($ax^2 + bx + c = 0$)
**Traccia:** Chiede tre interi $a, b, c$ ($a \ne 0, \Delta = b^2 - 4ac \ge 0$) e stampa le due soluzioni reali su due righe differenti. Se coincidenti, stampa la stessa soluzione due volte.  
*Formula:* $x_{1,2} = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}$
```python
import math

a = int(input("Inserisci a (≠ 0): "))
b = int(input("Inserisci b: "))
c = int(input("Inserisci c: "))

delta = b**2 - 4*a*c
radice_delta = math.sqrt(delta)

x1 = (-b - radice_delta) / (2 * a)
x2 = (-b + radice_delta) / (2 * a)

print(x1)
print(x2)
```

---

## Esercizio 9: Quadrato $3 \times 3$ con un Carattere
**Traccia:** Chiede un carattere (stringa di lunghezza 1) e stampa un quadrato pieno $3 \times 3$ di quel carattere.
```python
c = input("Inserisci carattere: ")
riga = c * 3
print(riga)
print(riga)
print(riga)
```
