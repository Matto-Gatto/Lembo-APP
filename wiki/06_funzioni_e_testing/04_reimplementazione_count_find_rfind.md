# Re-implementazione da Zero dei Metodi `count`, `find` e `rfind`

Nel notebook ufficiale del corso viene mostrato come riscrivere da zero le funzioni corrispondenti ai metodi standard delle stringhe, gestendo anche parametri opzionali di slicing (`start` ed `end`).

---

## 1. Funzione `conta(s, c, start=0, end=None)` (Replica di `str.count`)

### Requisiti:
- Riceve la stringa `s`, la sottostringa `c`, e gli indici opzionali `start` ed `end`.
- Conta le occorrenze **non sovrapposte** di `c` nella fetta considerata.
- Se `c == ''`, restituisce `len(s1) + 1` (come fa Python nativamente).

```python
def conta(s, c, start=0, end=None):
    s1 = s[start:end]
    if c == '':
        return len(s1) + 1
    
    num = 0
    i = 0
    # Ci fermiamo quando la finestra rimanente è più corta di c
    while i <= len(s1) - len(c):
        if s1[i : i + len(c)] == c:
            num += 1
            i += len(c)  # Salto in avanti per NON contare sovrapposizioni
        else:
            i += 1
    return num
```

---

## 2. Funzione `trova(s, c, start=0, end=None)` (Replica di `str.find`)

### Requisiti:
- Cerca la **prima occorrenza** di `c` da sinistra.
- Restituisce l'indice relativo alla stringa originaria `s` (quindi sommando `start`).
- Restituisce `-1` se non viene trovata.

```python
def trova(s, c, start=0, end=None):
    s1 = s[start:end]
    # Scansione con finestra di lunghezza len(c)
    for i in range(len(s1) - len(c) + 1):
        if s1[i : i + len(c)] == c:
            return i + start
    return -1
```

---

## 3. Funzione `trovad(s, c, start=0, end=None)` (Replica di `str.rfind`)

### Requisiti:
- Cerca la prima occorrenza di `c` partendo **da destra** (fine stringa).
- Restituisce l'indice assoluto in `s`, oppure `-1` se non trovata.

```python
def trovad(s, c, start=0, end=None):
    s1 = s[start:end]
    # Scansione all'indietro
    for i in range(len(s1) - len(c), -1, -1):
        if s1[i : i + len(c)] == c:
            return i + start
    return -1
```
