# Ambienti di Sviluppo ed Esecuzione in Python

## 1. Modalità di Esecuzione del Codice

### A. Esecuzione di Script da Terminale (`.py`)
- Il codice viene scritto in un file di testo semplice salvato con estensione `.py` (es. `helloworld.py`).
- Si esegue dal prompt dei comandi / terminale invocando l'interprete:
  ```bash
  python helloworld.py
  ```
- *Attenzione su Windows:* Verificare che le estensioni dei file siano visibili nelle opzioni di Esplora Risorse, per evitare file nominati erroneamente `helloworld.py.txt`.

### B. Modalità Interattiva (REPL - Read, Eval, Print Loop)
- Si avvia digitando semplicemente `python` nel terminale.
- Compare il prompt `>>>`:
  ```python
  >>> a = 5
  >>> b = 6
  >>> 2 * (a + b) + 3 * a
  37
  ```
- Ideale per sperimentazione rapida, test di singole funzioni o espressioni matematiche.

---

## 2. Ambienti di Sviluppo Integrati (IDE) e Notebook
Nel corso e nei laboratori vengono utilizzati:

1. **IDLE:** L'IDE minimale built-in fornito con l'installazione base di Python.
2. **Spyder:** 
   - L'IDE principale adottato nel corso.
   - Integra editor di testo con syntax highlighting, console interattiva IPython e inspector delle variabili in un'unica interfaccia.
3. **Jupyter Notebook (`.ipynb`) / JupyterLab:**
   - Strumento basato su celle interattive di codice e testo formattato (Markdown).
   - È il formato con cui il docente distribuisce le dispense e le note di lezione del corso.
4. **Miniconda / Anaconda:**
   - Gestore di pacchetti ed ambienti consigliato dal docente per installare in un colpo solo Python, Spyder, Jupyter e relative dipendenze.

---

## 3. Primo Esempio Completo di Programma Python (dal Corso)
Calcolo del Massimo Comun Divisore (MCD) tra due numeri inseriti dall'utente:

```python
# Lettura di due numeri interi da tastiera
m = int(input("Immetti un intero positivo: "))
n = int(input("Immetti un intero positivo: "))

print("Il massimo comun divisore di " + str(m) + " e " + str(n) + " è ")

# Inizializzazione degli insiemi dei divisori
Div_m = set()
Div_n = set()

for i in range(1, m + 1):
    if m % i == 0:
        Div_m.add(i)

for i in range(1, n + 1):
    if n % i == 0:
        Div_n.add(i)

# Intersezione insiemistica (divisori comuni)
D = Div_m & Div_n

# Stampa del massimo tra i divisori comuni
print(max(D))
```
