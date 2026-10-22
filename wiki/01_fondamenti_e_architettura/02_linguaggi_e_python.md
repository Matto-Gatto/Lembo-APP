# Linguaggi di Programmazione e il Modello di Esecuzione di Python

## 1. Linguaggi Macchina vs Linguaggi ad Alto Livello
- **Linguaggio Macchina:** Istruzioni binarie (`0` e `1`) direttamente decodificabili dall'architettura hardware (CPU). Estremamente ostico per gli umani e dipendente dallo specifico processore.
- **Linguaggi ad Alto Livello:** Linguaggi vicini al ragionamento umano e alla logica matematica (Python, C, Java, C++, Pascal, ecc.). Offrono astrazione dall'hardware ma richiedono una fase di **traduzione**.

---

## 2. Paradigmi di Traduzione: Compilatori vs Interpreti

| Criterio | Compilatore (es. C, C++) | Interprete (es. modello puro) |
| :--- | :--- | :--- |
| **Meccanismo** | Traduce l'intero codice sorgente in codice macchina prima dell'esecuzione. | Traduce ed esegue il codice riga per riga a runtime. |
| **Output prodotto** | Genera un file binario eseguibile indipendente (es. `.exe`, formato ELF). | Non genera un binario autonomo; richiede l'interprete sempre presente. |
| **Fase di Linking** | Il *Linker* unisce il codice compilato con le librerie esterne. | La risoluzione dei riferimenti avviene dinamicamente durante l'esecuzione. |
| **Rilevamento Errori** | Errori di sintassi intercettati tutti a tempo di compilazione. | Errori rilevati quando l'interprete raggiunge la riga incriminata. |

---

## 3. L'Architettura di Python: Linguaggio Pseudo-Compilato

Python adotta un approccio ibrido a due stadi:

```
+----------------+      Fase 1: Parsing & Traduzione      +------------------+
| Codice Sorgente| -------------------------------------> | Bytecode Python  |
|    (.py)       |   (Controllore Sintattico & Parser)    |     (.pyc)       |
+----------------+                                        +------------------+
                                                                   |
                                                                   | Fase 2: Esecuzione
                                                                   v
                                                         +--------------------+
               [Input Utente] -------------------------> |   Python Virtual   |
                                                         |   Machine (PVM)    | ---> [Output]
                                                         +--------------------+
                                                                   |
                                                        (Errori a Runtime / Eccezioni)
```

1. **Pre-compilazione in Bytecode (`.pyc`):**
   - Il parser verifica la correttezza sintattica. Se rileva errori emette subito un `SyntaxError`.
   - Se il codice è corretto, viene compilato in una sequenza di istruzioni intermedie detta **bytecode** (salvata in cache `.pyc` per velocizzare le esecuzioni successive).
   - Il bytecode è indipendente dall'hardware sottostante.
2. **Esecuzione tramite Macchina Virtuale (PVM - Python Virtual Machine):**
   - La PVM è il motore a runtime che legge il bytecode e lo esegue, interagendo con il sistema operativo.
   - Vantaggi: Massima **portabilità** e **indipendenza dalla piattaforma** (lo stesso file gira su Windows, Linux, macOS purché sia presente la PVM).

---

## 4. Caratteristiche Distintive di Python
- **Creatore e Origine:** Creato all'inizio degli anni '90 da **Guido van Rossum** (appassionato dei *Monty Python*).
- **Governance:** Gestito dalla *Python Software Foundation* (no-profit). Van Rossum è stato per decenni il BDFL (*Benevolent Dictator for Life*) prima di ritirarsi dal ruolo nel 2018.
- **Licenza:** Free Software / Open Source.
- **Multiparadigma:**
  - **Imperativo:** comandi sequenziali che modificano lo stato.
  - **Funzionale:** funzioni matematiche pure e calcolo di risultati.
  - **Orientato agli Oggetti (OOP):** modellazione del dominio tramite classi e oggetti.
- **Sistema di Tipi (Type System):**
  - **Forte (Strong Typing):** I tipi non vengono convertiti arbitrariamente senza esplicita conversione (es. `3 + '5'` genera un `TypeError`).
  - **Dinamico (Dynamic Typing):** Il controllo del tipo avviene a run-time; le variabili sono etichette/riferimenti a oggetti in memoria e non richiedono dichiarazione preventiva del tipo.
- **Gestione Automatica della Memoria:** Gestita tramite **Garbage Collector** integrato (allocazione e deallocazione automatica degli oggetti non più referenziati).
- **Batteries Included:** Fornito di serie con una ricca libreria standard built-in.
