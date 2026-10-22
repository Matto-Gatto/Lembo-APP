# Esercitazione Ufficiale n. 4 — 27 Ottobre 2025
> **Argomenti:** Ciclo `while`, variabili accumulatore, condizioni complesse su stringhe, serie di Fibonacci.

---

## Esercizio 1: Stringhe fino alla presenza contemporanea di `'a'` e `'c'`
**Traccia:** Chiede stringhe iterativamente; termina quando viene inserita una stringa che contiene **sia il carattere `'a'` che `'c'`. Stampa il numero totale di stringhe lette (inclusa l’ultima).  
*Esempio:* `'pippo'`, `'albero'`, `'casa'` $\rightarrow$ Stampa `3`.
```python
conteggio = 0
while True:
    s = input("Inserisci stringa: ")
    conteggio += 1
    if ('a' in s) and ('c' in s):
        break

print(conteggio)
```

---

## Esercizio 2: Scansione Stringa e Unicode > 100
**Traccia:** Scandisce la stringa da sinistra a destra. Se incontra un carattere con codice Unicode $> 100$, si ferma e stampa:  
`"Il primo carattere con codice Unicode maggiore di 100 è <carattere>"`.  
Se la stringa finisce senza trovarlo, stampa:  
`"stringa consumata e carattere non trovato"`.
```python
s = input("Inserisci stringa: ")
i = 0
trovato = False

while i < len(s):
    if ord(s[i]) > 100:
        print("Il primo carattere con codice Unicode maggiore di 100 è", s[i])
        trovato = True
        break
    i += 1

if not trovato:
    print("stringa consumata e carattere non trovato")
```

---

## Esercizio 3: Sequenza di Stringhe fino a $c$ Presente Più di 2 Volte
**Traccia:** Chiede all'inizio un carattere $c$, poi stringhe iterativamente finché $c$ compare **più di 2 volte** nella stringa corrente ($> 2$). Prima di terminare stampa il numero di occorrenze di $c$ nell'ultima stringa inserita.
```python
c = input("Inserisci il carattere target c: ")

while True:
    s = input("Inserisci stringa: ")
    occorrenze = s.count(c)
    if occorrenze > 2:
        print(occorrenze)
        break
```

---

## Esercizio 4: Somma dei Soli Interi Divisibili per 3 con Stop a 0
**Traccia:** Chiede numeri interi uno alla volta fino all'inserimento dello zero `0`. Stampa la somma dei soli numeri divisibili per 3 ($n \pmod 3 == 0$).
```python
somma = 0
while True:
    n = int(input("Inserisci intero (0 per terminare): "))
    if n == 0:
        break
    if n % 3 == 0:
        somma += n

print(somma)
```

---

## Esercizio 5: Calcolo Fattoriale $n!$ con Ciclo While
**Traccia:** Chiede un intero $n \ge 0$ e ne calcola il fattoriale ($0! = 1, 1! = 1, n! = n \times (n-1) \times \dots \times 1$).
```python
n = int(input("Inserisci n >= 0: "))

fattoriale = 1
i = 2
while i <= n:
    fattoriale *= i
    i += 1

print(fattoriale)
```

---

## Esercizio 6: Prodotto di Due Interi Senza Usare `*` o `/`
**Traccia:** Chiede due interi $a$ e $b$ (positivi, negativi o zero) e ne calcola il prodotto usando solo somme/sottrazioni ripetute.
```python
a = int(input("Primo intero: "))
b = int(input("Secondo intero: "))

# Determinazione del segno finale
segno_negativo = (a < 0) ^ (b < 0)

abs_a = abs(a)
abs_b = abs(b)

prodotto = 0
i = 0
while i < abs_b:
    prodotto += abs_a
    i += 1

if segno_negativo:
    prodotto = -prodotto

print(prodotto)
```

---

## Esercizio 7: Richiesta Continua fino a Stringa Palindroma
**Traccia:** Chiede una stringa. Finché non è palindroma, stampa `"non palindroma, inserire una stringa palindroma: "` e richiede l'input. Appena è palindroma, termina e stampa `"stringa palindroma di lunghezza <len>"`.
```python
s = input("Inserisci stringa: ")

while s != s[::-1]:
    s = input("non palindroma, inserire una stringa palindroma: ")

print("stringa palindroma di lunghezza", len(s))
```

---

## Esercizio 8: Catena di Parole (Ultimo Carattere = Primo Carattere)
**Traccia:** Legge una sequenza di stringhe non vuote; termina quando l'ultimo carattere della stringa precedente è uguale al primo carattere di quella attuale (`prec[-1] == corr[0]`). Stampa su un'unica riga le ultime due stringhe separate da spazio.  
*Esempio:* `'pippo'`, `'casa'`, `'albero'` $\rightarrow$ `'casa'` finisce per `'a'`, `'albero'` inizia per `'a'` $\rightarrow$ Stampa `"casa albero"`.
```python
prec = input("Inserisci prima stringa: ")

while True:
    corr = input("Inserisci stringa successiva: ")
    if prec[-1] == corr[0]:
        print(prec, corr)
        break
    prec = corr
```

---

## Esercizio 9: Primi $n$ Numeri della Successione di Fibonacci
**Traccia:** Chiede un intero $n > 0$ e stampa uno per riga i primi $n$ numeri di Fibonacci ($F_1 = 1, F_2 = 1, F_3 = 2, F_4 = 3, F_5 = 5, \dots$).
```python
n = int(input("Inserisci n > 0: "))

if n >= 1:
    print(1)
if n >= 2:
    print(1)

a = 1
b = 1
conteggio = 2
while conteggio < n:
    c = a + b
    print(c)
    a = b
    b = c
    conteggio += 1
```

---

## Esercizio 10: Finestra di Tre Stringhe ($len(s_1) + len(s_2) == len(s_3)$)
**Traccia:** Legge una sequenza di stringhe (almeno 3) terminando quando la somma delle lunghezze di due stringhe consecutive è pari alla lunghezza della stringa successiva. Stampa su una sola riga le tre stringhe separate da spazio.  
*Esempio:* `'fondamenti'`, `'uno'`, `'due'`, `'FP1'`, `'darwin'`  
$len(\text{'uno'}) + len(\text{'due'}) = 3 + 3 = 6 \ne len(\text{'FP1'})=3$  
$len(\text{'due'}) + len(\text{'FP1'}) = 3 + 3 = 6 == len(\text{'darwin'})=6$ $\rightarrow$ Termina e stampa `"due FP1 darwin"`.
```python
s1 = input("Stringa 1: ")
s2 = input("Stringa 2: ")

while True:
    s3 = input("Stringa successiva: ")
    if len(s1) + len(s2) == len(s3):
        print(s1, s2, s3)
        break
    s1 = s2
    s2 = s3
```
