# Tuple, Spacchettamento, Parametri Variabili (`*args`) e Insiemi (`set`)

## 1. Le Tuple (`tuple`)
Una tupla è una sequenza ordinata ed eterogenea di elementi **immutabili**:
- Si definisce con parentesi tonde o semplicemente separando i valori con virgole: `t = (10, -3, 4)` o `t = 10, -3, 4`.
- **Tupla di un solo elemento:** deve avere la virgola obbligatoria: `t = (5,)`. Scrivere `t = (5)` assegna semplicemente l'intero `5`!
- Immutabile: `t[0] = 25` lancia `TypeError: 'tuple' object does not support item assignment`.
- Supporta indicizzazione, slicing, concatenazione `+`, ripetizione `*`, `count()` e `index()`.

### Assegnazioni Multiple & Spacchettamento (*Unpacking*):
```python
giorno, mese, anno = 12, 10, 2025  # Assegna 3 variabili contemporaneamente
```

### Funzioni con Numero Variabile di Argomenti (`*args`):
L'asterisco prima del nome del parametro raccoglie tutti gli argomenti extra passati alla chiamata in una **tupla**:
```python
def somma(*valori):
    totale = 0
    for elemento in valori:
        totale += elemento
    return totale

print(somma(1, 2, 3, 4))  # Stampa 10
```

---

## 2. Gli Insiemi (`set`)
Un insieme (`set`) è una collezione **mutabile**, non ordinata, di **elementi unici** (nessun duplicato) e tassativamente **immutabili**:
- Si definisce con graffe `{1, 2, 3}` o tramite la funzione `set()`:
  - `set()`: crea l'insieme vuoto (attenzione: `{}` crea un dizionario vuoto!).
  - `set("casa")` $\rightarrow$ `{'c', 'a', 's'}` (elimina automaticamente i duplicati).
- Non è indicizzabile: `insieme[0]` lancia `TypeError: 'set' object is not subscriptable`.
- Non è garantito alcun ordine di iterazione.

---

## 3. Operatori e Metodi Sugli Insiemi

| Operazione | Operatore | Metodo Equivalente | Descrizione |
| :--- | :---: | :---: | :--- |
| **Unione** | `A \| B` | `A.union(B)` | Elementi presenti in $A$ o in $B$ (o in entrambi) |
| **Intersezione** | `A & B` | `A.intersection(B)` | Elementi presenti sia in $A$ che in $B$ |
| **Differenza** | `A - B` | `A.difference(B)` | Elementi che appartengono ad $A$ ma non a $B$ |
| **Diff. Simmetrica** | `A ^ B` | `A.symmetric_difference(B)` | Elementi in $A$ o $B$, ma NON in entrambi |
| **Sottoinsieme** | `A <= B` | `A.issubset(B)` | Verifica se $A \subseteq B$ (`True`/`False`) |
| **Disgiunzione** | — | `A.isdisjoint(B)` | Verifica se $A \cap B = \emptyset$ (`True`/`False`) |

### Modifica degli insiemi:
- `A.add(elem)`: aggiunge un elemento (se già presente, non ha effetto).
- `A.discard(elem)`: rimuove `elem` senza dare errore se l'elemento non c'era.
