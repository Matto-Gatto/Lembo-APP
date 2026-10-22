# Esercitazione Ufficiale n. 3 — 20 Ottobre 2025
> **Argomenti:** Il ciclo `while`, scansioni iterative, sentinelle, stringhe, primalità.

---

## Esercizio 1: Numeri Pari tra 2 ed $n$
**Traccia:** Chiede un intero $n > 2$ e stampa tutti i numeri pari compresi tra 2 ed $n$ (inclusi 2 ed $n$), uno per riga.
```python
n = int(input("Inserisci intero n > 2: "))
i = 2
while i <= n:
    print(i)
    i += 2
```

---

## Esercizio 2: Divisori Interi Positivi
**Traccia:** Chiede un intero $> 0$ e stampa tutti i suoi divisori interi positivi uno per riga.
```python
n = int(input("Inserisci intero positivo: "))
d = 1
while d <= n:
    if n % d == 0:
        print(d)
    d += 1
```

---

## Esercizio 3: Sequenza fino al Multiplo di 5
**Traccia:** Chiede una sequenza di interi uno per uno, terminando quando viene immesso un numero divisibile per 5. Prima di terminare, stampa la **divisione intera** fra l’ultimo numero inserito e 5.
```python
while True:
    n = int(input("Inserisci intero: "))
    if n % 5 == 0:
        print(n // 5)
        break
```

---

## Esercizio 4: Numeri da 0 a 10 Esclusi $x$ ed $y$
**Traccia:** Chiede due interi $x, y \in [0, 10]$ e stampa tutti i numeri da 0 a 10 esclusi $x$ ed $y$, uno per riga.
```python
x = int(input("Inserisci x [0..10]: "))
y = int(input("Inserisci y [0..10]: "))

i = 0
while i <= 10:
    if i != x and i != y:
        print(i)
    i += 1
```

---

## Esercizio 5: Stringhe fino a Stringa Solo Minuscola Alfabetica
**Traccia:** Chiede stringhe iterativamente; per ogni stringa stampa il primo e l'ultimo carattere (`s[0] + s[-1]`). Termina quando la stringa è composta **esclusivamente da caratteri alfabetici minuscoli** (`s.isalpha() and s.islower()`).
```python
while True:
    s = input("Inserisci stringa: ")
    print(s[0] + s[-1])
    if s.isalpha() and s.islower():
        break
```

---

## Esercizio 6: Conteggio Interi Positivi con Sentinella `*`
**Traccia:** Chiede interi iterativamente fino all'inserimento di `'*'`. Stampa quanti interi **positivi ($> 0$)** sono stati inseriti.
```python
conteggio_positivi = 0
valore = input("Inserisci intero (* per finire): ")

while valore != "*":
    num = int(valore)
    if num > 0:
        conteggio_positivi += 1
    valore = input("Inserisci intero (* per finire): ")

print(conteggio_positivi)
```

---

## Esercizio 7: Somma dei Soli Interi Negativi con Sentinella `*`
**Traccia:** Chiede interi fino all'inserimento di `'*'`. Stampa la somma dei soli interi negativi ($< 0$).
```python
somma_negativi = 0
valore = input("Inserisci intero (* per finire): ")

while valore != "*":
    num = int(valore)
    if num < 0:
        somma_negativi += num
    valore = input("Inserisci intero (* per finire): ")

print(somma_negativi)
```

---

## Esercizio 8: Carattere Più Frequente (con Pareggio Risolto da Destra)
**Traccia:** Data una stringa non vuota $s$, stampa il carattere che compare più volte. Se c'è parità, stampare quello che compare **per ultimo** nella stringa (più a destra).  
*Esempio:* `'clarabella'` $\rightarrow$ `'a'` e `'l'` compaiono entrambe 3 volte, ma l'ultima `'a'` è in posizione 9 mentre l'ultima `'l'` è in posizione 8, quindi vince `'a'`.
```python
s = input("Inserisci stringa: ")

# Inizializziamo scandendo dall'ultimo carattere
max_car = s[-1]
max_conteggio = s.count(s[-1])

# Scandiamo a ritroso da destra a sinistra
i = len(s) - 1
while i >= 0:
    c = s[i]
    conteggio = s.count(c)
    # Se troviamo un conteggio strettamente maggiore, aggiorniamo il vincitore
    if conteggio > max_conteggio:
        max_conteggio = conteggio
        max_car = c
    i -= 1

print(max_car)
```

---

## Esercizio 9: Controllo Primalità di un Intero $n$
**Traccia:** Chiede un intero $n$ e stampa `"numero primo"` oppure `"numero non primo"`.
```python
n = int(input("Inserisci intero: "))

if n <= 1:
    print("numero non primo")
else:
    is_primo = True
    d = 2
    while d * d <= n:
        if n % d == 0:
            is_primo = False
            break
        d += 1
    if is_primo:
        print("numero primo")
    else:
        print("numero non primo")
```

---

## Esercizio 10: Primi tra 2 ed $n$
**Traccia:** Chiede un intero $n > 1$ e stampa tutti i numeri primi compresi tra 2 ed $n$ uno per riga.
```python
n = int(input("Inserisci intero n > 1: "))

num = 2
while num <= n:
    # Verifichiamo se num è primo
    primo = True
    d = 2
    while d * d <= num:
        if num % d == 0:
            primo = False
            break
        d += 1
    if primo:
        print(num)
    num += 1
```
