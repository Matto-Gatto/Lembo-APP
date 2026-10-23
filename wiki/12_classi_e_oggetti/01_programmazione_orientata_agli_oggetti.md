# Programmazione ad Oggetti (OOP) in Python: Classi, Metodi Speciali e Oggetti come Chiavi

## 1. Il Paradigma Orientato agli Oggetti
In Python ogni dato è un **oggetto**, istanza di una certa **classe** (tipo di dato).
Una classe è un modello/blueprint che definisce:
- **Attributi (Stato):** dati e variabili incapsulati nell'oggetto.
- **Metodi (Comportamento):** funzioni che operano sui dati dell'oggetto.

---

## 2. La Definizione di una Classe e il Costruttore `__init__`
Il metodo speciale `__init__` viene invocato automaticamente al momento della creazione di una nuova istanza. Il primo parametro è sempre **`self`**, che rappresenta il riferimento all'oggetto corrente.

### Esempio Ufficiale del Corso: La Classe `Tempo`
```python
class Tempo:
    def __init__(self, Ore=0, Minuti=0, Secondi=0):
        self.Ore = Ore
        self.Minuti = Minuti
        self.Secondi = Secondi
```
Possiamo istanziare oggetti specificando argomenti posizionali o per nome:
```python
t1 = Tempo(11, 10, 0)
t2 = Tempo(Minuti=50)  # Ore=0, Minuti=50, Secondi=0
```

---

## 3. Metodi Speciali di Rappresentazione: `__str__` e `__repr__`
Definiscono come l'oggetto viene convertito in stringa:
- `__str__(self)`: invocato da `print(obj)` e `str(obj)` per una resa leggibile all'utente.
- `__repr__(self)`: invocato quando l'oggetto è dentro una collezione (es. dentro una lista o una tupla) o nella console interattiva.

```python
    def __str__(self):
        return f"{self.Ore}:{self.Minuti}:{self.Secondi}"

    def __repr__(self):
        return str(self)
```

---

## 4. Metodi di Confronto: `__eq__` e `__ne__`
Di default, in Python due oggetti sono considerati uguali (`==`) solo se occupano la stessa locazione di memoria (`id` identico). Per confrontarli in base ai valori dei loro attributi, si ridefinisce `__eq__`:

```python
    def __eq__(self, other):
        if type(self) == type(other) and self.Ore == other.Ore and \
           self.Minuti == other.Minuti and self.Secondi == other.Secondi:
            return True
        return False

    def __ne__(self, other):
        return not (self == other)
```

---

## 5. Hashing e Oggetti come Elementi di `set` e Chiavi di `dict` (`__hash__`)
In Python, per poter inserire un oggetto in un insieme (`set`) o usarlo come chiave in un dizionario (`dict`), l'oggetto deve essere **hashable** (e quindi immutabile):
- Se definiamo `__eq__`, Python disabilita automaticamente l'hash predefinito.
- Dobbiamo definire esplicitamente il metodo speciale **`__hash__(self)`**:

```python
class Squadra:
    def __init__(self, nome):
        self.nome = nome

    def __str__(self):
        return str(self.nome)

    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        return type(self) == type(other) and self.nome == other.nome

    def __hash__(self):
        return hash(self.nome)
```
> [!IMPORTANT]
> **Regola dell'Hash:** Se due oggetti risultano uguali tramite `__eq__`, **devono obbligatoriamente produrre lo stesso valore di hash**.

---

## 6. Composizione di Oggetti (Oggetti che Contengono Oggetti)
Una classe può avere come attributi istanze di altre classi:

```python
class Partita:
    def __init__(self, casa, ospiti, goalCasa=0, goalOspiti=0):
        self.casa = casa        # Oggetto di tipo Squadra
        self.ospiti = ospiti    # Oggetto di tipo Squadra
        self.goalCasa = goalCasa
        self.goalOspiti = goalOspiti
```
