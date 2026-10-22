# Espressioni Numeriche, Operatori e Moduli (`math`, `random`)

## 1. Tipi di Dati Numerici Fondamentali
In Python i numeri principali sono:
- **Interi (`int`):** numeri senza parte frazionaria (es. `12`, `-9`, `1`, `0`). In Python gli interi hanno precisione arbitraria (possono essere arbitrariamente grandi senza andare in overflow, es. `(21*5)**(31*4)`).
- **Frazionari / Virgola Mobile (`float`):** numeri con virgola (es. `3.14`, `-45.2`, `1.0`) o in notazione scientifica esponenziale (es. `-42.3e-4` che rappresenta $-42.3 \times 10^{-4}$).

---

## 2. Operatori Aritmetici

| Simbolo | Operazione | Note ed Esempi |
| :---: | :--- | :--- |
| `+` | Somma | `1 + 5` $\rightarrow$ `6`; `1.0 + 5` $\rightarrow$ `6.0` |
| `-` | Sottrazione | `10 - 4` $\rightarrow$ `6` |
| `*` | Moltiplicazione | `4 * 3` $\rightarrow$ `12` |
| `/` | **Divisione reale** | Restituisce **sempre** un `float`! Es. `6 / 2` $\rightarrow$ `3.0`, `2 / 5` $\rightarrow$ `0.4` |
| `//` | **Divisione intera** (*floor division*) | Il più grande intero $\le$ al quoziente reale. Es. `6 // 3` $\rightarrow$ `2`, `2 // 3` $\rightarrow$ `0`, `-2 // 3` $\rightarrow$ `-1` |
| `%` | **Modulo** (resto della divisione) | `7 % 3` $\rightarrow$ `1` |
| `**` | **Elevamento a potenza** | `2 ** 3` $\rightarrow$ `8` |

> [!IMPORTANT]
> - Se almeno un operando di `+`, `-`, `*`, `//`, `%` è `float`, il risultato è `float`.
> - L'operatore `/` produce **sempre** un `float`, anche se i numeri si dividono esattamente (`6 / 2` produce `3.0`, non `3`).

---

## 3. Funzioni Matematiche Predefinite (Built-in)
Non richiedono alcuna importazione:
- `abs(x)`: valore assoluto di `x` (es. `abs(-5)` $\rightarrow$ `5`).
- `round(x)`: arrotonda all'intero più vicino.
- `round(x, n)`: arrotonda `x` a `n` cifre decimali.
- `min(x1, x2, ...)`: restituisce il minimo tra gli argomenti.
- `max(x1, x2, ...)`: restituisce il massimo tra gli argomenti.

---

## 4. Moduli Esterni: `math` e `random`

### Tre modalità di importazione:
1. `import math`: Tutte le funzioni sono accessibili con prefisso `math.<funzione>` (es. `math.sqrt(9)`).
2. `from math import *`: Importa tutto nel namespace corrente (si usa `sqrt(9)` senza prefisso). *Sconsigliato nei programmi complessi per evitare conflitti di nomi.*
3. `from math import sin, sqrt`: Importa selettivamente solo le funzioni necessarie.

### Funzioni Chiave di `math` (restituiscono tutte `float`)
- Goniometriche: `sin(x)`, `cos(x)`, `tan(x)` (angoli in **radianti**!).
- Conversioni: `degrees(rad)` (radianti $\rightarrow$ gradi), `radians(deg)` (gradi $\rightarrow$ radianti).
- Esponenziali e Logaritmi: `exp(x)` ($e^x$), `log(x)` ($\ln x$), `log(x, base)`, `log10(x)`.
- Radici e potenze: `sqrt(x)` ($\sqrt{x}$), `pow(x, y)` ($x^y$).

### Modulo `random`
- `randint(a, b)`: genera un intero casuale $N$ tale che $a \le N \le b$ (estremi inclusi!).
  ```python
  from random import randint
  segreto = randint(1, 100)
  ```
