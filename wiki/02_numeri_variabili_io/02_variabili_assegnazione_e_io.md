# Variabili, Assegnazione, I/O (`input`, `print`) e Conversioni

## 1. Variabili e Istruzione di Assegnazione (`=`)
Una variabile è un'etichetta associata a una zona di memoria.
- **Sintassi:** `<nome_variabile> = <espressione>`
- L'espressione a destra viene valutata e il risultato viene assegnato alla variabile a sinistra.

> [!WARNING]
> L'assegnazione **NON** è un'uguaglianza matematica simmetrica!
> - In matematica: $a = b \iff b = a$.
> - In Python: `x = 7 * (5 + 2)` è valida, mentre `7 * (5 + 2) = x` genera `SyntaxError: cannot assign to expression here`.
> - Per verificare l'uguaglianza logica si usa il doppio uguale `==`.

---

## 2. Regole di Nomenclatura delle Variabili
1. Il **primo carattere** deve essere una lettera (`a-z`, `A-Z`) o il trattino basso (`_`). Non può iniziare con un numero!
2. I **caratteri successivi** possono essere lettere, cifre (`0-9`) o underscore (`_`).
3. Python è **case-sensitive** (distingue rigorosamente tra maiuscole e minuscole: `x` e `X` sono due variabili distinte!).

### Operatori di Assegnazione Composti
Sintassi compatta che calcola ed aggiorna contemporaneamente:
- `i += 5` $\iff$ `i = i + 5`
- `i -= 1` $\iff$ `i = i - 1`
- `i *= 2` $\iff$ `i = i * 2`
- `i /= 3` $\iff$ `i = i / 3`
- `i **= 4` $\iff$ `i = i ** 4`
- `i %= 2` $\iff$ `i = i % 2`

---

## 3. Editor vs Shell (Console)
- **Shell / REPL:** Valuta ed esegue subito ogni riga digitata, stampando in automatico il valore restituito.
- **Editor (es. Spyder / script `.py`):** Il codice viene salvato su file e per vedere i risultati a schermo è obbligatorio usare esplicitamente la funzione `print()`.

---

## 4. Input e Output (`print`, `input`)

### `print(*oggetti, sep=' ', end='\n')`
Mostra a video i valori specificati:
```python
print("Risultato:", 4 * 3)  # Stampa: Risultato: 12
print(12, 10, 2010, sep='/') # Stampa: 12/10/2010
```

### `input(prompt)`
Mette il programma in attesa dell'input dell'utente dalla console:
```python
nome = input("Come ti chiami? ")
```
> [!IMPORTANT]
> `input()` restituisce **SEMPRE una stringa (`str`)**!
> Anche se l'utente digita `5`, Python riceve `'5'`.
> Se si fa `'5' * 4`, il risultato sarà `'5555'` (ripetizione stringa), NON `20`!

---

## 5. Funzioni di Conversione di Tipo (Casting)
- `int(s)`: Converte una stringa di sole cifre in intero (es. `int('42')` $\rightarrow$ `42`). Se la stringa contiene caratteri non numerici o virgole, lancia `ValueError`.
- `float(s)`: Converte una stringa in numero con virgola (es. `float('3.14')` $\rightarrow$ `3.14`). *Nota:* si usa il punto `.`, non la virgola italiana `,` (`float('3,55')` genera `ValueError`).
- `str(x)`: Converte qualsiasi dato in stringa (indispensabile per concatenare con `+`).
