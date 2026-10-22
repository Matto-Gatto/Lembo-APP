# Esercitazione Ufficiale n. 2 — 13 Ottobre 2025
> **Argomenti:** Istruzioni condizionali (`if`, `elif`, `else`), operatori relazionali e logici.

---

## Esercizio 1: Conversione Ore, Minuti, Secondi in Secondi Totali
**Traccia:** Chiede ore $hh$, minuti $mm$ e secondi $ss$ e stampa a video l'equivalente in secondi totali.  
*Esempio:* $hh=2, mm=1, ss=11 \rightarrow 2 \times 3600 + 1 \times 60 + 11 = 7271$.
```python
hh = int(input("Ore: "))
mm = int(input("Minuti: "))
ss = int(input("Secondi: "))

totale_secondi = hh * 3600 + mm * 60 + ss
print(totale_secondi)
```

---

## Esercizio 2: Controllo Carattere Iniziale e Finale Uguali
**Traccia:** Chiede una stringa non vuota $s$ e verifica se il primo e l'ultimo carattere sono uguali. Stampa `"caratteri iniziale e finale uguali"` oppure `"caratteri iniziale e finale diversi"`.
```python
s = input("Inserisci stringa non vuota: ")

if s[0] == s[-1]:
    print("caratteri iniziale e finale uguali")
else:
    print("caratteri iniziale e finale diversi")
```

---

## Esercizio 3: Calcolo Anno Bisestile
**Traccia:** Chiede un anno e stampa `"anno bisestile"` o `"anno non bisestile"`.  
*Regola:* Divisibile per 4 ma non per 100, oppure divisibile per 400.
```python
anno = int(input("Inserisci anno: "))

if (anno % 4 == 0 and anno % 100 != 0) or (anno % 400 == 0):
    print("anno bisestile")
else:
    print("anno non bisestile")
```

---

## Esercizio 4: Tipologia di Frazione ($n/d$)
**Traccia:** Chiede numeratore $n$ e denominatore $d$. Stampa se la frazione è:
- `"propria"`: $n < d$
- `"apparente"`: $n$ è multiplo di $d$ ($n \pmod d == 0$)
- `"impropria"`: $n > d$ e non è multiplo di $d$

```python
n = int(input("Numeratore: "))
d = int(input("Denominatore: "))

if n % d == 0:
    print("apparente")
elif n < d:
    print("propria")
else:
    print("impropria")
```

---

## Esercizio 5: Tre Interi in Ordine Decrescente
**Traccia:** Chiede tre numeri interi $n_1, n_2, n_3$ e li stampa in ordine decrescente su 3 righe separate.
```python
n1 = int(input("n1: "))
n2 = int(input("n2: "))
n3 = int(input("n3: "))

# Identifichiamo massimo, minimo e l'elemento centrale
massimo = max(n1, n2, n3)
minimo = min(n1, n2, n3)
mediano = (n1 + n2 + n3) - massimo - minimo

print(massimo)
print(mediano)
print(minimo)
```

---

## Esercizio 6: Classificazione Triangoli
**Traccia:** Chiede tre interi $a, b, c$. Verifica se formano un triangolo valido (tutti positivi e ciascuno strettamente minore della somma degli altri due). In caso affermativo stampa `"equilatero"`, `"isoscele"` o `"scaleno"`, altrimenti `"input non valido"`.
```python
a = int(input("Lato a: "))
b = int(input("Lato b: "))
c = int(input("Lato c: "))

if a > 0 and b > 0 and c > 0 and a < b + c and b < a + c and c < a + b:
    if a == b == c:
        print("equilatero")
    elif a == b or b == c or a == c:
        print("isoscele")
    else:
        print("scaleno")
else:
    print("input non valido")
```

---

## Esercizio 7: Calcolo Mese Successivo
**Traccia:** Chiede mese e anno. Se il mese non è compreso tra 1 e 12 stampa `"input non valido"`. Altrimenti calcola il mese successivo e l'eventuale nuovo anno.  
*Esempi:* $10, 2017 \rightarrow$ `"11 2017"`; $12, 2017 \rightarrow$ `"1 2018"`.
```python
mese = int(input("Mese: "))
anno = int(input("Anno: "))

if 1 <= mese <= 12:
    if mese == 12:
        print("1", anno + 1)
    else:
        print(mese + 1, anno)
else:
    print("input non valido")
```

---

## Esercizio 8: Conversione Età Cane in Età Umana
**Traccia:** Chiede l'età del cane (float $\ge 0$). I primi 2 anni valgono $10.5$ anni umani ciascuno; gli anni successivi valgono $4$ anni uomo ciascuno. Se $< 0$ input non valido.  
*Esempio:* $10.0 \rightarrow 2 \times 10.5 + 8 \times 4 = 21 + 32 = 53.0$.
```python
eta = float(input("Età cane: "))

if eta < 0:
    print("input non valido")
elif eta <= 2:
    print(eta * 10.5)
else:
    anni_umani = 2 * 10.5 + (eta - 2) * 4
    print(anni_umani)
```

---

## Esercizio 9: Classificazione Fascia di Temperatura
**Traccia:** Chiede una temperatura intera $t$ e stampa:
- $t > 30 \rightarrow$ `"molto caldo"`
- $20 < t \le 30 \rightarrow$ `"caldo"`
- $10 < t \le 20 \rightarrow$ `"gradevole"`
- $t \le 10 \rightarrow$ `"freddo"`

```python
t = int(input("Temperatura: "))

if t > 30:
    print("molto caldo")
elif t > 20:
    print("caldo")
elif t > 10:
    print("gradevole")
else:
    print("freddo")
```

---

## Esercizio 10: Stato dell'Acqua con Conversione Scale (Celsius / Fahrenheit)
**Traccia:** Chiede temperatura e scala (`'C'` o `'F'`). Se Fahrenheit, converte con $C = (F - 32) / 1.8$.  
Stampa:
- `"solida"` se $C \le 0$
- `"liquida"` se $0 < C < 100$
- `"gassosa"` se $C \ge 100$

```python
temp = float(input("Temperatura: "))
scala = input("Scala (C o F): ").strip().upper()

if scala == 'F':
    celsius = (temp - 32) / 1.8
else:
    celsius = temp

if celsius <= 0:
    print("solida")
elif celsius < 100:
    print("liquida")
else:
    print("gassosa")
```
