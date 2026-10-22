# Dizionari in Python: Struttura Chiave-Valore, Proprietà e Metodi

## 1. Che cos'è un Dizionario (`dict`)?
Un dizionario è una struttura dati **mutabile** che memorizza coppie **chiave : valore** (*key : value*):
- Ogni elemento è identificato univocamente dalla sua **chiave** (e non da un indice numerico posizionale!).
- Si crea con le parentesi graffe: `d = {"mario": 28, "luigi": 30}` o `d = {}` per il dizionario vuoto.

### Proprietà Fondamentali:
1. **Unicità delle chiavi:** I valori associati possono ripetersi, ma le chiavi **non possono mai duplicarsi**. Se si assegna un valore a una chiave già esistente (`d["mario"] = 31`), il vecchio valore viene sovrascritto.
2. **Tipi delle chiavi (Hashable):** Le chiavi possono essere di qualsiasi tipo **immutabile** (stringhe, numeri interi/float, tuple). Non possono mai essere liste (`TypeError: unhashable type: 'list'`).
3. **I valori possono essere di qualunque tipo:** numeri, stringhe, liste, altri dizionari annidati.
4. **L'operatore `in` si applica solo alle chiavi:**
   ```python
   d = {"a": 10, "b": 20}
   "a" in d   # True (è una chiave)
   10 in d    # False! (10 è un valore, non una chiave)
   ```

---

## 2. Metodi Fondamentali dei Dizionari

| Metodo / Sintassi | Descrizione |
| :--- | :--- |
| `d[chiave]` | Accede al valore associato. Se la chiave non esiste genera `KeyError`. |
| `d.get(chiave, default=None)` | Restituisce il valore associato; se non esiste restituisce `default` (senza errori!). |
| `d.pop(chiave)` | Rimuove la coppia e restituisce il valore associato. |
| `d.keys()` | Restituisce una vista iterabile di tutte le chiavi. |
| `d.values()` | Restituisce una vista iterabile di tutti i valori. |
| `d.items()` | Restituisce coppie tupla `(chiave, valore)`. |
| `d.copy()` | Crea una copia superficiale del dizionario. |
| `d.clear()` | Svuota il dizionario (`{}`). |

---

## 3. Pattern Fondamentale del Corso: Il Conteggio di Frequenze
Come contare le frequenze di parole o caratteri in modo compatto:

```python
# Con if-else standard
d = {}
for parola in lista_parole:
    if parola in d:
        d[parola] += 1
    else:
        d[parola] = 1

# Oppure con get() in una sola riga:
for parola in lista_parole:
    d[parola] = d.get(parola, 0) + 1
```

---

## 4. Ordinamento di un Dizionario
Un dizionario non è ordinato posizionalmente; per ordinarlo si trasformano le chiavi o i valori in liste:

- **Ordinare per Chiave:**
  ```python
  for k in sorted(d.keys()):
      print(k, d[k])
  ```
- **Trovare le Chiavi con il Valore Massimo:**
  ```python
  max_val = max(d.values())
  migliori = [k for k in d if d[k] == max_val]
  ```
