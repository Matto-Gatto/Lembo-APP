# Esercitazione Ufficiale n. 10 — Lavoro Autonomo
> **Argomenti:** CSV avanzati, grafi di relazioni dinamiche (amici/nemici), validazione IP, decodifica codici fiscali, alberi genealogici ed eredità, classifiche di campionati sportivi.

---

## Ex1(fileName): Esami Superati (`Matricola,Voto,Materia`)
**Traccia:** Legge un CSV con intestazione `Matricola,Voto,Materia` e restituisce la lista di coppie tupla `(Matricola, Materia)` per gli esami con $voto \ge 18$, nello stesso ordine del file.
```python
def Ex1(fileName):
    ris = []
    with open(fileName, "r", encoding="UTF-8") as f:
        f.readline()  # Salta intestazione
        for riga in f:
            riga = riga.strip()
            if len(riga) > 0:
                mat, voto_s, materia = riga.split(",")
                if int(voto_s) >= 18:
                    ris.append((mat.strip(), materia.strip()))
    return ris
```

---

## Ex2(fileName): Materie con Almeno Due Studenti con Voto $\ge 29$
**Traccia:** Restituisce un insieme (`set`) contenente tutte e sole le materie per cui ci sono almeno due studenti distinti che hanno ottenuto un voto $\ge 29$.
```python
def Ex2(fileName):
    conteggio_materia = {}
    with open(fileName, "r", encoding="UTF-8") as f:
        f.readline()  # Salta intestazione
        for riga in f:
            riga = riga.strip()
            if len(riga) > 0:
                mat, voto_s, materia = riga.split(",")
                materia = materia.strip()
                if int(voto_s) >= 29:
                    conteggio_materia[materia] = conteggio_materia.get(materia, 0) + 1
                    
    ris = {m for m, count in conteggio_materia.items() if count >= 2}
    return ris
```

---

## Ex3(file, nome): Punti Totali di un Giocatore di Basket
**Traccia:** Righe con formato `Nome1 punti1;Nome2 punti2;...`. Calcola la somma dei punti realizzati dal giocatore `nome` in tutte le partite (0 se assente).
```python
def Ex3(file, nome):
    totale = 0
    with open(file, "r", encoding="UTF-8") as f:
        for riga in f:
            riga = riga.strip()
            if len(riga) > 0:
                voci = riga.split(";")
                for voce in voci:
                    voce = voce.strip()
                    if len(voce) > 0:
                        parti = voce.split()
                        if len(parti) == 2 and parti[0] == nome:
                            totale += int(parti[1])
    return totale
```

---

## Ex4(file): Rete Dinamica di Amici e Nemici
**Traccia:** File CSV `Nome1,Nome2,relazione` con relazione simmetrica `'amici'` o `'nemici'`. Se due persone diventano amiche si aggiungono alle rispettive liste (senza duplicati); se diventano nemiche si rimuovono. Restituisce il dizionario che mappa ogni persona nella **lista ordinata alfabeticamente** dei suoi amici finali.
```python
def Ex4(file):
    amici = {}
    with open(file, "r", encoding="UTF-8") as f:
        f.readline()  # Salta intestazione
        for riga in f:
            riga = riga.strip()
            if len(riga) > 0:
                p1, p2, rel = [x.strip() for x in riga.split(",")]
                if p1 not in amici: amici[p1] = set()
                if p2 not in amici: amici[p2] = set()
                
                if rel == 'amici':
                    amici[p1].add(p2)
                    amici[p2].add(p1)
                elif rel == 'nemici':
                    amici[p1].discard(p2)
                    amici[p2].discard(p1)
                    
    # Convertiamo gli insiemi in liste ordinate
    return {p: sorted(list(amici_set)) for p, amici_set in amici.items()}
```

---

## Ex5(file): Classificazione Indirizzi IPv4
**Traccia:** Classifica gli indirizzi del file in un dizionario con chiavi `'invalidi'`, `'domestici'` e `'altri'`:
- Indirizzo valido: 4 interi separati da punto `.` ciascuno compreso tra $0$ e $255$.
- Domestico: valido e con formato `192.168.X.Y`.
- Altri: valido ma non domestico.
```python
def Ex5(file):
    conteggi = {'invalidi': 0, 'domestici': 0, 'altri': 0}
    with open(file, "r", encoding="UTF-8") as f:
        for riga in f:
            riga = riga.strip()
            if len(riga) == 0:
                continue
            parti = riga.split(".")
            valido = False
            if len(parti) == 4 and all(p.isdecimal() and 0 <= int(p) <= 255 for p in parti):
                valido = True
                
            if not valido:
                conteggi['invalidi'] += 1
            else:
                ottetti = [int(p) for p in parti]
                if ottetti[0] == 192 and ottetti[1] == 168:
                    conteggi['domestici'] += 1
                else:
                    conteggi['altri'] += 1
    return conteggi
```

---

## Ex6(file): Decodifica Codici Fiscali e Calcolo Date di Nascita
**Traccia:** Estrae la data di nascita nel formato `dd/mm/aaaa` da codici fiscali italiani `ABCXYZaaMggWnnnV`.
- Anno: se $aa \le 20 \rightarrow 20aa$, altrimenti $19aa$.
- Mese: mappatura da lettera a numero mese:  
  `A:01, B:02, C:03, D:04, E:05, H:06, L:07, M:08, P:09, R:10, S:11, T:12`. Se la lettera non esiste $\rightarrow$ `'Mese errato'`.
- Giorno: se $gg > 40 \rightarrow gg - 40$ (femmina). Verificare che $1 \le giorno \le giorni\_del\_mese$. Se errato $\rightarrow$ `'Giorno errato'`. Se entrambi errati, prevale `'Mese errato'`.
```python
def Ex6(file):
    mesi_dict = {
        'A': ('01', 31), 'B': ('02', 28), 'C': ('03', 31),
        'D': ('04', 30), 'E': ('05', 31), 'H': ('06', 30),
        'L': ('07', 31), 'M': ('08', 31), 'P': ('09', 30),
        'R': ('10', 31), 'S': ('11', 30), 'T': ('12', 31)
    }
    ris = []
    with open(file, "r", encoding="UTF-8") as f:
        for riga in f:
            cf = riga.strip()
            if len(cf) == 0:
                continue
            aa_str = cf[6:8]
            m_code = cf[8]
            gg_str = cf[9:11]
            
            # Anno
            aa = int(aa_str)
            anno = 2000 + aa if aa <= 20 else 1900 + aa
            
            # Controllo mese
            if m_code not in mesi_dict:
                ris.append('Mese errato')
                continue
                
            mm_str, max_giorni = mesi_dict[m_code]
            
            # Controllo giorno
            giorno_val = int(gg_str)
            if giorno_val > 40:
                giorno_val -= 40
                
            if not (1 <= giorno_val <= max_giorni):
                ris.append('Giorno errato')
                continue
                
            giorno_formattato = f"{giorno_val:02d}"
            ris.append(f"{giorno_formattato}/{mm_str}/{anno}")
            
    return ris
```

---

## Ex7(file): Tracciamento dell'Eredità di Famiglia
**Traccia:** CSV con righe `Oggetto,Antenato,Erede`.
- L'antenato che compare per la prima volta con un oggetto ne è il proprietario originale.
- Un passaggio è valido solo se l'antenato possiede attualmente l'oggetto.
- Restituisce `{oggetto: [proprietario_originale, ultimo_erede_valido]}`.
```python
def Ex7(file):
    proprietario_originario = {}
    possessore_corrente = {}
    
    with open(file, "r", encoding="UTF-8") as f:
        f.readline()  # Salta header
        for riga in f:
            riga = riga.strip()
            if len(riga) > 0:
                ogg, ant, ere = [x.strip() for x in riga.split(",")]
                # Prima volta che vediamo l'oggetto: ant ne è il proprietario originario
                if ogg not in proprietario_originario:
                    proprietario_originario[ogg] = ant
                    possessore_corrente[ogg] = ere
                else:
                    # Passaggio valido solo se ant è il possessore corrente
                    if possessore_corrente[ogg] == ant:
                        possessore_corrente[ogg] = ere
                        
    return {ogg: [proprietario_originario[ogg], possessore_corrente[ogg]] for ogg in proprietario_originario}
```

---

## Ex8(fileName): Indici di Riga degli Interi nel File
**Traccia:** Restituisce un dizionario che mappa ogni intero che compare nel file nell'**insieme dei numeri di riga** (in base 1) in cui appare.
```python
def Ex8(fileName):
    d = {}
    with open(fileName, "r", encoding="UTF-8") as f:
        num_riga = 1
        for riga in f:
            riga = riga.strip()
            if len(riga) > 0:
                numeri = [int(x.strip()) for x in riga.split(",") if len(x.strip()) > 0]
                for n in numeri:
                    if n not in d:
                        d[n] = set()
                    d[n].add(num_riga)
            num_riga += 1
    return d
```

---

## Ex9(fileName): Classifica Torneo di Calcio da CSV
**Traccia:** Calcola i punti in classifica per ogni squadra (Vittoria = 3 punti, Pareggio = 1 punto, Sconfitta = 0 punti). Tutte le squadre menzionate nel file devono avere una chiave nel dizionario.
```python
def Ex9(fileName):
    punti = {}
    with open(fileName, "r", encoding="UTF-8") as f:
        f.readline()  # Salta header
        for riga in f:
            riga = riga.strip()
            if len(riga) > 0:
                s1, s2, g1_s, g2_s = [x.strip() for x in riga.split(",")]
                g1, g2 = int(g1_s), int(g2_s)
                
                if s1 not in punti: punti[s1] = 0
                if s2 not in punti: punti[s2] = 0
                
                if g1 > g2:
                    punti[s1] += 3
                elif g2 > g1:
                    punti[s2] += 3
                else:
                    punti[s1] += 1
                    punti[s2] += 1
    return punti
```
