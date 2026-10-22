# Liste in Python, Gestione della Memoria (Stack vs Heap) e Algoritmi di Modifica

## 1. Caratteristiche Fondamentali delle Liste
Una lista (`list`) è una sequenza **ordinata** ed **eterogenea** di elementi **mutabili**:
- Può contenere tipi diversi: `L = [10, "ciao", 3.14, True, [1, 2]]`.
- Gli elementi si accedono per indice (da `0` a `len(L) - 1`, o negativi da `-1`).
- È mutabile: `L[1] = "nuovo"` modifica direttamente l'elemento sul posto.

---

## 2. Modello di Memoria: Stack vs Heap

```
+------------------------------------+---------------------------------------+
| STACK (Dati statici / Frame)       | HEAP (Dati dinamici / Oggetti)        |
+------------------------------------+---------------------------------------+
| [Global Frame / Funzione]          |                                       |
| - Tipi Immutabili (int, str, float)|                                       |
|   a = 5  (valore memorizzato qui)  |                                       |
|                                    |                                       |
| - Tipi Mutabili (list, dict, set)  |                                       |
|   lista = [Puntatore ID: 0x104A] ---> [ 0x104A: [2, 4, 5] nell'Heap ]     |
+------------------------------------+---------------------------------------+
```

### Conseguenze Fondamentali:
1. **Assegnazione di Variabili (`L2 = L1`):**  
   Non crea una nuova lista! Copia solo il puntatore (riferimento alla stessa area nell'heap). Qualsiasi modifica a `L2` si riflette istantaneamente su `L1` (*aliasing*).
2. **Copia Superficiale vs Nuova Lista:**
   - Per creare una copia indipendente in una nuova zona di memoria:
     ```python
     L2 = L1.copy()   # oppure: L2 = L1[:]
     ```
   - Verifica: `L1 == L2` vale `True` (hanno gli stessi valori), ma `L1 is L2` vale `False` (hanno `id()` diversi in memoria).

---

## 3. Metodi Fondamentali delle Liste

| Metodo | In-Place? | Descrizione |
| :--- | :---: | :--- |
| `l.append(x)` | **SÌ** | Aggiunge `x` in fondo alla lista (stesso ID di memoria). |
| `l.extend(l2)` | **SÌ** | Concatena tutti gli elementi di `l2` in fondo a `l`. |
| `l.insert(i, x)` | **SÌ** | Inserisce `x` all'indice `i`, slittando gli elementi a destra. |
| `l.remove(x)` | **SÌ** | Rimuove la **prima occorrenza** di `x`. Lancia `ValueError` se `x` non c'è. |
| `l.pop([i])` | **SÌ** | Rimuove e **restituisce** l'elemento all'indice `i` (default: ultimo elemento). |
| `l.clear()` | **SÌ** | Svuota la lista (`[]`). |
| `l.reverse()` | **SÌ** | Inverte l'ordine degli elementi in loco. |
| `l.sort()` | **SÌ** | Ordina gli elementi omogenei in loco. Restituisce **`None`**! |
| `sorted(l)` | **NO** | Funzione built-in che restituisce una **nuova lista** ordinata, lasciando `l` invariata. |
| `l.count(x)` | **NO** | Conta le occorrenze di `x` nella lista. |
| `l.index(x)` | **NO** | Restituisce la prima posizione di `x` (o lancia `ValueError`). |

---

## 4. La Trappola Classica d'Esame: Modificare una Lista Durante il Ciclo!

> [!CAUTION]
> **MAI usare `for elem in l:` o `for i in range(len(l)):` rimuovendo elementi (`l.remove()`) durante l'iterazione!**
> Quando un elemento viene rimosso, tutti gli elementi successivi slittano a sinistra di una posizione. Il ciclo `for` avanza comunque al prossimo indice numerico, saltando l'elemento adiacente o causando `IndexError: list index out of range`!

### Le 2 Soluzioni Corrette:
1. **Iterare su una copia (`l.copy()`):**
   ```python
   for elem in l.copy():
       if type(elem) is not str:
           l.remove(elem)
   ```
2. **Usare un ciclo `while` (avanzando l'indice solo se NON si è rimosso nulla):**
   ```python
   i = 0
   while i < len(l):
       if type(l[i]) is not str:
           l.remove(l[i])  # Non incrementare i, il prossimo elemento è slittato qui!
       else:
           i += 1
   ```
