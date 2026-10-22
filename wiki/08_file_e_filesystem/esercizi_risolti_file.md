# Esercizi Risolti — File di Testo e CSV

Raccolta completa degli esercizi tratti dalle dispense sui File e sui CSV.

---

## 1. `stringaMaxFreq(file, l)`
**Testo:** Riceve il nome di un file di testo e una lista di stringhe `l`. Restituisce la stringa di `l` che compare più volte nel file (senza distinzione tra maiuscole e minuscole). In caso di parità, restituisce la prima in ordine alfabetico.

```python
def stringaMaxFreq(file, l):
    with open(file, "r", encoding="UTF-8") as f:
        testo = f.read().lower()
        
    # Ordiniamo prima alfabeticamente per gestire automaticamente le parità
    l_ordinate = sorted(l)
    
    migliore = l_ordinate[0]
    max_conteggio = -1
    
    for s in l_ordinate:
        conteggio = testo.count(s.lower())
        if conteggio > max_conteggio:
            max_conteggio = conteggio
            migliore = s
            
    return migliore
```

---

## 2. `copiaRigheFiltro(file_in, file_out, l)`
**Testo:** Copia in `file_out` tutte le righe di `file_in` che contengono almeno 2 delle stringhe presenti nella lista `l` (case-sensitive).

```python
def copiaRigheFiltro(file_in, file_out, l):
    with open(file_in, "r", encoding="UTF-8") as fin, open(file_out, "w", encoding="UTF-8") as fout:
        for riga in fin:
            trovate = 0
            for parola in l:
                if parola in riga:
                    trovate += 1
            if trovate >= 2:
                fout.write(riga)
```

---

## 3. `creaListaRighe(f, c, n)`
**Testo:** Restituisce la lista dei numeri di riga (con numerazione a partire da 1) del file `f` in cui il carattere `c` compare almeno `n` volte.

```python
def creaListaRighe(f, c, n):
    ris = []
    with open(f, "r", encoding="UTF-8") as fin:
        numero_riga = 1
        for riga in fin:
            if riga.count(c) >= n:
                ris.append(numero_riga)
            numero_riga += 1
    return ris
```

---

## 4. `creaListaParole(f, c)`
**Testo:** Restituisce la lista ordinata alfabeticamente delle parole (usando `split()`) che iniziano e finiscono per il carattere `c` (senza doppioni).

```python
def creaListaParole(f, c):
    with open(f, "r", encoding="UTF-8") as fin:
        testo = fin.read()
        
    parole = testo.split()
    selezionate = set()
    
    for p in parole:
        if len(p) > 0 and p[0] == c and p[-1] == c:
            selezionate.add(p)
            
    ris = list(selezionate)
    ris.sort()
    return ris
```

---

## 5. `semprePiuAlto(file)`
**Testo:** Legge un file CSV di altezze. Verifica se esiste una persona che risulta strettamente la più alta in ogni singola riga di misurazione. Se il file è vuoto restituisce `"file vuoto"`, se non c'è restituisce `"non c'è uno sempre più alto"`.

```python
def semprePiuAlto(file):
    with open(file, "r", encoding="UTF-8") as fin:
        riga_nomi = fin.readline().strip()
        if len(riga_nomi) == 0:
            return "file vuoto"
            
        nomi = riga_nomi.split(",")
        leader = ""
        
        for riga in fin:
            riga = riga.strip()
            if len(riga) == 0:
                continue
            valori = [float(x) for x in riga.split(",")]
            if len(valori) != len(nomi):
                continue
                
            max_val = max(valori)
            # Verifica se il massimo è univoco nella riga
            if valori.count(max_val) > 1:
                return "non c'è uno sempre più alto"
                
            indice_max = valori.index(max_val)
            vincitore_riga = nomi[indice_max]
            
            if leader == "":
                leader = vincitore_riga
            elif leader != vincitore_riga:
                return "non c'è uno sempre più alto"
                
    return leader if leader != "" else "non c'è uno sempre più alto"
```
