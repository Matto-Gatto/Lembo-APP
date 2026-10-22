# Esercizi Risolti — Dizionari

Raccolta completa degli esercizi tratti dal notebook "Dizionari", con codice verificato e test ufficiali.

---

## 1. `sommaImporti(file)`
**Testo:** Riceve un file CSV con coppie `Nome,Importo` guadagnato. Restituisce un dizionario contenente per ogni persona il totale guadagnato. Se il file è vuoto, restituisce un dizionario vuoto `{}`.

```python
def sommaImporti(file):
    d = {}
    with open(file, "r", encoding="UTF-8") as f:
        for riga in f:
            riga = riga.strip()
            if len(riga) > 0:
                parti = riga.split(",")
                if len(parti) == 2:
                    nome = parti[0].strip()
                    importo = int(parti[1].strip())
                    d[nome] = d.get(nome, 0) + importo
    return d

# Casi di test:
# tester_fun(sommaImporti, ["importi1.csv"], {'Mario': 23, 'Giorgio': 15, 'Michela': 37})
# tester_fun(sommaImporti, ["vuoto.csv"], {})
```

---

## 2. `creaDizionarioAltezze(file)`
**Testo:** Legge un file CSV di altezze e restituisce un dizionario con chiavi i nomi delle persone e valori la lista delle loro altezze come stringhe, nell'ordine in cui compaiono. Se vuoto restituisce `{}`.

```python
def creaDizionarioAltezze(file):
    d = {}
    with open(file, "r", encoding="UTF-8") as f:
        riga_nomi = f.readline().strip()
        if len(riga_nomi) == 0:
            return d
            
        nomi = [n.strip() for n in riga_nomi.split(",")]
        for n in nomi:
            d[n] = []
            
        for riga in f:
            riga = riga.strip()
            if len(riga) > 0:
                valori = [v.strip() for v in riga.split(",")]
                if len(valori) == len(nomi):
                    for i in range(len(nomi)):
                        d[nomi[i]].append(valori[i])
    return d
```

---

## 3. `voti(file)`
**Testo:** Riceve un file con tutti i voti degli esami (formato `Nome,Esame,Voto`). Calcola l'elenco in ordine alfabetico di tutti gli studenti che hanno preso **almeno 27 a tutti i loro esami** sostenuti.

```python
def voti(file):
    # Costruiamo un dizionario: studente -> lista di voti interi
    studenti_voti = {}
    with open(file, "r", encoding="UTF-8") as f:
        for riga in f:
            riga = riga.strip()
            if len(riga) > 0:
                parti = riga.split(",")
                if len(parti) >= 3:
                    nome = parti[0].strip()
                    voto = int(parti[2].strip())
                    studenti_voti.setdefault(nome, []).append(voto)
                    
    # Filtriamo chi ha tutti i voti >= 27
    bravi = []
    for nome, voti_list in studenti_voti.items():
        if all(v >= 27 for v in voti_list):
            bravi.append(nome)
            
    bravi.sort()
    return bravi

# Casi di test:
# tester_fun(voti, ['esami1.csv'], ['Giovanni', 'Maria'])
```

---

## 4. `infoContatto(file, nome, campo)`
**Testo:** Data una rubrica di contatti Google in CSV, cerca tutti i contatti il cui nome completo contiene la sottostringa `nome` (case-sensitive) e restituisce una lista di coppie `[nome_completo, valore_campo]`.

```python
def infoContatto(file, nome, campo):
    ris = []
    with open(file, "r", encoding="UTF-8") as f:
        riga_campi = f.readline().strip()
        if len(riga_campi) == 0:
            return ris
            
        campi = [c.strip() for c in riga_campi.split(",")]
        if campo not in campi:
            return ris
            
        idx_campo = campi.index(campo)
        # Supponiamo che il primo campo (o 'Name'/'Given Name') contenga il nome
        # Nel file Google CSV standard la prima colonna è il display name
        for riga in f:
            riga = riga.strip()
            if len(riga) > 0:
                valori = [v.strip() for v in riga.split(",")]
                if len(valori) == len(campi):
                    nome_completo = valori[0]
                    if nome in nome_completo:
                        ris.append([nome_completo, valori[idx_campo]])
    return ris
```
