# Esercizi Risolti — Definizione di Funzioni

Raccolta completa dei 6 esercizi finali del notebook "Definizione di Funzioni", completi di casi di test ufficiali e spiegazione.

---

## Esercizio 1: `fattoriale(n)`
**Testo:** Scrivere una funzione che prende in input un numero naturale $n$ e restituisce il suo fattoriale ($n!$). Per convenzione $0! = 1$.

```python
def fattoriale(n):
    if n == 0 or n == 1:
        return 1
    risultato = 1
    for i in range(2, n + 1):
        risultato *= i
    return risultato

# Casi di test:
# tester_fun(fattoriale, [4], 24)
# tester_fun(fattoriale, [5], 120)
# tester_fun(fattoriale, [10], 3628800)
# tester_fun(fattoriale, [0], 1)
```

---

## Esercizio 2: `maxdivisore(n)`
**Testo:** Prende in input un intero positivo $n$ e restituisce il suo massimo divisore diverso da $n$. Se il numero è primo, restituisce $1$.

```python
def maxdivisore(n):
    # Il più grande divisore proprio non può superare n // 2
    for d in range(n // 2, 0, -1):
        if n % d == 0:
            return d
    return 1

# Casi di test:
# tester_fun(maxdivisore, [24], 12)
# tester_fun(maxdivisore, [9], 3)
# tester_fun(maxdivisore, [175], 35)
# tester_fun(maxdivisore, [231], 77)
# tester_fun(maxdivisore, [131], 1)
```

---

## Esercizio 3: `maxfreq(s)`
**Testo:** Prende in input una stringa e restituisce il carattere più frequente. In caso di parità, restituisce il primo incontrato da sinistra. Se la stringa è vuota, restituisce una stringa vuota `""`.

```python
def maxfreq(s):
    if len(s) == 0:
        return ""
    
    miglior_carattere = s[0]
    max_conteggio = s.count(s[0])
    
    for c in s:
        conteggio = s.count(c)
        # Nota: usiamo strettamente > per preservare il primo incontrato in caso di parità
        if conteggio > max_conteggio:
            max_conteggio = conteggio
            miglior_carattere = c
            
    return miglior_carattere

# Casi di test:
# tester_fun(maxfreq, ['palla'], 'a')
# tester_fun(maxfreq, ['pallone'], 'l')
# tester_fun(maxfreq, ['casa bianca di piero e sergio'], ' ')
# tester_fun(maxfreq, ['palla casa pallone'], 'a')
# tester_fun(maxfreq, [''], '')
```

---

## Esercizio 4: `collegaNoRipetizioni(s1, s2)`
**Testo:** Prende in input due stringhe `s1` ed `s2` e restituisce una nuova stringa formata dai caratteri di `s1` seguiti da quelli di `s2`, ma **senza ripetizioni** (mantenendo solo la prima occorrenza di ogni carattere).

```python
def collegaNoRipetizioni(s1, s2):
    unione = s1 + s2
    risultato = ""
    for c in unione:
        if c not in risultato:
            risultato += c
    return risultato

# Casi di test:
# tester_fun(collegaNoRipetizioni, ['casa', 'dolce casa'], 'casdole ')
# tester_fun(collegaNoRipetizioni, ['',''], '')
```

---

## Esercizio 5: `maxlung(s)`
**Testo:** Prende in input una stringa `s` con parole separate da spazi e restituisce la **lunghezza della parola più lunga**. Usare `find()` o scansione per trovare gli spazi. Se stringa vuota restituisce 0.

```python
def maxlung(s):
    if len(s.strip()) == 0:
        return 0
    
    max_len = 0
    inizio = 0
    
    while inizio < len(s):
        # Ignora eventuali spazi consecutivi
        if s[inizio] == ' ':
            inizio += 1
            continue
            
        fine = s.find(' ', inizio)
        if fine == -1:  # Ultima parola fino alla fine
            lunghezza = len(s) - inizio
            if lunghezza > max_len:
                max_len = lunghezza
            break
        else:
            lunghezza = fine - inizio
            if lunghezza > max_len:
                max_len = lunghezza
            inizio = fine + 1
            
    return max_len

# Casi di test:
# tester_fun(maxlung, ['casa dolce casa'], 5)
# tester_fun(maxlung, ['pallina dentro un cassetto bianco'], 8)
# tester_fun(maxlung, ['pallina dentro un cassetto bianco estremamente pieno'], 12)
# tester_fun(maxlung, [''], 0)
```

---

## Esercizio 6: `sostituisci(s, c1, c2, count=None)`
**Testo:** Scrivere una funzione `sostituisci` che simula fedelmente `s.replace(c1, c2, count)`. Se `count` è `None`, sostituisce tutte le occorrenze di `c1` con `c2`.

```python
def sostituisci(s, c1, c2, count=None):
    if c1 == "":
        return s
    
    risultato = ""
    i = 0
    sostituzioni_fatte = 0
    
    while i < len(s):
        # Se troviamo la sottostringa c1 e non abbiamo superato il limite count
        if s[i : i + len(c1)] == c1 and (count is None or sostituzioni_fatte < count):
            risultato += c2
            i += len(c1)
            sostituzioni_fatte += 1
        else:
            risultato += s[i]
            i += 1
            
    return risultato

# Casi di test:
# tester_fun(sostituisci, ['palla', 'a', 'e'], 'pelle')
# tester_fun(sostituisci, ['pallina', 'a', 'o'], 'pollino')
# tester_fun(sostituisci, ['pallina', 'a', 'o', 1], 'pollina')
# tester_fun(sostituisci, ['pallina', 'al', 'er', 1], 'perlina')
# tester_fun(sostituisci, ['palla casa pallone', 'll', 'l', 1], 'pala casa pallone')
```
