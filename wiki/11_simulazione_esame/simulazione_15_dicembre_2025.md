# Simulazione Ufficiale Prova d'Esame — 15 Dicembre 2025
> **Durata prova:** 1 ora e 30 minuti (90 minuti)  
> **Composizione:** 3 esercizi pratici di scrittura funzioni con suite di test automatica.

---

## Esercizio 1: `Ex1(s)` — Parola Più Lunga con Stessa Lettera Iniziale e Finale
**Traccia:**  
Data una stringa `s` composta da parole separate da spazi bianchi, calcolare la parola più lunga che inizia e finisce con la stessa lettera (case-sensitive).  
- Se ci sono più parole massimali della stessa lunghezza, restituire la **prima incontrata da sinistra a destra**.  
- Se nessuna parola soddisfa la condizione, restituire `''` (stringa vuota).

### Esempio:
`s = 'tanto gatta lardo lascia orto ala'` $\rightarrow$ restituisce `'orto'` (lunghezza 4).

### Soluzione Ottimale:
```python
def Ex1(s):
    parole = s.split()
    migliore = ''
    max_len = 0
    
    for p in parole:
        if len(p) > 0 and p[0] == p[-1]:
            if len(p) > max_len:
                max_len = len(p)
                migliore = p
                
    return migliore
```

---

## Esercizio 2: `Ex2(l1, l2)` — Insieme di Anagrammi Incrociati
**Traccia:**  
Riceve due liste di stringhe `l1` ed `l2`. Restituisce l'**insieme (`set`)** delle stringhe di `l1` che sono anagramma di una stringa di `l2` e delle stringhe di `l2` che sono anagramma di una stringa di `l1`.

### Esempio:
`l1 = ['arco', 'pippo', 'pluto', 'corda']`  
`l2 = ['palla', 'darco', 'ocra', 'casa']`  
Restituisce: `{'arco', 'corda', 'darco', 'ocra'}`  
*(Notare: `'arco'` e `'ocra'` sono anagrammi, `'corda'` e `'darco'` sono anagrammi).*

### Soluzione Ottimale:
Due stringhe sono anagrammi se e solo se le loro lettere ordinate sono identiche (`sorted(s1) == sorted(s2)`).
```python
def Ex2(l1, l2):
    ris = set()
    
    # 1. Trova elementi di l1 che hanno un anagramma in l2
    for s1 in l1:
        s1_ord = sorted(s1)
        for s2 in l2:
            if s1_ord == sorted(s2):
                ris.add(s1)
                ris.add(s2)  # Entrambe appartengono all'unione degli anagrammi
                
    return ris
```

---

## Esercizio 3: `Ex3(file1, file2)` — Gestione Ordini Ristorante e Disponibilità
**Traccia:**  
- `file1` (menù): `NomePiatto,Costo,Disponibilità` (piatti unici).
- `file2` (ordinazioni): `NomeCliente,NomePiatto_1,quantità_1,NomePiatto_2,quantità_2`.  
Le ordinazioni arrivano in ordine cronologico (dall'inizio alla fine del file).  
Per ogni cliente:
- Se la disponibilità di **entrambi** i piatti è sufficiente ($\text{disp} \ge \text{quantità}$), l'ordine viene completato: le scorte vengono scalate e al cliente viene addebitato il totale in euro.
- Se anche solo **uno** dei due piatti non ha disponibilità sufficiente, l'ordine viene **respinto**: nessuna porzione viene preparata (le scorte rimangono invariate) e nel dizionario il valore sarà `'respinto'`.

Restituisce un dizionario `{NomeCliente: costo_o_respinto}`.

### Esempio:
`file1`:
```
Carbonara,10,10
PastaVongole,12,6
Pollo,12,8
```
`file2`:
```
Giorgio,Carbonara,2,PastaVongole,4
Paola,Pollo,3,PastaVongole,3
Francesca,Pollo,3,Carbonara,3
```
Risultato: `{'Giorgio': 68, 'Paola': 'respinto', 'Francesca': 66}`  
*(Perché dopo Giorgio rimangono solo 2 PastaVongole; Paola ne chiede 3 quindi viene respinta. Francesca chiede Pollo e Carbonara che sono ancora disponibili e paga $3 \times 12 + 3 \times 10 = 66$).*

### Soluzione Ottimale:
```python
def Ex3(file1, file2):
    costo_piatto = {}
    disp_piatto = {}
    
    # 1. Caricamento menù
    with open(file1, "r", encoding="UTF-8") as f:
        for riga in f:
            riga = riga.strip()
            if len(riga) > 0:
                piatto, costo_s, disp_s = [x.strip() for x in riga.split(",")]
                costo_piatto[piatto] = int(costo_s)
                disp_piatto[piatto] = int(disp_s)
                
    risultato = {}
    
    # 2. Elaborazione ordini
    with open(file2, "r", encoding="UTF-8") as f:
        for riga in f:
            riga = riga.strip()
            if len(riga) > 0:
                cliente, p1, q1_s, p2, q2_s = [x.strip() for x in riga.split(",")]
                q1, q2 = int(q1_s), int(q2_s)
                
                # Verifica disponibilità di entrambi i piatti
                if disp_piatto.get(p1, 0) >= q1 and disp_piatto.get(p2, 0) >= q2:
                    # Scalo scorte
                    disp_piatto[p1] -= q1
                    disp_piatto[p2] -= q2
                    # Calcolo importo
                    totale = q1 * costo_piatto[p1] + q2 * costo_piatto[p2]
                    risultato[cliente] = totale
                else:
                    risultato[cliente] = 'respinto'
                    
    return risultato
```
