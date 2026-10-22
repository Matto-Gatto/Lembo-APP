# Mappa Didattica per la Web App ("Duolingo Python")

Questo documento mappa ogni argomento delle lezioni del corso in **Unità Didattiche Gamificate** per la futura web application.

---

## 🌳 Albero delle Competenze (Skill Tree Progressivo)

```
[Unità 1: Hello World & Architettura]
       |
[Unità 2: Variabili, Tipi & Operatori]
       |
[Unità 3: Condizioni (if / elif / else)]
       |
[Unità 4: Cicli & Iterazioni (while / for)]
       |
[Unità 5: Funzioni & Modularità]
       |
[Unità 6: Strutture Dati (Liste, Tuple, Set)]
       |
[Unità 7: Dizionari (Key-Value)]
       |
[Unità 8: File I/O & File System]
       |
[Unità 9: Tabelle & File CSV]
       |
[Unità 10: Programmazione ad Oggetti (OOP)]
       |
[Unità 11: NumPy & Calcolo Vettoriale]
       |
[Unità 12: Boss Level: Simulazione Esame Ufficiale (3 Esercizi / 90 min)]
```

---

## 🎯 Tipologie di Esercizi Gamificati da Implementare

1. **Multiple Choice Quiz (Teoria & Sintassi):**
   - *Esempio (dalla Lezione 1):* "Qual è il compito della PVM (Python Virtual Machine)?"  
     - Opzione A: Tradurre il codice in C  
     - Opzione B: Eseguire il bytecode generato dal traduttore *(Corretta)*  
     - Opzione C: Controllare solo la sintassi  
2. **Fill-in-the-Blank (Completamento sintassi):**
   - *Esempio:* Completare la conversione: `n = ____(input("Inserisci n: "))` -> `int`
3. **Parsons Puzzle (Riorganizza i blocchi di codice indentati):**
   - Riordinare le righe del calcolo del MCD o del controllo divisibilità.
4. **Spot the Bug / Trova l'errore:**
   - Esempio: Individuare l'errore di concatenazione stringa-numero (`"Il numero è " + 5` -> `TypeError`).
5. **Micro-Coding Challenge (con Pyodide nel browser):**
   - Scrivi una funzione che prende due parametri e restituisce il risultato atteso, validata contro test case nascosti.
6. **Time Attack / Arena Esame:**
   - Simulatore della prova d'esame: 90 minuti per 3 funzioni con suite di test automatici che danno il voto in trentesimi.
