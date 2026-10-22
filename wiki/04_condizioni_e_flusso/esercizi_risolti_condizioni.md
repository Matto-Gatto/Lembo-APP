# Esercizi Risolti — Condizioni e Flusso di Controllo

Raccolta completa degli esercizi delle dispense ufficiali con spiegazione e casi di test.

---

## Esercizio Guida: Selezione Sottostringa tra la 1ª e la 2ª Occorrenza
**Testo:** Legge una stringa `s` e un carattere `c`. Se `c` compare almeno 2 volte in `s`, stampa la parte di stringa dalla prima alla seconda occorrenza di `c` (incluse). Altrimenti stampa: `"Il carattere c compare meno di due volte nella stringa s"`.

```python
s = input("Inserisci la stringa: ")
c = input("Inserisci il carattere: ")

if s.count(c) >= 2:
    prima_occ = s.find(c)
    # Cerca la seconda occorrenza a partire dall'indice successivo alla prima
    seconda_occ = s.find(c, prima_occ + 1)
    # Slicing con estremo destro + 1 per includere il carattere
    print(s[prima_occ : seconda_occ + 1])
else:
    print("Il carattere", c, "compare meno di due volte nella stringa", s)
```

---

## Esercizio 1: Ordinamento Alfabetico e per Lunghezza
**Testo:** Riceve in input due stringhe `s1` ed `s2` e stampa:
1. Prima riga: le stringhe in ordine alfabetico
2. Seconda riga: le stringhe in ordine di lunghezza crescente

```python
s1 = input("Inserisci prima stringa: ")
s2 = input("Inserisci seconda stringa: ")

# 1. Ordine alfabetico (lessicografico)
if s1 <= s2:
    print("Ordine alfabetico:", s1, s2)
else:
    print("Ordine alfabetico:", s2, s1)

# 2. Ordine per lunghezza
if len(s1) <= len(s2):
    print("Ordine per lunghezza:", s1, s2)
else:
    print("Ordine per lunghezza:", s2, s1)
```

---

## Esercizio 2: Ricerca e Conteggio Sottostringa
**Testo:** Prende in ingresso due stringhe `s1` ed `s2`. Se `s2` è contenuta in `s1`, calcola quante volte compare e stampa:  
`La stringa s2 compare N volte nella stringa s1`.  
Altrimenti stampa:  
`La stringa s2 non compare nella stringa s1`.

```python
s1 = input("Inserisci s1: ")
s2 = input("Inserisci s2: ")

if s2 in s1:
    n = s1.count(s2)
    print("La stringa", s2, "compare", n, "volte nella stringa", s1)
else:
    print("La stringa", s2, "non compare nella stringa", s1)
```

---

## Esercizio 3: Verifica Stringa Palindroma con Slicing
**Testo:** Prende in ingresso una stringa `s` e stampa `True` se `s` è palindroma (si legge uguale da sinistra a destra e viceversa).

```python
s = input("Inserisci la stringa da verificare: ")
# Slicing con passo -1 per invertire la stringa
is_palindroma = (s == s[::-1])
print("È palindroma?", is_palindroma)
```

---

## Esercizio 4: Il Gioco dell'Indovinello (3 Tentativi)
**Testo:** L'utente inserisce un numero $N$. Il computer "pensa" un numero casuale tra $1$ ed $N$ compresi (usando `random.randint(1, N)`). L'utente ha **3 tentativi** per indovinare; ad ogni tentativo il programma risponde con:
- `"Bravo hai indovinato"`
- `"Il Numero che hai detto è troppo grande"`
- `"Il Numero che hai detto è troppo piccolo"`

*Curiosità teorica:* Qual è il valore massimo di $N$ per cui l'utente può vincere **sempre** con strategia ottima (ricerca binaria)?  
Risposta: con 3 tentativi si possono distinguere al massimo $2^3 - 1 = 7$ numeri diversi ($N = 7$).

```python
from random import randint

n = int(input("Inserisci il valore massimo N: "))
segreto = randint(1, n)
indovinato = False

# Tentativo 1
t1 = int(input("Tentativo 1 - Inserisci numero: "))
if t1 == segreto:
    print("Bravo hai indovinato")
    indovinato = True
elif t1 > segreto:
    print("Il Numero che hai detto è troppo grande")
else:
    print("Il Numero che hai detto è troppo piccolo")

# Tentativo 2 (solo se non ha già indovinato)
if not indovinato:
    t2 = int(input("Tentativo 2 - Inserisci numero: "))
    if t2 == segreto:
        print("Bravo hai indovinato")
        indovinato = True
    elif t2 > segreto:
        print("Il Numero che hai detto è troppo grande")
    else:
        print("Il Numero che hai detto è troppo piccolo")

# Tentativo 3 (solo se non ha già indovinato)
if not indovinato:
    t3 = int(input("Tentativo 3 - Inserisci numero: "))
    if t3 == segreto:
        print("Bravo hai indovinato")
        indovinato = True
    elif t3 > segreto:
        print("Il Numero che hai detto è troppo grande")
    else:
        print("Il Numero che hai detto è troppo piccolo")

if not indovinato:
    print("Tentativi esauriti! Il numero era:", segreto)
```
