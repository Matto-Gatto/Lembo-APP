# Il `return`, Valore `None`, Effetti Collaterali e Moduli

## 1. `return` vs `print()` (Errore Classico d'Esame!)

> [!CAUTION]
> **Nelle prove d'esame è quasi sempre richiesto di RESTITUIRE il risultato (`return`) e NON di stamparlo (`print`)!**  
> Se si usa `print()` invece di `return`, la funzione restituisce implicitamente `None` e fallirà tutti i test automatici di valutazione!

```python
# SBAGLIATO (stampa ma non restituisce nulla!)
def raddoppia_errata(n):
    print(2 * n)

# CORRETTO (restituisce il valore al chiamante)
def raddoppia_corretta(n):
    return 2 * n
```

- Se una funzione non contiene `return`, oppure esegue `return` senza argomenti, restituisce automaticamente l'oggetto speciale **`None`**.
- La stessa funzione built-in `print()` restituisce `None`.

---

## 2. Uscita Anticipata: Il Pattern del "Doppio Return" (Early Return)
L'istruzione `return` provoca l'uscita **istantanea** dalla funzione, interrompendo qualsiasi riga successiva o ciclo in esecuzione.

### Esempio: Verifica Primalità con Early Return
Non serve accumulare flag booleani; appena si trova un divisore si esce subito con `return False`:
```python
def isprimo(n):
    if n <= 1:
        return False
    for i in range(2, (n // 2) + 1):
        if n % i == 0:
            return False  # Trovato divisore -> esci subito!
    return True           # Se il ciclo finisce senza divisori -> è primo!
```

---

## 3. Effetti Collaterali (*Side Effects*)
Si ha un effetto collaterale quando una funzione modifica lo stato esterno all'ambiente locale, ad esempio:
- Modifica variabili globali.
- Modifica parametri mutabili passati in ingresso (es. liste modificate sul posto).
- Esegue operazioni di I/O (scrittura su file, stampe su terminale).

### Buone Regole di Progettazione:
1. **Tutti gli input** devono essere passati come **parametri formali**.
2. **L'output** deve essere restituito tramite **`return`**.
3. **Nessun accesso diretto** a variabili globali.
4. Ridurre al minimo gli effetti collaterali non necessari per garantire la pura componibilità.

---

## 4. Creazione e Importazione di Moduli Personali
Per riutilizzare le funzioni in altri script:
1. Si salvano le definizioni in un file `.py` (es. `mieFunzioni.py`) nella stessa cartella.
2. Nello script principale si importano come qualsiasi libreria standard:
   ```python
   from mieFunzioni import ispari, isprimo
   ```
