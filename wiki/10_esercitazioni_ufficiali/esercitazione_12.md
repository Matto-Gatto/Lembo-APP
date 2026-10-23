# Esercitazione Ufficiale n. 12 — Lavoro Autonomo (Classi e OOP)
> **Argomenti:** Classi `Tempo`, `Persona`, `Squadra`, `Partita`, operatori aritmetici su orari, ordinamento di oggetti e tabelle CSV orientate agli oggetti.

---

## Ex1(t1, t2): Distanza Assoluta in Secondi fra Due Oggetti `Tempo`
**Traccia:** Riceve due oggetti `t1` e `t2` di tipo `Tempo(Ore, Minuti, Secondi)` e restituisce il valore assoluto della loro differenza in secondi.  
*Esempio:* `t1 = Tempo(11, 10, 0)`, `t2 = Tempo(9, 30, 15)` $\rightarrow 5985$ secondi.
```python
def Ex1(t1, t2):
    sec1 = t1.Ore * 3600 + t1.Minuti * 60 + t1.Secondi
    sec2 = t2.Ore * 3600 + t2.Minuti * 60 + t2.Secondi
    return abs(sec1 - sec2)
```

---

## Ex2(l): Ordinamento Crescente e Rimozione Duplicati di Oggetti `Tempo`
**Traccia:** Riceve una lista $l$ di oggetti `Tempo` e restituisce una nuova lista con gli stessi oggetti ordinati in modo crescente e **senza ripetizioni**.  
*Esempio:* `[Tempo(10, 15), Tempo(9, 12, 34), Tempo(8, 30, 2)]` $\rightarrow$ `[Tempo(8, 30, 2), Tempo(9, 12, 34), Tempo(10, 15)]`.
```python
def Ex2(l):
    # Rimuove duplicati mantenendo un solo oggetto per valore di orario
    distinti = []
    for t in l:
        if t not in distinti:
            distinti.append(t)
            
    # Ordiniamo in base al numero totale di secondi
    distinti.sort(key=lambda t: t.Ore * 3600 + t.Minuti * 60 + t.Secondi)
    return distinti
```

---

## Ex3(t, s): Incremento di Secondi Modulo 24 Ore
**Traccia:** Riceve un oggetto `t` di tipo `Tempo` e un intero positivo $s$. Restituisce un nuovo oggetto `Tempo` incrementato di $s$ secondi con operazione "modulo 24 ore" ($86400$ secondi in un giorno).  
*Esempio:* `Tempo(23, 15, 0)` incrementato di $3675$ s $\rightarrow$ `Tempo(0, 16, 15)`.
```python
def Ex3(t, s):
    secondi_totali = (t.Ore * 3600 + t.Minuti * 60 + t.Secondi + s) % 86400
    nuove_ore = secondi_totali // 3600
    resto = secondi_totali % 3600
    nuovi_minuti = resto // 60
    nuovi_secondi = resto % 60
    return Tempo(nuove_ore, nuovi_minuti, nuovi_secondi)
```

---

## Ex4(l): Raggruppamento Oggetti `Persona` per Anno di Nascita
**Traccia:** Riceve una lista $l$ di oggetti `Persona(nome, annoNascita)` e restituisce un dizionario le cui chiavi sono gli anni di nascita e i cui valori sono gli **insiemi (`set`)** dei nomi delle persone nate in quell'anno.  
*Esempio:* `[Persona('mario', 1952), Persona('anna', 1952), Persona('aldo', 1970)]` $\rightarrow$ `{1952: {'mario', 'anna'}, 1970: {'aldo'}}`.
```python
def Ex4(l):
    d = {}
    for p in l:
        if p.annoNascita not in d:
            d[p.annoNascita] = set()
        d[p.annoNascita].add(p.nome)
    return d
```

---

## Ex5(file): Caricamento da CSV e Ordinamento Alfabetico di `Persona`
**Traccia:** Legge un CSV con intestazione `Nome,AnnoNascita`. Restituisce la lista di oggetti `Persona` ordinati alfabeticamente per nome. Se vuoto restituisce `[]`.
```python
def Ex5(file):
    persone = []
    with open(file, "r", encoding="UTF-8") as f:
        f.readline()  # Salta intestazione
        for riga in f:
            riga = riga.strip()
            if len(riga) > 0:
                nome, anno_s = [x.strip() for x in riga.split(",")]
                persone.append(Persona(nome, int(anno_s)))
                
    persone.sort(key=lambda p: p.nome)
    return persone
```

---

## Ex6(file): Caricamento Partite da CSV in Oggetti Composti
**Traccia:** Legge un CSV `Casa,Ospiti,GoalCasa,GoalOspiti` e restituisce una lista di oggetti `Partita(Squadra(casa), Squadra(ospiti), goalCasa, goalOspiti)` nello stesso ordine del file.
```python
def Ex6(file):
    partite = []
    with open(file, "r", encoding="UTF-8") as f:
        f.readline()  # Salta intestazione
        for riga in f:
            riga = riga.strip()
            if len(riga) > 0:
                casa, ospiti, g1_s, g2_s = [x.strip() for x in riga.split(",")]
                sq_casa = Squadra(casa)
                sq_ospiti = Squadra(ospiti)
                partite.append(Partita(sq_casa, sq_ospiti, int(g1_s), int(g2_s)))
    return partite
```

---

## Ex7(file): Squadre al Primo Posto in Classifica (Insieme di Oggetti `Squadra`)
**Traccia:** Calcola i punti del torneo (Vittoria=3, Pareggio=1, Sconfitta=0). Restituisce l'**insieme (`set`)** degli oggetti `Squadra` che occupano il primo posto a pari merito. Se non ci sono partite, restituisce `set()`.
```python
def Ex7(file):
    classifica = {}  # Squadra (oggetto) -> punti intero
    
    with open(file, "r", encoding="UTF-8") as f:
        f.readline()  # Salta intestazione
        for riga in f:
            riga = riga.strip()
            if len(riga) > 0:
                casa, ospiti, g1_s, g2_s = [x.strip() for x in riga.split(",")]
                s1 = Squadra(casa)
                s2 = Squadra(ospiti)
                g1, g2 = int(g1_s), int(g2_s)
                
                if s1 not in classifica: classifica[s1] = 0
                if s2 not in classifica: classifica[s2] = 0
                
                if g1 > g2:
                    classifica[s1] += 3
                elif g2 > g1:
                    classifica[s2] += 3
                else:
                    classifica[s1] += 1
                    classifica[s2] += 1
                    
    if len(classifica) == 0:
        return set()
        
    punti_max = max(classifica.values())
    prime = {sq for sq, p in classifica.items() if p == punti_max}
    return prime
```
