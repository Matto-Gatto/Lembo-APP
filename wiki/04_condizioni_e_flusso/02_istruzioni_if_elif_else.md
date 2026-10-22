# Il Controllo del Flusso: `if`, `else`, `elif` e Indentazione

## 1. Struttura Condizionale Base (`if`)
Permette di eseguire un blocco di istruzioni solo se una condizione booleana è vera:

```python
if condizione:
    istruzione_1
    istruzione_2
```

### Regole Sintattiche Fondamentali:
1. **I due punti `:`** devono essere sempre posti alla fine dell'intestazione condizionale.
2. **L'indentazione:** In Python i blocchi di codice non sono delimitati da parentesi graffe `{}` (come in C o Java) o parole chiave (`begin...end`), bensì dallo **spostamento a destra (rientro di 4 spazi)**.
3. Tutte le istruzioni con lo stesso livello di indentazione appartengono allo stesso blocco.

---

## 2. La Clausola Alternativa (`if - else`)
Esegue il primo blocco se la condizione è `True`, oppure il secondo se è `False`:

```python
if condizione:
    # Ramo if (eseguito se condizione è True)
    fai_qualcosa()
else:
    # Ramo else (eseguito se condizione è False)
    fai_altro()
```

---

## 3. Selezione Multipla (`if - elif - else`)
Quando ci sono più condizioni mutuamente esclusive, si evita di annidare infiniti `else: if ...` usando la parola chiave compatta `elif` (*else if*):

```python
voto = int(input("Inserisci il voto: "))

if voto > 27:
    print("Fascia: A (Eccellente)")
elif voto > 24:
    print("Fascia: B (Molto buono)")
elif voto > 20:
    print("Fascia: C (Discreto)")
elif voto >= 18:
    print("Fascia: C- (Sufficiente)")
else:
    print("Fascia: D (Non superato)")
```
*Le condizioni vengono esaminate dall'alto verso il basso. Non appena una risulta vera, il relativo blocco viene eseguito e tutti i restanti rami vengono ignorati.*

---

## 4. Metodi Booleani sulle Stringhe
Metodi che restituiscono direttamente `True` o `False`, perfetti come condizioni di `if`:

- `'sub' in s`: verifica se la sottostringa compare in `s` (es. `'pel' in 'spellare'` $\rightarrow$ `True`).
- `s.isalpha()`: `True` se la stringa non è vuota e contiene **solo caratteri alfabetici**.
- `s.isdecimal()`: `True` se la stringa non è vuota e contiene **solo cifre decimali** `0-9`.
- `s.islower()`: `True` se contiene almeno un carattere alfabetico e **nessun carattere maiuscolo**.
- `s.isupper()`: `True` se contiene almeno un carattere alfabetico e **nessun carattere minuscolo**.
