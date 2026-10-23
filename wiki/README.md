# Wiki del Corso: Fondamenti di Programmazione I
> **Docente:** Prof. Domenico Lembo  
> **Corso di Laurea:** Filosofia ed Intelligenza Artificiale (9 CFU) / Lettere Moderne (6 CFU)  
> **A.A.:** 2025-2026 — Sapienza Università di Roma  
> **Modalità Esame:** Prova pratica al calcolatore (3 esercizi di scrittura funzioni in Python in 1 ora e mezza).

---

## 🗺️ Mappa dei Contenuti e Indice della Wiki

| Sezione | Documento | Argomenti Principali | Stato Materiale |
| :--- | :--- | :--- | :---: |
| **00. Info Corso** | [`00_corso/programma_e_esame.md`](file:///c:/App/PY%20game/wiki/00_corso/programma_e_esame.md) | Obiettivi, CFU, calendario appelli, struttura prova d'esame | ✅ Indicizzato |
| **01. Teoria Introduttiva** | [`01_fondamenti_e_architettura/01_calcolatore_e_algoritmi.md`](file:///c:/App/PY%20game/wiki/01_fondamenti_e_architettura/01_calcolatore_e_algoritmi.md) | Algoritmi, pseudocodice, raffinamenti successivi, HW/SW | ✅ Indicizzato |
| | [`01_fondamenti_e_architettura/02_linguaggi_e_python.md`](file:///c:/App/PY%20game/wiki/01_fondamenti_e_architettura/02_linguaggi_e_python.md) | Compilatore vs Interprete, Bytecode, PVM, modello di Python | ✅ Indicizzato |
| | [`01_fondamenti_e_architettura/03_ambiente_di_sviluppo.md`](file:///c:/App/PY%20game/wiki/01_fondamenti_e_architettura/03_ambiente_di_sviluppo.md) | Script `.py`, Shell interattiva, Spyder, Jupyter Notebook | ✅ Indicizzato |
| **02. Numeri, I/O & Moduli** | [`02_numeri_variabili_io/01_espressioni_numeriche_e_moduli.md`](file:///c:/App/PY%20game/wiki/02_numeri_variabili_io/01_espressioni_numeriche_e_moduli.md) | Tipi `int`/`float`, operatori `/`, `//`, `%`, `**`, `math`, `random` | ✅ Indicizzato |
| | [`02_numeri_variabili_io/02_variabili_assegnazione_e_io.md`](file:///c:/App/PY%20game/wiki/02_numeri_variabili_io/02_variabili_assegnazione_e_io.md) | Assegnazione `=`, operatori composti, `input()`, `print()`, casting | ✅ Indicizzato |
| | [`02_numeri_variabili_io/esercizi_risolti_lezione2.md`](file:///c:/App/PY%20game/wiki/02_numeri_variabili_io/esercizi_risolti_lezione2.md) | Esercizi risolti: potenze, radici, stringhe, aree cerchio, cilindro | ✅ Indicizzato |
| **03. Stringhe** | [`03_stringhe/01_stringhe_e_metodi.md`](file:///c:/App/PY%20game/wiki/03_stringhe/01_stringhe_e_metodi.md) | Escape (`\n`, `\t`), `len`, `lower`, `upper`, `strip`, `count`, `find`, `ord`, `chr` | ✅ Indicizzato |
| | [`03_stringhe/02_slicing_e_immutabilita.md`](file:///c:/App/PY%20game/wiki/03_stringhe/02_slicing_e_immutabilita.md) | Indicizzazione, Slicing `s[i:j:k]`, indici negativi, immutabilità | ✅ Indicizzato |
| | [`03_stringhe/esercizi_risolti_stringhe.md`](file:///c:/App/PY%20game/wiki/03_stringhe/esercizi_risolti_stringhe.md) | Esercizi risolti: ricerca/replace, campionamento con passo, quadrato caratteri | ✅ Indicizzato |
| **04. Flusso Condizionale** | [`04_condizioni_e_flusso/01_booleani_e_logica.md`](file:///c:/App/PY%20game/wiki/04_condizioni_e_flusso/01_booleani_e_logica.md) | Booleani `True`/`False`, relazionali, `and`/`or`/`not`, De Morgan | ✅ Indicizzato |
| | [`04_condizioni_e_flusso/02_istruzioni_if_elif_else.md`](file:///c:/App/PY%20game/wiki/04_condizioni_e_flusso/02_istruzioni_if_elif_else.md) | `if`, `else`, `elif`, indentazione, metodi booleani stringhe | ✅ Indicizzato |
| | [`04_condizioni_e_flusso/03_confronto_float_e_validazione_input.md`](file:///c:/App/PY%20game/wiki/04_condizioni_e_flusso/03_confronto_float_e_validazione_input.md) | Confronto `float` con `abs()` / `isclose()`, parsing numero reale | ✅ Indicizzato |
| | [`04_condizioni_e_flusso/esercizi_risolti_condizioni.md`](file:///c:/App/PY%20game/wiki/04_condizioni_e_flusso/esercizi_risolti_condizioni.md) | Esercizi risolti: sottostringa, ordinamento, palindromi, indovinello | ✅ Indicizzato |
| **05. Cicli & Iterazioni** | [`05_cicli_iterazioni/01_ciclo_while_e_sentinelle.md`](file:///c:/App/PY%20game/wiki/05_cicli_iterazioni/01_ciclo_while_e_sentinelle.md) | Ciclo `while`, cicli definiti/indefiniti, pattern sentinella | ✅ Indicizzato |
| | [`05_cicli_iterazioni/02_ciclo_for_e_range.md`](file:///c:/App/PY%20game/wiki/05_cicli_iterazioni/02_ciclo_for_e_range.md) | Ciclo `for`, funzione `range()`, scansione indici vs caratteri, tabelle | ✅ Indicizzato |
| | [`05_cicli_iterazioni/03_break_continue_e_figure.md`](file:///c:/App/PY%20game/wiki/05_cicli_iterazioni/03_break_continue_e_figure.md) | `break`, `continue`, confronto while vs for, disegno figure (`*`) | ✅ Indicizzato |
| | [`05_cicli_iterazioni/esercizi_risolti_cicli.md`](file:///c:/App/PY%20game/wiki/05_cicli_iterazioni/esercizi_risolti_cicli.md) | Esercizi risolti: serie armonica, polinomi, base 2 a 8, lettere doppie | ✅ Indicizzato |
| **06. Funzioni & Testing** | [`06_funzioni_e_testing/01_definizione_parametri_e_scope.md`](file:///c:/App/PY%20game/wiki/06_funzioni_e_testing/01_definizione_parametri_e_scope.md) | `def`, parametri formali vs argomenti, scope locale/globale, `global` | ✅ Indicizzato |
| | [`06_funzioni_e_testing/02_return_effetti_collaterali_e_moduli.md`](file:///c:/App/PY%20game/wiki/06_funzioni_e_testing/02_return_effetti_collaterali_e_moduli.md) | `return` vs `print()`, valore `None`, early return, side-effects | ✅ Indicizzato |
| | [`06_funzioni_e_testing/03_parametri_opzionali_e_tester_fun.md`](file:///c:/App/PY%20game/wiki/06_funzioni_e_testing/03_parametri_opzionali_e_tester_fun.md) | Valori di default, keyword arguments, framework `tester_fun` | ✅ Indicizzato |
| | [`06_funzioni_e_testing/04_reimplementazione_count_find_rfind.md`](file:///c:/App/PY%20game/wiki/06_funzioni_e_testing/04_reimplementazione_count_find_rfind.md) | Replica manuale con algoritmi da zero di `count`, `find`, `rfind` | ✅ Indicizzato |
| | [`06_funzioni_e_testing/esercizi_risolti_funzioni.md`](file:///c:/App/PY%20game/wiki/06_funzioni_e_testing/esercizi_risolti_funzioni.md) | Esercizi risolti: `fattoriale`, `maxdivisore`, `maxfreq`, `collegaNoRipetizioni`, `maxlung`, `sostituisci` | ✅ Indicizzato |
| **07. Liste, Tuple & Insiemi** | [`07_strutture_dati_liste_tuple_set/01_liste_e_gestione_memoria.md`](file:///c:/App/PY%20game/wiki/07_strutture_dati_liste_tuple_set/01_liste_e_gestione_memoria.md) | Mutabilità, Stack vs Heap, `copy()`, trappola rimozione in ciclo | ✅ Indicizzato |
| | [`07_strutture_dati_liste_tuple_set/02_tuple_e_insiemi.md`](file:///c:/App/PY%20game/wiki/07_strutture_dati_liste_tuple_set/02_tuple_e_insiemi.md) | Tuple immutabili, unpacking, `*args`, insiemi (`set`) e operazioni | ✅ Indicizzato |
| | [`07_strutture_dati_liste_tuple_set/esercizi_risolti_liste_tuple_set.md`](file:///c:/App/PY%20game/wiki/07_strutture_dati_liste_tuple_set/esercizi_risolti_liste_tuple_set.md) | 12 esercizi risolti: `merge`, `divisoriComuni`, `unisci`, selezioni, frequenze | ✅ Indicizzato |
| **08. File & File System** | [`08_file_e_filesystem/01_lettura_scrittura_file_e_csv.md`](file:///c:/App/PY%20game/wiki/08_file_e_filesystem/01_lettura_scrittura_file_e_csv.md) | `open`, `read`, `readlines`, cursore file, `with`, CSV e `split(",")` | ✅ Indicizzato |
| | [`08_file_e_filesystem/esercizi_risolti_file.md`](file:///c:/App/PY%20game/wiki/08_file_e_filesystem/esercizi_risolti_file.md) | Esercizi risolti: `stringaMaxFreq`, `copiaRigheFiltro`, `creaListaRighe`, `semprePiuAlto` | ✅ Indicizzato |
| **09. Dizionari & Tabelle** | [`09_dizionari/01_dizionari_e_metodi.md`](file:///c:/App/PY%20game/wiki/09_dizionari/01_dizionari_e_metodi.md) | Chiave-valore, hashability, `get()`, conteggio frequenze, ordinamento | ✅ Indicizzato |
| | [`09_dizionari/esercizi_risolti_dizionari.md`](file:///c:/App/PY%20game/wiki/09_dizionari/esercizi_risolti_dizionari.md) | Esercizi risolti: `sommaImporti`, `creaDizionarioAltezze`, `voti`, `infoContatto` | ✅ Indicizzato |
| **10. Esercitazioni Ufficiali (1-10, 12)** | [`10_esercitazioni_ufficiali/esercitazione_1.md`](file:///c:/App/PY%20game/wiki/10_esercitazioni_ufficiali/esercitazione_1.md) | **Es. 1:** I/O, tipi, equazioni 2° grado | ✅ Indicizzato |
| | [`10_esercitazioni_ufficiali/esercitazione_2.md`](file:///c:/App/PY%20game/wiki/10_esercitazioni_ufficiali/esercitazione_2.md) | **Es. 2:** `if/else`, triangoli, bisestili, Celsius/Fahrenheit | ✅ Indicizzato |
| | [`10_esercitazioni_ufficiali/esercitazione_3.md`](file:///c:/App/PY%20game/wiki/10_esercitazioni_ufficiali/esercitazione_3.md) | **Es. 3:** `while`, sentinelle `*`, numeri primi | ✅ Indicizzato |
| | [`10_esercitazioni_ufficiali/esercitazione_4.md`](file:///c:/App/PY%20game/wiki/10_esercitazioni_ufficiali/esercitazione_4.md) | **Es. 4:** accumulatori, Fibonacci, catene parole | ✅ Indicizzato |
| | [`10_esercitazioni_ufficiali/esercitazione_5.md`](file:///c:/App/PY%20game/wiki/10_esercitazioni_ufficiali/esercitazione_5.md) | **Es. 5:** stringhe, distanze massime, contorni quadrati/diagonali | ✅ Indicizzato |
| | [`10_esercitazioni_ufficiali/esercitazione_6.md`](file:///c:/App/PY%20game/wiki/10_esercitazioni_ufficiali/esercitazione_6.md) | **Es. 6:** 11 funzioni d'esame (`Ex1` - `Ex11`) con return | ✅ Indicizzato |
| | [`10_esercitazioni_ufficiali/esercitazione_7.md`](file:///c:/App/PY%20game/wiki/10_esercitazioni_ufficiali/esercitazione_7.md) | **Es. 7:** 10 funzioni su liste (`Ex1` - `Ex10`): padding, somme Unicode | ✅ Indicizzato |
| | [`10_esercitazioni_ufficiali/esercitazione_8.md`](file:///c:/App/PY%20game/wiki/10_esercitazioni_ufficiali/esercitazione_8.md) | **Es. 8:** 10 funzioni su insiemi/tuple (`Ex1` - `Ex10`): join relazionale, coppie | ✅ Indicizzato |
| | [`10_esercitazioni_ufficiali/esercitazione_9.md`](file:///c:/App/PY%20game/wiki/10_esercitazioni_ufficiali/esercitazione_9.md) | **Es. 9:** 9 funzioni: dizionari, frequenze, coppie di parole, Quadrato Latino | ✅ Indicizzato |
| | [`10_esercitazioni_ufficiali/esercitazione_10.md`](file:///c:/App/PY%20game/wiki/10_esercitazioni_ufficiali/esercitazione_10.md) | **Es. 10:** 9 funzioni: CSV, basket, amici/nemici, IP, codici fiscali, eredità, calcio | ✅ Indicizzato |
| | [`10_esercitazioni_ufficiali/esercitazione_12.md`](file:///c:/App/PY%20game/wiki/10_esercitazioni_ufficiali/esercitazione_12.md) | **Es. 12 (OOP):** 7 funzioni su classi `Tempo`, `Persona`, `Squadra`, `Partita` | ✅ Indicizzato |
| **11. Simulazione Prova d'Esame** | [`11_simulazione_esame/simulazione_15_dicembre_2025.md`](file:///c:/App/PY%20game/wiki/11_simulazione_esame/simulazione_15_dicembre_2025.md) | **Prova d'Esame Ufficiale (15 Dic 2025 - Lab 11):** 3 compiti d'esame da 90 min (parola simmetrica, anagrammi incrociati, menù & disponibilità ristorante) | ✅ Indicizzato |
| **12. Classi e OOP** | [`12_classi_e_oggetti/01_programmazione_orientata_agli_oggetti.md`](file:///c:/App/PY%20game/wiki/12_classi_e_oggetti/01_programmazione_orientata_agli_oggetti.md) | Classi, `__init__`, `self`, `__str__`, `__repr__`, `__eq__`, `__hash__` per set/dict | ✅ Indicizzato |

---

## 🎮 Statistiche del Dataset Didattico
- **110+ Problemi Algoritmici ed Esercizi Ufficiali** risolti e pronti all'uso.
- **Tutti i requisiti del professor Domenico Lembo** (convenzioni di test, corner cases, gestione file CSV malformati, classi custom e dizionari annidati) mappati e formalizzati.
