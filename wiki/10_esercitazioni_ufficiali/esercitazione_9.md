# Esercitazione Ufficiale n. 9 — 1 Dicembre 2025
> **Tipologia:** Funzioni su file di testo, dizionari di frequenze e parole, e verifica matriciale (Quadrato Latino).

---

## Ex1(fileName): Conteggio Caratteri Alfabetici in un File
**Traccia:** Riceve una stringa `fileName` e restituisce il numero totale di caratteri alfabetici (`c.isalpha()`) contenuti nel file.
```python
def Ex1(fileName):
    conteggio = 0
    with open(fileName, "r", encoding="UTF-8") as f:
        for riga in f:
            for c in riga:
                if c.isalpha():
                    conteggio += 1
    return conteggio
```

---

## Ex2(l): Dizionario delle Frequenze delle Stringhe
**Traccia:** Riceve una lista di stringhe $l$ e restituisce il dizionario che mappa ogni stringa nel numero di volte in cui compare in $l$. Se vuota restituisce `{}`.  
*Esempio:* `['casa','orso','cane','casa','orso','casa']` $\rightarrow$ `{'casa': 3, 'orso': 2, 'cane': 1}`.
```python
def Ex2(l):
    d = {}
    for s in l:
        d[s] = d.get(s, 0) + 1
    return d
```

---

## Ex3(s, n): Iniziali di Parole Lunghe Almeno $n$
**Traccia:** Riceve una stringa $s$ di lettere minuscole e spazi, e un intero $n$. Restituisce un dizionario avente come chiavi le lettere minuscole e come valori il numero di parole in $s$ che iniziano per quella lettera e hanno lunghezza $\ge n$. Non deve contenere chiavi con conteggio 0.  
*Esempio:* $s = \text{'tanto va la gatta al lardo che ci lascia lo zampino'}, n = 3 \rightarrow$ `{'t': 1, 'g': 1, 'c': 1, 'l': 2, 'z': 1}`.
```python
def Ex3(s, n):
    d = {}
    parole = s.split()
    for p in parole:
        if len(p) >= n:
            iniziale = p[0]
            d[iniziale] = d.get(iniziale, 0) + 1
    return d
```

---

## Ex4(n): Dizionario dei Quadrati da $0$ a $n$
**Traccia:** Dato un intero $n \ge 0$, restituisce un dizionario con chiavi i numeri da $0$ ad $n$ (inclusi) e per valori i loro quadrati.  
*Esempio:* $n = 3 \rightarrow \{0: 0, 1: 1, 2: 4, 3: 9\}$.
```python
def Ex4(n):
    d = {}
    for i in range(n + 1):
        d[i] = i ** 2
    return d
```

---

## Ex5(file): Dizionario Lunghezza Righe (Caratteri per Riga)
**Traccia:** Restituisce un dizionario che associa al numero di riga (a partire da 1) il numero totale di caratteri in quella riga (incluso l'eventuale `\n`).
```python
def Ex5(file):
    d = {}
    with open(file, "r", encoding="UTF-8") as f:
        numero_riga = 1
        for riga in f:
            d[numero_riga] = len(riga)
            numero_riga += 1
    return d
```

---

## Ex6(file): Massima Lunghezza di Parola per Riga
**Traccia:** Restituisce un dizionario con chiave il numero di riga (da 1) e valore la massima lunghezza di una parola in quella riga (usando `split()`). Se la riga non contiene parole, la lunghezza è 0.
```python
def Ex6(file):
    d = {}
    with open(file, "r", encoding="UTF-8") as f:
        numero_riga = 1
        for riga in f:
            parole = riga.split()
            max_len = max([len(p) for p in parole]) if len(parole) > 0 else 0
            d[numero_riga] = max_len
            numero_riga += 1
    return d
```

---

## Ex7(file): Carattere Minimo per Riga (Esclusi Spazi e `\n`)
**Traccia:** Restituisce un dizionario con chiave il numero di riga (da 1) e valore il carattere alfabeticamente minimo (codice Unicode più basso) presente nella riga, diverso da `' '` e da `'\n'`.
```python
def Ex7(file):
    d = {}
    with open(file, "r", encoding="UTF-8") as f:
        numero_riga = 1
        for riga in f:
            caratteri_validi = [c for c in riga if c not in (' ', '\n')]
            if len(caratteri_validi) > 0:
                d[numero_riga] = min(caratteri_validi)
            numero_riga += 1
    return d
```

---

## Ex8(file): Sequenze di Due Parole Consecutive con Stessa Iniziale e Finale
**Traccia:** Calcola quante sono le sequenze di due parole consecutive nel testo (anche a cavallo di righe) che soddisfano:
1. Entrambe lunghe almeno 2 caratteri ($\ge 2$).
2. Hanno la stessa lettera iniziale (case-insensitive: $p_1[0].lower() == p_2[0].lower()$).
3. Hanno la stessa lettera finale ($p_1[-1].lower() == p_2[-1].lower()$).  
*Esempio:* `'tanto va Aldino annaspando che resta indietro'` $\rightarrow 1$ (`'Aldino annaspando'`: entrambe iniziano per `'a'` e finiscono per `'o'`).
```python
def Ex8(file):
    with open(file, "r", encoding="UTF-8") as f:
        testo = f.read()
    parole = testo.split()
    conteggio = 0
    for i in range(len(parole) - 1):
        p1 = parole[i].lower()
        p2 = parole[i + 1].lower()
        if len(p1) >= 2 and len(p2) >= 2:
            if p1[0] == p2[0] and p1[-1] == p2[-1]:
                conteggio += 1
    return conteggio
```

---

## Ex9(file): Verifica Quadrato Latino
**Traccia:** Un quadrato latino di ordine $N$ è una scacchiera $N \times N$ con $N$ simboli distinti tale che ogni simbolo compaia **una e una sola volta in ogni riga ed in ogni colonna**.  
Riceve il nome del file contenente le righe di caratteri e restituisce `True` se è un quadrato latino valido, `False` altrimenti.
```python
def Ex9(file):
    with open(file, "r", encoding="UTF-8") as f:
        righe = [r.strip() for r in f.readlines() if len(r.strip()) > 0]
        
    if len(righe) == 0:
        return False
        
    n = len(righe)
    # 1. Verifica che ogni riga abbia lunghezza n
    for r in righe:
        if len(r) != n:
            return False
            
    # L'alfabeto di simboli ammessi è quello della prima riga (deve avere n simboli distinti)
    simboli = set(righe[0])
    if len(simboli) != n:
        return False
        
    # 2. Verifica che ogni riga contenga tutti gli n simboli distinti
    for r in righe:
        if set(r) != simboli:
            return False
            
    # 3. Verifica che ogni colonna contenga tutti gli n simboli distinti
    for col in range(n):
        colonna = [righe[row][col] for row in range(n)]
        if set(colonna) != simboli:
            return False
            
    return True
```
