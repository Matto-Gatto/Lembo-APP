# Esercizi Risolti — Liste, Tuple e Insiemi

Raccolta completa di tutti i 12 esercizi proposti nei notebook ufficiali su Liste, Memoria, Tuple e Insiemi.

---

## 1. `stringaMax(l)`
**Testo:** Riceve una lista non vuota di stringhe e restituisce la **lunghezza** della stringa più lunga.
```python
def stringaMax(l):
    max_l = len(l[0])
    for s in l:
        if len(s) > max_l:
            max_l = len(s)
    return max_l
```

---

## 2. `ultimoPos(l)`
**Testo:** Riceve una lista di interi e restituisce l'indice dell'**ultimo elemento non negativo ($\ge 0$)**. Se non c'è, restituisce `-1`. Se la lista è vuota, restituisce la stringa `'errore vuota'`.
```python
def ultimoPos(l):
    if len(l) == 0:
        return 'errore vuota'
    for i in range(len(l) - 1, -1, -1):
        if l[i] >= 0:
            return i
    return -1
```

---

## 3. `inserisciStringa(l, s)`
**Testo:** Riceve una lista `l` di stringhe già ordinata per lunghezza crescente e una stringa `s`. Restituisce una nuova lista inserendo `s` nella posizione corretta per preservare l'ordinamento.
```python
def inserisciStringa(l, s):
    ris = l.copy()
    inserito = False
    for i in range(len(ris)):
        if len(s) < len(ris[i]):
            ris.insert(i, s)
            inserito = True
            break
    if not inserito:
        ris.append(s)
    return ris
```

---

## 4. `somma(l)`
**Testo:** Riceve una lista di elementi disomogenei e restituisce la somma di tutti e soli gli elementi di tipo intero (`int`). Se la lista è vuota, restituisce `0`.
```python
def somma(l):
    totale = 0
    for elem in l:
        # type(elem) is int esclude i float e i bool
        if type(elem) is int:
            totale += elem
    return totale
```

---

## 5. `eliminaStringhe(l, i)`
**Testo:** Riceve una lista di stringhe `l` e un intero `i`. Restituisce la lista ottenuta eliminando tutte le stringhe di lunghezza strettamente maggiore di `i`.
```python
def eliminaStringhe(l, i):
    # Costruiamo una nuova lista o usiamo while/copia
    ris = []
    for s in l:
        if len(s) <= i:
            ris.append(s)
    return ris
```

---

## 6. `merge(l1, l2)` (Fusione Ordinata per Lunghezza)
**Testo:** Riceve due liste `l1` e `l2` già ordinate per lunghezza crescente. Restituisce la fusione ordinata. In caso di pari lunghezza, ha precedenza l'elemento di `l2`.
```python
def merge(l1, l2):
    ris = []
    i = 0
    j = 0
    while i < len(l1) and j < len(l2):
        if len(l2[j]) <= len(l1[i]):  # In caso di parità, prima l2
            ris.append(l2[j])
            j += 1
        else:
            ris.append(l1[i])
            i += 1
    # Accoda gli elementi residui
    ris.extend(l1[i:])
    ris.extend(l2[j:])
    return ris
```

---

## 7. `maxfrequenza(l)`
**Testo:** Restituisce l'elemento più frequente nella lista `l`. A parità di frequenza, restituisce quello che compare prima nella lista.
```python
def maxfrequenza(l):
    migliore = l[0]
    max_c = l.count(l[0])
    for elem in l:
        c = l.count(elem)
        if c > max_c:
            max_c = c
            migliore = elem
    return migliore
```

---

## 8. `listaContiene(l, s)`
**Testo:** Restituisce la lista ordinata alfabeticamente degli elementi di `l` che contengono la sottostringa `s`.
```python
def listaContiene(l, s):
    filtrati = [parola for parola in l if s in parola]
    filtrati.sort()
    return filtrati
```

---

## 9. `listaSelezioni(ls, ln)`
**Testo:** Restituisce una nuova lista estraendo da `ls` gli elementi agli indici indicati in `ln`. Gli indici fuori range (sia positivi che negativi) vengono ignorati.
```python
def listaSelezioni(ls, ln):
    ris = []
    lunghezza = len(ls)
    for idx in ln:
        # Un indice idx è valido se -lunghezza <= idx < lunghezza
        if -lunghezza <= idx < lunghezza:
            ris.append(ls[idx])
    return ris
```

---

## 10. `contaIniziali(l1, l2)`
**Testo:** Date due liste di stringhe, conta quante volte le stringhe nella stessa posizione hanno la stessa lettera iniziale.
```python
def contaIniziali(l1, l2):
    limite = min(len(l1), len(l2))
    conteggio = 0
    for i in range(limite):
        if len(l1[i]) > 0 and len(l2[i]) > 0:
            if l1[i][0] == l2[i][0]:
                conteggio += 1
    return conteggio
```

---

## 11. `unisci(l1, l2)`
**Testo:** Date due liste, restituisce una lista di tuple `(l1[i], l2[i])` fino alla lunghezza minima.
```python
def unisci(l1, l2):
    limite = min(len(l1), len(l2))
    ris = []
    for i in range(limite):
        ris.append((l1[i], l2[i]))
    return ris
```

---

## 12. `divisoriComuni(l)`
**Testo:** Riceve una lista di interi positivi e restituisce l'**insieme (`set`)** dei divisori comuni a **tutti** i numeri della lista.
```python
def divisoriComuni(l):
    if len(l) == 0:
        return set()
    
    # Inizializza con i divisori del primo numero
    comuni = set()
    for d in range(1, l[0] + 1):
        if l[0] % d == 0:
            comuni.add(d)
            
    # Calcola l'intersezione con i divisori di ciascun altro numero
    for num in l[1:]:
        div_num = set()
        for d in range(1, num + 1):
            if num % d == 0:
                div_num.add(d)
        comuni &= div_num
        
    return comuni
```
