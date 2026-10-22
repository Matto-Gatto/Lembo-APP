# Il Ciclo For, la Funzione `range()` e Scansioni di Sequenze

## 1. La Struttura del Ciclo `for`
In Python il ciclo `for` è un iteratore che scorre uno a uno gli elementi di una qualsiasi collezione o sequenza (stringhe, intervalli numerici, liste, tuple):

```python
for variabile in sequenza:
    istruzioni
```
- A ogni iterazione, `variabile` assume automaticamente il valore dell'elemento successivo della sequenza.
- È la scelta naturale e più pulita per **cicli definiti**.

---

## 2. La Funzione `range()`
Genera una sequenza aritmetica immutabile di numeri interi:

1. **Un solo parametro: `range(stop)`**  
   Numeri da $0$ fino a $stop - 1$ (passo $1$).  
   *Esempio:* `range(5)` genera `0, 1, 2, 3, 4`.
2. **Due parametri: `range(start, stop)`**  
   Numeri da $start$ fino a $stop - 1$ (passo $1$).  
   *Esempio:* `range(2, 7)` genera `2, 3, 4, 5, 6`.
3. **Tre parametri: `range(start, stop, step)`**  
   Numeri da $start$ fino a $stop$ escluso, incrementando di $step$.  
   *Esempio positivo:* `range(2, 9, 2)` $\rightarrow$ `2, 4, 6, 8`.  
   *Esempio decrescente:* `range(9, 2, -1)` $\rightarrow$ `9, 8, 7, 6, 5, 4, 3`.

---

## 3. Scansione di Stringhe: Per Carattere vs Per Indice

| Metodo | Codice | Quando Usarlo |
| :--- | :--- | :--- |
| **Scansione per elemento** | `for c in s:` | Quando serve solo leggere il carattere (più compatto e leggibile). |
| **Scansione per indice** | `for i in range(len(s)):` | Quando serve conoscere la posizione numerica `i`, accedere a caratteri adiacenti (`s[i+1]`), o scandire al contrario. |

### Esempio: Scansione all'indietro per indici
```python
s = "esame"
for i in range(len(s) - 1, -1, -1):
    print(s[i], end='')  # Stampa "emase"
```

---

## 4. Cicli Annidati e Tabelle Pitagoriche
Un ciclo può contenere un altro ciclo al suo interno. Per ogni iterazione del ciclo esterno, il ciclo interno viene eseguito completamente.

### Esempio Tabellina Pitagorica (1-10):
```python
for i in range(1, 11):
    for j in range(1, 11):
        print(i * j, end='\t')
    print()  # A capo alla fine di ogni riga
```

---

## 5. Algoritmo di Conversione di Base (da Base $B$ a Base 10)
Esempio didattico fondamentale presentato dal docente per convertire un numerale da base $2 \le B \le 16$ in decimale:

```python
s = "92B3"  # Numero in base 12
base = 12

valore = 0
potenza = len(s) - 1

for c in s:
    if c in "ABCDEF":
        cifra = ord(c) - ord("A") + 10
    else:
        cifra = int(c)
    valore += cifra * (base ** potenza)
    potenza -= 1

print("Valore decimale:", valore)  # 15975
```
