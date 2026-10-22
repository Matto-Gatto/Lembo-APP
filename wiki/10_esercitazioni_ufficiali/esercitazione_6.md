# Esercitazione Ufficiale n. 6 — 10 Novembre 2025
> **Tipologia:** Funzioni Python con `return` e suite di test (struttura identica alla prova pratica d'esame!).

---

## Ex1(s, c): Conteggio Caratteri che Seguono $c$ in Unicode
**Traccia:** Restituisce il numero di caratteri in $s$ che seguono $c$ nell'ordinamento Unicode ($ord(car) > ord(c)$).  
*Esempio:* `s='AzzuRRO'`, `c='a'` $\rightarrow$ `3` (`'z'`, `'z'`, `'u'` seguono `'a'`; `'A'`, `'R'`, `'O'` la precedono).
```python
def Ex1(s, c):
    conteggio = 0
    for car in s:
        if ord(car) > ord(c):
            conteggio += 1
    return conteggio
```

---

## Ex2(s, c): Stringa dei Caratteri che Seguono $c$ in Unicode
**Traccia:** Restituisce la stringa di caratteri in $s$ che seguono $c$ in Unicode.  
*Esempio:* `s='AzzuRRO'`, `c='a'` $\rightarrow$ `'zzu'`.
```python
def Ex2(s, c):
    ris = ""
    for car in s:
        if ord(car) > ord(c):
            ris += car
    return ris
```

---

## Ex3(n, m): Somma Interi nell'Intervallo $[n, m]$
**Traccia:** Somma di tutti gli interi tra $n$ ed $m$ inclusi. Se $n == m \rightarrow n$; se $n > m \rightarrow 0$.  
*Esempi:* $n=3, m=11 \rightarrow 63$; $n=3, m=-2 \rightarrow 0$.
```python
def Ex3(n, m):
    if n > m:
        return 0
    somma = 0
    for i in range(n, m + 1):
        somma += i
    return somma
```

---

## Ex4(s1, s2): Caratteri Esclusivi senza Ripetizioni
**Traccia:** Restituisce una stringa con tutti i caratteri in $s_1$ che non sono in $s_2$, seguiti da tutti quelli in $s_2$ che non sono in $s_1$, senza ripetizioni e nello stesso ordine originale.  
*Esempio:* `s1='pippo'`, `s2='zorro'` $\rightarrow$ `'pizr'`.
```python
def Ex4(s1, s2):
    ris = ""
    for c in s1:
        if c not in s2 and c not in ris:
            ris += c
    for c in s2:
        if c not in s1 and c not in ris:
            ris += c
    return ris
```

---

## Ex5(s): Indice Uguale alla Cifra Corrispondente
**Traccia:** Data una stringa di cifre (lunghezza $\le 10$), restituisce `True` se esiste almeno un indice $i$ tale che $s[i] == str(i)$. Se vuota restituisce `False`.  
*Esempi:* `'999379'` $\rightarrow$ `True` ($s[3] == '3'$); `'234567890'` $\rightarrow$ `False`.
```python
def Ex5(s):
    for i in range(len(s)):
        if s[i] == str(i):
            return True
    return False
```

---

## Ex6(s, n): Caratteri con Codice Divisibile per $n$ (Senza Doppioni)
**Traccia:** Data una stringa $s$ e un intero $n > 0$, restituisce una stringa con i caratteri di $s$ il cui codice Unicode è divisibile per $n$, presi una sola volta e in ordine da sinistra a destra.  
*Esempio:* `s='stringa di prova'`, $n=3 \rightarrow$ `'rio'`.
```python
def Ex6(s, n):
    ris = ""
    for c in s:
        if ord(c) % n == 0 and c not in ris:
            ris += c
    return ris
```

---

## Ex7(s): Massima Frequenza tra le Lettere Maiuscole
**Traccia:** Restituisce la frequenza (intero) del carattere alfabetico maiuscolo più frequente in $s$. Se non ci sono maiuscole restituisce `0`.  
*Esempi:* `'aHa^^&^HH'` $\rightarrow 3$ (perché `'H'` appare 3 volte); `'CIAO'` $\rightarrow 1$.
```python
def Ex7(s):
    max_f = 0
    for c in s:
        if c.isupper():
            f = s.count(c)
            if f > max_f:
                max_f = f
    return max_f
```

---

## Ex8(s): Stringa dei Caratteri Più Frequenti
**Traccia:** Restituisce una nuova stringa con tutti i caratteri che hanno la massima frequenza in $s$, senza ripetizioni e nell'ordine di prima apparizione. Se $s$ è vuota restituisce `""`.  
*Esempio:* `s='caso palese'` $\rightarrow$ `'ase'` (frequenza massima è 2).
```python
def Ex8(s):
    if len(s) == 0:
        return ""
    
    # 1. Troviamo la massima frequenza
    max_f = max(s.count(c) for c in s)
    
    # 2. Raccogliamo i caratteri con tale frequenza senza duplicati
    ris = ""
    for c in s:
        if s.count(c) == max_f and c not in ris:
            ris += c
    return ris
```

---

## Ex9(s1, s2): Caratteri con Stessa Frequenza ($> 0$) in Due Stringhe
**Traccia:** Restituisce il numero di caratteri distinti che compaiono con lo stesso conteggio ($> 0$) sia in $s_1$ che in $s_2$. Se una delle due è vuota restituisce 0.  
*Esempio:* `s1='caso palese'`, `s2='casa blue'` $\rightarrow$ `3` (i caratteri `'c'`, `'a'`, `' '` e `'l'` compaiono lo stesso numero di volte).
```python
def Ex9(s1, s2):
    if len(s1) == 0 or len(s2) == 0:
        return 0
    
    esaminati = set()
    conteggio = 0
    for c in s1:
        if c not in esaminati:
            esaminati.add(c)
            c1 = s1.count(c)
            c2 = s2.count(c)
            if c1 > 0 and c1 == c2:
                conteggio += 1
    return conteggio
```

---

## Ex10(s): Massimo Intero in Stringa con Trattini
**Traccia:** Data una stringa non vuota con numeri separati da `'-'` (es. `'12-123-45-6-78'`), restituisce il massimo valore numerico come intero (`int`).  
*Esempio:* `'12-123-45-6-78'` $\rightarrow 123$.
```python
def Ex10(s):
    numeri_str = s.split("-")
    massimo = int(numeri_str[0])
    for num in numeri_str:
        val = int(num)
        if val > massimo:
            massimo = val
    return massimo
```

---

## Ex11(b1, b2): AND Bit a Bit tra Stringhe di Lunghezza Qualsiasi
**Traccia:** Date due stringhe di bit `'0'` e `'1'`, calcola l'AND bit a bit da sinistra a destra. Se una stringa è più corta dell'altra, i bit mancanti sono considerati `'0'` (quindi l'AND produrrà `'0'`).  
*Esempi:* `'100'`, `'1011'` $\rightarrow$ `'1000'`; `''`, `'111'` $\rightarrow$ `'000'`; `''`, `''` $\rightarrow$ `''`.
```python
def Ex11(b1, b2):
    max_len = max(len(b1), len(b2))
    ris = ""
    for i in range(max_len):
        bit1 = b1[i] if i < len(b1) else '0'
        bit2 = b2[i] if i < len(b2) else '0'
        if bit1 == '1' and bit2 == '1':
            ris += '1'
        else:
            ris += '0'
    return ris
```
