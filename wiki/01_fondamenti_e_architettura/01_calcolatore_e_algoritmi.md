# Calcolatore, Algoritmi e Problem Solving

## 1. Che cos'è l'Informatica?
- **Definizione:** L'informatica **non** è lo studio dei computer come artefatti fisici (costruzione o riparazione).
- **Oggetto di studio:** Studio sistematico della **risoluzione di problemi (*problem solving*)** attraverso la formulazione di algoritmi e la loro traduzione in programmi eseguibili da un calcolatore.
- **Interdisciplinarità:** Biologia (genomica), economia (modelli finanziari), climatologia, linguistica computazionale e filologia (risoluzione di paternità di testi letterari), grafica e videogiochi.

---

## 2. Architettura Concettuale: Hardware vs Software
- **Hardware (HW):** Componenti e dispositivi fisici del sistema di elaborazione.
  - La **CPU (Central Processing Unit)** esegue semplici operazioni aritmetico-logiche a velocità elevatissima (ordine di grandezza: ~1 nanosecondo per operazione, ossia $10^{-9}$ s).
- **Software (SW):** Insieme dei programmi eseguiti sul calcolatore.
  - **Applicazioni:** Livello con cui interagisce l'utente finale (browser, editor, fogli di calcolo).
  - **Sistema Operativo (OS):** Livello intermedio (Windows, Linux, macOS) che interagisce direttamente con l'hardware per gestire le risorse fisiche in modo efficiente e controllato.

```
+------------------------------------+
| Applicazioni (Word, Chrome, App)   |
+------------------------------------+
                 ↓
+------------------------------------+
| Sistema Operativo (OS)             |
+------------------------------------+
                 ↓
+------------------------------------+
| Hardware (CPU, RAM, Dischi, I/O)   |
+------------------------------------+
```

---

## 3. Il Concetto di Algoritmo
Un algoritmo è un procedimento di calcolo ("ricetta"), composto da una sequenza finita di passi elementari, che trasforma dati di ingresso (*input*) nei corrispondenti dati di uscita (*output*).

```
   [Dati di ingresso] ---> [ ELABORAZIONE (Algoritmo) ] ---> [Dati di uscita]
```

### Proprietà Formali Fondamentali
Un procedimento è un algoritmo se soddisfa tassativamente 3 requisiti:
1. **Non ambiguità (Chiarezza):** Ogni passo/istruzione deve essere formulato in modo univoco e deterministico.
2. **Efficacia:** Ogni passo deve essere concretamente eseguibile dalla macchina operatrice.
3. **Finitezza:** L'esecuzione deve necessariamente arrestarsi dopo un numero finito di passi/operazioni.

---

## 4. Metodologia: Dai Problemi al Codice
```
[Problema] ---> [Algoritmo di soluzione] ---> [Programma in LDP]
```

### Metodo dei Raffinamenti Successivi (Top-Down Design)
Quando un problema è complesso, si opera per livelli crescenti di dettaglio:
1. Si formula prima una versione ad alto livello di astrazione.
2. Si scompongono e si raffinano le singole operazioni in sotto-passi elementari o strutture di controllo.
3. Si raggiunge una specifica abbastanza dettagliata da essere codificata direttamente in un linguaggio di programmazione (LDP).

---

## 5. Pseudocodice
Linguaggio informale a metà strada tra il linguaggio naturale e un LDP, privo delle rigidità sintattiche dei compilatori ma dotato di strutture logiche formali:
- **Sequenza:** Esecuzione passo-passo dall'alto verso il basso.
- **Selezione condizionale:** `if <condizione> then <op1> else <op2>`
- **Iterazione pre-condizionale:** `while <condizione> do <op>`
- **Iterazione enumerativa:** `for ogni valore tra A e B do <op>`

### Esempio Didattico del Corso: Massimo Comun Divisore (MCD)
Calcolo dell'MCD tra due interi positivi $m$ ed $n$:
1. Calcola l'insieme $I$ dei divisori di $m$.
   - *Raffinamento:* Per ogni $i$ da $1$ a $m$, se $m \pmod i == 0$, inserisci $i$ in $I$.
2. Calcola l'insieme $J$ dei divisori di $n$.
   - *Raffinamento:* Per ogni $i$ da $1$ a $n$, se $n \pmod i == 0$, inserisci $i$ in $J$.
3. Calcola l'insieme $K = I \cap J$ (intersezione = divisori comuni).
4. Restituisci il massimo elemento in $K$.
