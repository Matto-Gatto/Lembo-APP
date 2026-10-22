# Valori Booleani, Operatori Logici e Leggi di De Morgan

## 1. Il Tipo Booleano (`bool`)
In Python esistono esattamente due costanti booleane:
- `True` (iniziale rigorosamente **maiuscola**)
- `False` (iniziale rigorosamente **maiuscola**)

---

## 2. Operatori di Confronto (Relazionali)
Restituiscono sempre un booleano (`True` o `False`):
- `>` (maggiore), `<` (minore)
- `>=` (maggiore o uguale), `<=` (minore o uguale)
- `==` (uguaglianza logica: verifica se i due valori coincidono)
- `!=` (disuguaglianza logica: verifica se i due valori sono diversi)

> [!NOTE]
> I confronti tra stringhe avvengono in **ordine lessicografico** (basato sui codici numerici Unicode):  
> `"scuola" > "sala"` vale `True` perché ad indice 1 `'c'` (99) $>$ `'a'` (97).  
> Tutte le lettere maiuscole (`'A'`=65) precedono le minuscole (`'a'`=97): `'B' < 'a'` è `True`!

---

## 3. Algebra Booleana: `and`, `or`, `not`

### Tabelle di Verità
- **`and` (Congiunzione):** Vero **solo se entrambi** gli operandi sono `True`.
  - `True and True` $\rightarrow$ `True`
  - `True and False` $\rightarrow$ `False`
  - `False and False` $\rightarrow$ `False`
- **`or` (Disgiunzione):** Vero se **almeno uno** degli operandi è `True`.
  - `True or False` $\rightarrow$ `True`
  - `False or False` $\rightarrow$ `False`
- **`not` (Negazione unaria):** Inverte il valore.
  - `not True` $\rightarrow$ `False`
  - `not False` $\rightarrow$ `True`

---

## 4. Leggi di De Morgan
Fondamentali per semplificare o negare condizioni complesse:
1. `not (A and B)` $\iff$ `(not A) or (not B)`
2. `not (A or B)` $\iff$ `(not A) and (not B)`

### Equivalenze con Operatori di Confronto
- `not (x == y)` $\iff$ `x != y`
- `not (x != y)` $\iff$ `x == y`
- `not (x < y)` $\iff$ `x >= y`
- `not (x <= y)` $\iff$ `x > y`

---

## 5. Ordine di Precedenza degli Operatori
Quando un'espressione contiene più operatori e non ci sono parentesi:
1. **Operatori aritmetici** (`**`, poi `* / // %`, poi `+ -`)
2. **Operatori di confronto** (`==`, `!=`, `<`, `<=`, `>`, `>=`)
3. **`not`**
4. **`and`**
5. **`or`**

*Esempio:*
`True == False or False` $\rightarrow$ viene valutato come `(True == False) or False` $\rightarrow$ `False or False` $\rightarrow$ `False`.
