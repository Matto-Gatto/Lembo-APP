# Esercizi Risolti — Stringhe

Raccolta completa degli esercizi proposti nel notebook sulle Stringhe.

---

## Esercizio 1: Ricerca e Sostituzione di un Carattere
**Testo:** Chiedere all'utente una stringa `s` e un carattere `x`, e stampare:
1. La posizione della prima occorrenza di `x` in `s`
2. Il numero di volte in cui `x` appare in `s`
3. La stringa ottenuta sostituendo `x` in `s` con `'!!!'`

```python
s = input("Inserisci la stringa s: ")
x = input("Inserisci il carattere x: ")

# 1. Prima occorrenza (-1 se assente)
pos = s.find(x)
print("Posizione prima occorrenza:", pos)

# 2. Conteggio occorrenze
conteggio = s.count(x)
print("Numero di occorrenze:", conteggio)

# 3. Sostituzione con '!!!'
s_modificata = s.replace(x, '!!!')
print("Stringa con sostituzione:", s_modificata)
```

---

## Esercizio 2: Sostituzione di Caratteri e Ricerca di Coppia
**Testo:** Chiedere una stringa `s` e due caratteri `x` e `y`. Stampare:
1. La stringa ottenuta sostituendo `x` con `y` in `s`
2. Il numero di volte in cui la sequenza `xy` appare in `s`

```python
s = input("Inserisci la stringa s: ")
x = input("Inserisci il primo carattere x: ")
y = input("Inserisci il secondo carattere y: ")

print("Stringa con sostituzione x -> y:", s.replace(x, y))
print("Occorrenze della sottostringa '" + x + y + "':", s.count(x + y))
```

---

## Esercizio 3: Sostituzioni Multiple
**Testo:** Chiedere una stringa `s`, un carattere `x` e un'altra stringa `s1`. Stampare:
1. `s` sostituendo `x` con `'!!!'`
2. Il numero di volte in cui `s1` appare in `s`
3. `s` sostituendo `s1` con `x`

```python
s = input("Inserisci la stringa s: ")
x = input("Inserisci il carattere x: ")
s1 = input("Inserisci la stringa s1: ")

print("1. x sostituito con '!!!':", s.replace(x, '!!!'))
print("2. Occorrenze di s1 in s:", s.count(s1))
print("3. s1 sostituito con x:", s.replace(s1, x))
```

---

## Esercizio 4: Campionamento con Passo (Slicing)
**Testo:** Chiedere una stringa `s` e un intero passo `n`. Stampare un carattere ogni `n`.  
*Esempio:* `'linguaggio di programmazione'` con $n=4 \rightarrow$ `'luiiomi'`.

```python
s = input("Inserisci la stringa s: ")
n = int(input("Inserisci il passo n: "))

risultato = s[::n]
print("Risultato:", risultato)
```

---

## Esercizio 5: Stampa di un Quadrato di Caratteri
**Testo:** Prendere in input un carattere e un intero positivo `n` e stampare un quadrato pieno di lato `n`.  
*Esempio con `'*'` e `n=2`:*
```
**
**
```

```python
c = input("Inserisci il carattere: ")
n = int(input("Inserisci la dimensione n: "))

riga = (c * n) + '\n'
quadrato = riga * n
print(quadrato, end='')
```
