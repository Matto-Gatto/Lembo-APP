# Tassonomia e Guida Strategica agli Esami del Prof. Domenico Lembo

> **Docente:** Prof. Domenico Lembo — Sapienza Università di Roma  
> **Formato Esame:** 3 Funzioni Python da completare in 90 minuti (1h 30m).  
> **Framework di Valutazione:** Test automatici con `tester_fun` su diversi file e casi limite (*corner cases*).

---

## 🎯 Anatomia di una Prova d'Esame Tipo

Analizzando tutti gli 8 compiti d'esame ufficiali (comprese le varianti A, B, C, D), l'esame è strutturato con regolarità matematica in **3 Esercizi Tipologici**:

```
[ESERCIZIO 1: Stringhe e Algoritmi Elementari] (~20 min, 8-10 punti)
       |
[ESERCIZIO 2: Liste, Insiemi e File di Testo]  (~30 min, 10-12 punti)
       |
[ESERCIZIO 3: File CSV, Tabelle e Dizionari Complessi] (~40 min, 10-12 punti)
```

---

## 🧩 Esercizio 1: Pattern Ricorrenti su Stringhe

### Obiettivo:
Verificare la padronanza di cicli (`while` o `for`), indicizzazione, slicing, e codici Unicode.

### I Pattern più Frequenti:
1. **Prefissi e Suffissi Comuni:**
   - Confronto posizionale da sinistra (`min(len(s1), len(s2))`) o da destra (`s[-1-i]`).
2. **Cifre o Caratteri Consecutivi:**
   - Scansione con indice $i$ e controllo di adiacenza: `s[i] in '0123456789' and s[i+1] in '0123456789'`.
3. **Caratteri Alternati o Invertiti:**
   - Ricostruzione di stringhe intercalando caratteri da due stringhe (es. prima lettera di $s_1$, ultima di $s_2$).
4. **Massima Distanza tra Caratteri Uguali:**
   - Uso di `s.rfind(c) - s.find(c)`.
5. **Distanza di Similarità / Hamming:**
   - Conteggio dei caratteri che occupano la stessa posizione con lo stesso valore.

> [!TIP]
> **Consiglio d'oro per Ex1:** Non dimenticare i casi limite: stringhe vuote `""`, stringhe di un solo carattere, o stringhe di lunghezze differenti!

---

## 📊 Esercizio 2: Pattern su Liste, Insiemi e File di Testo

### Obiettivo:
Verificare la gestione della memoria, modifiche in-place, dizionari di appoggio e conteggi condizionali.

### I Pattern più Frequenti:
1. **Modifica della Lista in-place (Rimozione o Duplicazione):**
   - Rimuovere gli elementi con il massimo numero di maiuscole o duplicare quelli con il massimo di minuscole.
   - *Tecnica obbligata:* usare un ciclo `while i < len(l)` e incrementare `i` solo se non si rimuove nulla!
2. **Mappature di Testo `{chiave: parola_massima}`:**
   - Leggere un file di testo con `split()`, raggruppare per lunghezza di parola, memorizzare solo la parola alfabeticamente maggiore.
3. **Mappa di Numeri di Riga `{elemento: set(righe)}`:**
   - Scandire riga per riga (contatore in base 1) e associare a ogni elemento l'insieme delle righe in cui compare.
4. **Ricerca del Dominio Email da File:**
   - Parsing manuale con `rfind('@')` e `rfind('.')` per isolare il dominio di secondo livello.

---

## 💼 Esercizio 3: Applicazioni Reali su File CSV e Dizionari

### Obiettivo:
È l'esercizio più corposo: richiede di elaborare un modello di business (gestione ordini, scorte, classifiche sportive, vendite commerciali, transazioni bancarie, treni in stazione).

### I Pattern più Frequenti:
1. **Consumo Scorte / Disponibilità (Pattern Atomico "Tutto o Niente"):**
   - *Regola:* Se un ordine contiene 2 piatti, verificare la disponibilità di entrambi **prima** di scalare le scorte. Se uno manca, l'ordine è `'respinto'` e le scorte rimangono intatte!
2. **Compravendita / Passaggio di Proprietà:**
   - Quadri, oggetti d'antiquariato, eredità. Il passaggio è valido solo se il venditore/antenato possiede attualmente l'oggetto.
3. **Transazioni Finanziarie (Banca / Saldi):**
   - File 1 (utenti e saldo iniziale) $\rightarrow$ File 2 (trasferimenti). Scalare dal mittente, accreditare al destinatario, controllare se il saldo va in negativo o se si applicano commissioni.
4. **Classifica di Campionato (Calcio / Basket):**
   - Calcolo punti (Vittoria 3, Pareggio 1, Sconfitta 0) o punti canestro aggregati per giocatore. Restituzione dell'insieme delle squadre o giocatori primi a pari merito.
5. **Classifica Prestazioni / Agenti di Vendita:**
   - Per ogni riga (mese/giorno), trovare il massimo di riga e assegnare 1 vittoria a tutti gli agenti a pari merito col massimo. Alla fine trovare gli agenti con più vittorie.

---

## ⚠️ I 5 Errori Più Gravi che Fanno Perdere Punti all'Esame

1. **Usare `print()` invece di `return`:**
   La funzione non restituisce nulla (`None`) e fallisce il 100% dei test automatici!
2. **Dimenticare di chiudere il file (`f.close()` o `with open`):**
   Può causare lock o dati non scritti su disco.
3. **Modificare una lista con `for` anziché `while`:**
   Genera salti di elementi e `IndexError`.
4. **Non considerare i file vuoti o stringhe vuote:**
   Se il file è vuoto o la prima riga è vuota, restituire subito `{}` o `set()` o `[]` come specificato nella traccia.
5. **Confusioni tra `str` e `int` su CSV:**
   I dati letti da file con `.split(",")` sono **stringhe**! Bisogna sempre convertirli esplicitamente con `int()` o `float()` prima di fare somme o confronti numerici (`"12" > "9"` vale `False` lessicograficamente!).
