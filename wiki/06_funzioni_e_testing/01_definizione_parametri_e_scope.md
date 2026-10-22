# Definizione di Funzioni, Parametri e Visibilità (Scope) delle Variabili

## 1. Perché Usare le Funzioni?
Una funzione racchiude una sequenza di istruzioni a cui viene assegnato un nome per:
1. **Modularità e Riutilizzo:** evitare duplicazione di codice (*DRY - Don't Repeat Yourself*).
2. **Astrazione:** nascondere i dettagli implementativi esponendo solo una chiara interfaccia (input $\rightarrow$ elaborazione $\rightarrow$ output).

---

## 2. Sintassi di Definizione e Invocazione

```python
def nome_funzione(parametro1, parametro2):
    # Corpo della funzione (indentato)
    risultato = parametro1 + parametro2
    return risultato
```

- **Definizione vs Esecuzione:** Scrivere `def` **non** esegue il codice, ma si limita a registrare la funzione in memoria rendendola disponibile.
- **Invocazione (Chiamata):** Si usa il nome seguito dalle parentesi tonde con gli argomenti:
  ```python
  res = nome_funzione(5, 7)  # res conterrà 12
  ```

---

## 3. Parametri Formali vs Argomenti Effettivi
- **Parametri formali:** Le variabili dichiarate nell'intestazione della funzione (`n` in `def raddoppia(n):`).
- **Argomenti effettivi:** I valori o espressioni passati all'atto della chiamata (`raddoppia(7 + 3)`).
- All'invocazione, Python copia il valore di ciascun argomento nel corrispondente parametro formale.

---

## 4. Visibilità delle Variabili: Locali vs Globali

```
+-------------------------------------------------------------+
| AMBIENTE GLOBALE (Programma Principale)                     |
| Variabili globali: accessibili ovunque in sola lettura     |
|                                                             |
|   +-----------------------------------------------------+   |
|   | AMBIENTE LOCALE (Funzione)                          |   |
|   | - Parametri formali                                 |   |
|   | - Variabili create dentro la funzione               |   |
|   | - Invisibili al programma principale!               |   |
|   +-----------------------------------------------------+   |
+-------------------------------------------------------------+
```

### Regole Rigorose di Python:
1. **Le variabili locali nascono all'invocazione e muoiono al termine della funzione:**
   Se si prova a stampare dall'esterno una variabile locale, si ottiene `NameError: name 'x' is not defined`.
2. **Accesso in lettura a variabili globali:**
   Una funzione può leggere una variabile globale senza problemi.
3. **Modifica di variabili globali (La direttiva `global`):**
   Se dentro una funzione si assegna un valore a una variabile con lo stesso nome di una globale, Python la considera una **nuova variabile locale**, lasciando inalterata quella globale!
   Per forzare la modifica della globale, serve dichiararla esplicitamente con `global`:
   ```python
   k = 5
   def modifica():
       global k
       k = 9
   modifica()
   print(k)  # Stampa 9
   ```
   > [!WARNING]
   > L'uso di variabili globali all'interno delle funzioni è una pessima pratica didattica e di ingegneria del software: rende le funzioni rigide, non riutilizzabili e difficili da testare.
