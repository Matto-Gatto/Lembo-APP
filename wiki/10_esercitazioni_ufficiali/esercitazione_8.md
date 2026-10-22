# Esercitazione Ufficiale n. 8 — 24 Novembre 2025
> **Tipologia:** Funzioni avanzate su insiemi (`set`), tuple, join relazionali, combinazioni e frequenze.

---

## Ex1(l): Caratteri con Almeno Due Occorrenze in una Singola Stringa
**Traccia:** Riceve una lista $l$ di stringhe e restituisce un insieme (`set`) contenente tutti e soli i caratteri che compaiono **almeno due volte all'interno di una stessa stringa** della lista.  
*Esempio:* `['casa', 'albero', 'bello']` $\rightarrow \{'a', 'l'\}$.
```python
def Ex1(l):
    ris = set()
    for s in l:
        for c in s:
            if s.count(c) >= 2:
                ris.add(c)
    return ris
```

---

## Ex2(l, c, n): Filtro Stringhe per Soglia di Occorrenze di $c$
**Traccia:** Restituisce una lista con tutte le stringhe di $l$ escluse quelle che contengono almeno $n$ volte il carattere $c$.  
*Esempio:* $l = \text{['palla', 'casse', 'palo']}$, $c = 'l'$, $n = 2 \rightarrow$ `['casse', 'palo']`.
```python
def Ex2(l, c, n):
    ris = []
    for s in l:
        if s.count(c) < n:
            ris.append(s)
    return ris
```

---

## Ex3(l): Espansione Dinamica per Differenze Successive
**Traccia:** Data una lista di interi positivi, ogni volta che un elemento $l[i] < l[i+1]$, si aggiunge in fondo alla lista la differenza $l[i+1] - l[i]$. Il controllo deve proseguire anche sui **nuovi elementi aggiunti**!  
*Esempio:* $[10, 1, 11, 31, 251] \rightarrow [10, 1, 11, 31, 251, 10, 20, 220, 10, 200, 190]$.
```python
def Ex3(l):
    if len(l) == 0:
        return []
    
    ris = l.copy()
    i = 0
    # Usiamo un ciclo while poiché la lunghezza di ris aumenta dinamicamente
    while i < len(ris) - 1:
        if ris[i] < ris[i + 1]:
            diff = ris[i + 1] - ris[i]
            ris.append(diff)
        i += 1
    return ris
```

---

## Ex4(i): Insieme di Interi Divisibili per 5 Ordinati in Lista
**Traccia:** Riceve un insieme $i$ di interi e restituisce la lista dei soli elementi divisibili per 5, ordinata in modo crescente.  
*Esempio:* $\{3, 345, 15, 24, 25, -10\} \rightarrow [-10, 15, 25, 345]$.
```python
def Ex4(i):
    filtrati = [x for x in i if x % 5 == 0]
    filtrati.sort()
    return filtrati
```

---

## Ex5(l): Insieme di Coppie `(stringa, conteggio)`
**Traccia:** Riceve una lista $l$ di stringhe e restituisce un insieme di tuple `(x, n)` dove $x$ è la stringa ed $n$ è il numero di volte in cui $x$ compare in $l$.  
*Esempio:* `['jkl', 'h', 'plqa', 'jkl', 'h', 'xkj']` $\rightarrow \{('jkl', 2), ('h', 2), ('plqa', 1), ('xkj', 1)\}$.
```python
def Ex5(l):
    ris = set()
    for s in l:
        coppia = (s, l.count(s))
        ris.add(coppia)
    return ris
```

---

## Ex6(l): Tutte le Coppie Distinte di Stringhe di Pari Lunghezza
**Traccia:** Restituisce un insieme di coppie `(x1, x2)` tali che $x_1 \ne x_2$ e $len(x_1) == len(x_2)$.  
*Esempio:* `['jkl', 'h', 'plqa', 'a', 'xkj']` $\rightarrow \{('jkl', 'xkj'), ('xkj', 'jkl'), ('h', 'a'), ('a', 'h')\}$.
```python
def Ex6(l):
    ris = set()
    for i in range(len(l)):
        for j in range(len(l)):
            if i != j and len(l[i]) == len(l[j]):
                ris.add((l[i], l[j]))
    return ris
```

---

## Ex7(a, b): Join Relazionale Insiemi di Coppie (`persona -> città -> regione`)
**Traccia:** Dati due insiemi di coppie:
- $a = \{(\text{nome}, \text{città})\}$
- $b = \{(\text{città}, \text{regione})\}$
Restituisce l'insieme $\{(\text{nome}, \text{regione})\}$. Se la città non è in $b$, la persona non viene inclusa.  
*Esempio:*
$a = \{('Giovanni', 'Napoli'), ('Marco', 'Roma'), ('Aldo', 'Torino')\}$  
$b = \{('Napoli', 'Campania'), ('Roma', 'Lazio'), ('Genova', 'Liguria')\}$  
Risultato: $\{('Giovanni', 'Campania'), ('Marco', 'Lazio')\}$ (nessuna voce per Aldo perché Torino manca in $b$).
```python
def Ex7(a, b):
    # Creiamo un dizionario di appoggio per lookup istantaneo O(1) di b
    citta_regione = dict(b)
    ris = set()
    for nome, citta in a:
        if citta in citta_regione:
            ris.add((nome, citta_regione[citta]))
    return ris
```

---

## Ex8(l): Insieme dei Caratteri Più Frequenti di Ciascuna Stringa
**Traccia:** Per ciascuna stringa in $l$, estrae il carattere più frequente; in caso di parità, prende il più piccolo in ordine alfabetico Unicode. Restituisce l'insieme (`set`) di tali caratteri. Se vuota restituisce `set()`.  
*Esempio:* `['amaca', 'amaranto', 'rosso']` $\rightarrow \{'a', 'o'\}$.
```python
def Ex8(l):
    ris = set()
    for s in l:
        if len(s) == 0:
            continue
        max_f = max(s.count(c) for c in s)
        candidati = [c for c in s if s.count(c) == max_f]
        candidati.sort()
        ris.add(candidati[0])
    return ris
```

---

## Ex9(l): Lettera Minuscola che Compare in Più Stringhe
**Traccia:** Data una lista non vuota di stringhe, calcola quale lettera minuscola (`'a'-'z'`) compare in più stringhe distinte. Se c'è parità, restituisce quella alfabeticamente più grande (più avanti nell'alfabeto).  
*Esempio:* `['casa', 'senape', 'ketchup', 'pasta']` $\rightarrow$ `'s'`, `'a'`, `'p'` compaiono ciascuna in 3 stringhe distinte; vince `'s'` perché più grande.
```python
def Ex9(l):
    alfabeto = 'abcdefghijklmnopqrstuvwxyz'
    migliore_lettera = 'a'
    max_stringhe = -1
    
    for lettera in alfabeto:
        conteggio = 0
        for s in l:
            if lettera in s:
                conteggio += 1
        # Usiamo >= per prediligere a parità di conteggio la lettera successiva
        if conteggio >= max_stringhe and conteggio > 0:
            max_stringhe = conteggio
            migliore_lettera = lettera
            
    return migliore_lettera
```

---

## Ex10(l): Elementi Esclusivi (Presenti in Uno e Solo Uno degli Insiemi)
**Traccia:** Riceve una lista $l$ di insiemi di interi. Restituisce un insieme con tutti e soli gli elementi che appartengono a **uno e un solo insieme** della lista.  
*Esempio:* $l = [\{3, 2, 90\}, \{2, 87, 23\}, \{2, 23, 3\}] \rightarrow \{90, 87\}$ (il 3, il 2 e il 23 compaiono in più insiemi).
```python
def Ex10(l):
    if len(l) == 0:
        return set()
    
    # 1. Contiamo in quanti insiemi compare ciascun elemento
    frequenza_insiemi = {}
    for insieme in l:
        for elem in insieme:
            frequenza_insiemi[elem] = frequenza_insiemi.get(elem, 0) + 1
            
    # 2. Selezioniamo solo quelli con frequenza esattamente pari a 1
    ris = set()
    for elem, freq in frequenza_insiemi.items():
        if freq == 1:
            ris.add(elem)
            
    return ris
```
