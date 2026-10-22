# Stringhe in Python: Caratteri di Escape, Funzioni e Metodi Built-in

## 1. Definizione e Delimitatori
Una stringa (`str`) è una sequenza immutabile e ordinata di caratteri Unicode.
Può essere delimitata da:
- Singoli apici: `'ciao'`
- Doppi apici: `"ciao"`
- Se all'interno compare l'apostrofo `'`, si usano i doppi apici all'esterno (`"l'amico"`), o la sequenza di escape (`'l\'amico'`).

---

## 2. Caratteri Speciali (Escape Characters)
Preceduti da `\` (backslash):
- `\n`: Newline (a capo)
- `\t`: Tabulazione (spazio orizzontale)
- `\b`: Backspace (cancella il carattere precedente)
- `\'`: Inserisce un apice singolo letterale
- `\"`: Inserisce un apice doppio letterale
- `\\`: Inserisce un backslash letterale
- `\` a fine riga: Indicatore di continuazione del codice alla riga successiva (non deve esserci nessuno spazio dopo).

---

## 3. Funzioni di Base e Tabella Unicode
- `len(s)`: restituisce la lunghezza (numero di caratteri). I caratteri speciali (come `\n` o `\t`) contano come **1 singolo carattere**. Stringa vuota `len('')` restituisce `0`.
- `ord(c)`: dato un singolo carattere, restituisce il suo codice numerico intero nella tabella Unicode (es. `ord('a')` $\rightarrow$ `97`, `ord('A')` $\rightarrow$ `65`).
- `chr(codice)`: operazione inversa di `ord()`. Dato un intero, restituisce il carattere corrispondente (es. `chr(97)` $\rightarrow$ `'a'`). La tabella supporta fino a `0x10FFFF` (1.114.111).

---

## 4. Metodi Principali delle Stringhe

> [!NOTE]
> I metodi si invocano con la sintassi `stringa.metodo()`. Ricorda: le stringhe sono **immutabili**, quindi nessun metodo modifica la stringa originale, ma ne restituisce sempre una nuova!

| Metodo | Descrizione | Esempio |
| :--- | :--- | :--- |
| `s.lower()` | Converte tutti i caratteri in minuscolo | `'CIAO'.lower()` $\rightarrow$ `'ciao'` |
| `s.upper()` | Converte tutti i caratteri in maiuscolo | `'ciao'.upper()` $\rightarrow$ `'CIAO'` |
| `s.strip()` | Rimuove spazi, `\t`, `\n` all'inizio e alla fine | `'  ciao \n'.strip()` $\rightarrow$ `'ciao'` |
| `s.count(sub)` | Conta le occorrenze **non sovrapposte** di `sub` | `'lololo'.count('lolo')` $\rightarrow$ `1` |
| `s.find(sub[, start])` | Restituisce l'indice della **prima occorrenza** di `sub` da sinistra. Restituisce `-1` se non trovato. | `'palla'.find('a')` $\rightarrow$ `1`, `'palla'.find('z')` $\rightarrow$ `-1` |
| `s.rfind(sub[, start])` | Come `find`, ma cerca partendo da destra (*right find*) | `'palla'.rfind('a')` $\rightarrow$ `4` |
| `s.replace(old, new[, count])` | Sostituisce le occorrenze di `old` con `new`. Con `count` si limita il numero di sostituzioni da sinistra. | `'pippo'.replace('p', 'k', 1)` $\rightarrow$ `'kippo'` |
| `str(x)` | Converte qualsiasi tipo in stringa | `str(10)` $\rightarrow$ `'10'` |

### Attenzione a `count()` su sottostringhe sovrapposte
`count()` consuma i caratteri da sinistra verso destra senza sovrapposizioni:
In `'lololo'`, la sottostringa `'lolo'` compare all'indice 0-3. I caratteri rimanenti sono `'lo'`, quindi il conteggio finale è `1` (non `2`!).
