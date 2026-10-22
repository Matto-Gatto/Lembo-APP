# Gestione dei File di Testo, Cursore, Encoding e File CSV

## 1. Apertura e Chiusura dei File
In Python si usa la funzione built-in `open()`:
```python
f = open("nome_file.txt", mode="r", encoding="UTF-8")
# ... operazioni di I/O ...
f.close()  # Obbligatorio per rilasciare le risorse!
```

### Modalità di Apertura (`mode`):
- `'r'` (Read, default): Apre in sola lettura. Se il file non esiste, genera `FileNotFoundError`.
- `'w'` (Write): Apre in scrittura. Se il file **non esiste viene creato**; se **esiste viene sovrascritto e azzerato**!
- `'a'` (Append): Apre in aggiunta in coda. Se non esiste viene creato.

### Il Context Manager (`with`):
Garantisce la chiusura automatica del file anche in caso di eccezioni o errori a runtime:
```python
with open("dati.txt", "w", encoding="UTF-8") as f:
    f.write("Prima riga\n")
```

---

## 2. Metodi di Lettura e il Cursore del File
Un file aperto possiede un **cursore interno** che avanza mano a mano che si legge e **non torna indietro** a meno di chiudere e riaprire il file.

1. `f.read()`: Legge tutto il file restituendo un'**unica stringa**.
2. `f.readlines()`: Legge tutte le righe restituendo una **lista di stringhe** (ciascuna terminata da `\n`).
3. `f.readline()`: Legge una sola riga alla volta. Quando il file finisce, restituisce una stringa vuota `""`.
4. `for riga in f:`: **Il metodo più efficiente** in assoluto; carica e consuma una riga alla volta in memoria (ideale per file di grandi dimensioni).

---

## 3. Metodi di Scrittura
- `f.write(s)`: Scrive la stringa `s` nel file. Non va a capo da solo; occorre includere esplicitamente `\n`.
- `print(s, file=f, end='')`: Reindirizza l'output della funzione `print` direttamente sul file.

---

## 4. Manipolazione del Formato CSV (*Comma Separated Values*)
Nei file CSV ogni riga rappresenta un record e i campi sono separati da un delimitatore (solitamente la virgola `,` o punto e virgola `;`):

### Differenza Fondamentale nell'uso di `split()`:
- `s.split()` (senza argomenti): collassa sequenze di spazi/tab/newline e su stringa vuota `"".split()` produce `[]`.
- `s.split(",")` (con argomento virgola): divide strettamente su ogni virgola e su stringa vuota `"".split(",")` produce `[""]`!

### Pattern Standard di Lettura e Parsing CSV:
```python
def leggi_tabella(nome_file):
    with open(nome_file, "r", encoding="UTF-8") as f:
        intestazione = f.readline().strip().split(",")
        num_colonne = len(intestazione)
        
        dati = []
        for riga in f:
            riga = riga.strip()
            if len(riga) > 0:  # Salta righe vuote
                valori = riga.split(",")
                if len(valori) == num_colonne:  # Salta righe malformate
                    dati.append(valori)
    return intestazione, dati
```
