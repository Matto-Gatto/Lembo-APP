# Esercitazione Ufficiale n. 7 — 17 Novembre 2025
> **Tipologia:** Funzioni su liste, lunghezze, somme posizionali con padding, matrici/indicizzazioni annidate e prefissi comuni.

---

## Ex1(l): Lista delle Lunghezze
**Traccia:** Riceve una lista $l$ di stringhe e restituisce una lista con le rispettive lunghezze nello stesso ordine.  
*Esempio:* `['tanto', 'va', 'la', 'gatta', 'al', 'lardo']` $\rightarrow [5, 2, 2, 5, 2, 5]$.
```python
def Ex1(l):
    ris = []
    for s in l:
        ris.append(len(s))
    return ris
```

---

## Ex2(l): Massima Lunghezza in Lista
**Traccia:** Riceve una lista $l$ di stringhe e restituisce la lunghezza massima di una stringa contenuta in $l$.  
*Esempio:* `['tanto', 'va', 'la', 'gatta', 'al', 'lardo']` $\rightarrow 5$.
```python
def Ex2(l):
    if len(l) == 0:
        return 0
    max_len = len(l[0])
    for s in l:
        if len(s) > max_len:
            max_len = len(s)
    return max_len
```

---

## Ex3(l1, l2): Somma Posizionale con Padding a Zero
**Traccia:** Riceve due liste di interi con $len(l_2) \ge len(l_1)$. Restituisce una lista con la somma degli elementi alla stessa posizione. Gli elementi mancanti di $l_1$ valgono 0. Se entrambe vuote restituisce `[]`.  
*Esempio:* $l_1 = [3, 6], l_2 = [3, 4, 9] \rightarrow [6, 10, 9]$.
```python
def Ex3(l1, l2):
    ris = []
    for i in range(len(l2)):
        v1 = l1[i] if i < len(l1) else 0
        ris.append(v1 + l2[i])
    return ris
```

---

## Ex4(start, n): Generazione Primi $n$ Numeri $\ge start$
**Traccia:** Dati un intero `start` e un intero non negativo $n$, restituisce la lista dei primi $n$ numeri $\ge start$. Se $n=0 \rightarrow []$.  
*Esempio:* $start=4, n=3 \rightarrow [4, 5, 6]$.
```python
def Ex4(start, n):
    ris = []
    for i in range(n):
        ris.append(start + i)
    return ris
```

---

## Ex5(l, n): Estrazione $n$-esimo Carattere con Fallback `'!'`
**Traccia:** Data una lista di stringhe $l$ e un indice $n \ge 0$, restituisce una stringa formata dai caratteri di indice $n$ di ciascuna stringa. Se una stringa ha lunghezza $\le n$, inserisce `'!'`. Se lista vuota restituisce `""`.  
*Esempio:* $l = \text{['tanto', 'va', 'la', 'gatta', 'al', 'lardo']}$, $n = 3 \rightarrow$ `'t!!t!d'`.
```python
def Ex5(l, n):
    ris = ""
    for s in l:
        if n < len(s):
            ris += s[n]
        else:
            ris += "!"
    return ris
```

---

## Ex6(l): Stringa Parità `'P'` o `'D'`
**Traccia:** Riceve una lista di interi e restituisce una stringa con `'P'` se l'elemento è pari e `'D'` se è dispari. Se vuota restituisce `""`.  
*Esempio:* $[3, 7, 8, 9] \rightarrow$ `'DDPD'`.
```python
def Ex6(l):
    ris = ""
    for num in l:
        if num % 2 == 0:
            ris += "P"
        else:
            ris += "D"
    return ris
```

---

## Ex7(l): Somma Codici Unicode delle Stringhe in Lista
**Traccia:** Data una lista di stringhe, restituisce la lista di interi in cui ogni elemento è la somma dei codici Unicode della stringa corrispondente. Se vuota restituisce `[]`.  
*Esempio:* `['ama', 'ma', 'amaca']` $\rightarrow [303, 206, 499]$.
```python
def Ex7(l):
    ris = []
    for s in l:
        somma_unicode = 0
        for c in s:
            somma_unicode += ord(c)
        ris.append(somma_unicode)
    return ris
```

---

## Ex8(l1, l2): Differenza Insiemistica Ordinata Preservando Duplicati
**Traccia:** Restituisce una lista con gli elementi di $l_1$ che **non** compaiono in $l_2$, ordinati in modo crescente. Le eventuali ripetizioni in $l_1$ vanno mantenute se l'elemento non è in $l_2$, o eliminate tutte se è in $l_2$.  
*Esempio:* $l_1 = [1, 3, 7, 2, 1, -5, 7], l_2 = [1, 3] \rightarrow [-5, 2, 7, 7]$.
```python
def Ex8(l1, l2):
    ris = []
    for x in l1:
        if x not in l2:
            ris.append(x)
    ris.sort()
    return ris
```

---

## Ex9(s): Lettere Maiuscole Senza Ripetizioni in Ordine Crescente
**Traccia:** Data una stringa $s$, restituisce una lista con tutte e sole le lettere maiuscole senza ripetizioni, ordinate alfabeticamente. Se nessuna maiuscola o vuota restituisce `[]`.  
*Esempio:* `'cIAo MAmMa'` $\rightarrow ['A', 'I', 'M']$.
```python
def Ex9(s):
    maiuscole = set()
    for c in s:
        if c.isupper():
            maiuscole.add(c)
    ris = list(maiuscole)
    ris.sort()
    return ris
```

---

## Ex10(s1, s2): Prefisso Più Lungo Comune (*Longest Common Prefix*)
**Traccia:** Date due stringhe $s_1$ ed $s_2$, restituisce il loro prefisso comune più lungo. Se una delle due è vuota o non hanno prefisso comune, restituisce `""`.  
*Esempi:* `'amaca'`, `'amaranto'` $\rightarrow$ `'ama'`; `'amaca'`, `'stringa'` $\rightarrow$ `""`.
```python
def Ex10(s1, s2):
    prefisso = ""
    limite = min(len(s1), len(s2))
    for i in range(limite):
        if s1[i] == s2[i]:
            prefisso += s1[i]
        else:
            break
    return prefisso
```
