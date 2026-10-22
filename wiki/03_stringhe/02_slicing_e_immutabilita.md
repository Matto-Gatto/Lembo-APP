# Indicizzazione, Slicing e Immutabilità delle Stringhe

## 1. Indicizzazione (Accesso al Singolo Carattere)
Ogni carattere ha una posizione posizionale fissa con indice a base 0:
```
  Indici positivi:   0   1   2   3   4
  Caratteri:         p   a   l   l   a
  Indici negativi:  -5  -4  -3  -2  -1
```
- Accesso: `s[i]`. Ad esempio `s[1]` produce `'a'`.
- Indici negativi: `s[-1]` punta all'ultimo carattere, `s[-len(s)]` al primo.
- Se si accede a un indice fuori range (es. `s[5]` su `'palla'`), Python lancia `IndexError: string index out of range`.

---

## 2. Lo Slicing (`s[inizio:fine:passo]`)
Permette di estrarre una "fetta" (sottostringa) da una stringa.
- **Regola base:** `s[i:j]` estrae i caratteri dall'indice `i` **incluso** all'indice `j` **escluso** $[i, j)$.
  - Se `i` è omesso (`s[:j]`), parte dall'inizio (indice `0`).
  - Se `j` è omesso (`s[i:]`), arriva fino alla fine (indice `len(s)`).
  - `s[:]` restituisce una copia identica dell'intera stringa.
  - Se $i \ge j$ (con passo positivo), restituisce una **stringa vuota** `''` (senza errori!).

### Slicing con Passo (`s[i:j:passo]`)
- `s[i:j:k]` seleziona un carattere ogni `k` posizioni:
  ```python
  s = "paperopoli"
  s[1:8:2]  # Indici 1, 3, 5, 7 -> 'aeoo'
  ```
- **Inversione di una stringa con passo negativo:**
  ```python
  s = "python"
  s[::-1]   # Restituisce 'nohtyp'
  ```
  *(Trucco fondamentale spesso richiesto per verificare se una parola è palindroma!)*

---

## 3. L'Immutabilità delle Stringhe (Cruciale per gli Esami)
In Python le stringhe sono **oggetti immutabili**. Una volta create in memoria, non possono essere modificate sul posto (*in-place*).

```python
s = 'pippo'
s[1] = 'a'  # TypeError: 'str' object does not support item assignment
```

### Come "modificare" allora una stringa?
Bisogna **creare una nuova stringa** combinando slicing, concatenazioni o `replace()` e riassegnarla alla variabile:
```python
s = 'pippo'
# Vogliamo sostituire la seconda lettera 'i' con 'a' -> 'pappo'
s = s[0] + 'a' + s[2:]
```
