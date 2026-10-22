# Esercizi Risolti — Numeri, Operatori e I/O

Questo documento raccoglie tutti gli esercizi proposti nelle dispense ufficiali con codice verificato, spiegazione dettagliata e casi di test.

---

## Esercizio 1 (Operazioni Aritmetiche): Potenza
**Testo:** Scrivere l'istruzione Python che calcola l'espressione $(2^{10})^5$.
```python
risultato = (2**10)**5
# oppure 2**(10*5) = 2**50
print(risultato)  # Output: 1125899906842624
```

---

## Esercizio 2 (Operazioni Aritmetiche): Resto Divisione
**Testo:** Scrivere l'istruzione Python che calcola il resto della divisione di $5^5$ per $2^3$.
```python
resto = (5**5) % (2**3)
print(resto)  # 3125 % 8 = 5
```

---

## Esercizio 3 (Operazioni Aritmetiche con Modulo `math`): Radice
**Testo:** Scrivere l'istruzione Python che calcola $\sqrt{3^2 - 4 \times 2}$.
```python
import math
valore = math.sqrt(3**2 - 4 * 2)
# oppure: (3**2 - 4 * 2) ** 0.5
print(valore)  # Output: 1.0
```

---

## Esercizi 4, 5, 6: Composizione di Stringhe con `+` e `*`
**Esercizio 4:** Generare `'ciao!ciaociao!!'` a partire da `'ciao'` e `'!'`:
```python
s = 'ciao' + '!' + 'ciao' * 2 + '!' * 2
print(s)  # 'ciao!ciaociao!!'
```

**Esercizio 5:** Generare `'ciao!!!ciaociao!!!ciaociaociao!!!'`:
```python
s = ('ciao' + '!' * 3) + ('ciao' * 2 + '!' * 3) + ('ciao' * 3 + '!' * 3)
print(s)
```

**Esercizio 6:** Generare `'ciao! ciao ciao!!ciao ciao ciao!!!'`:
```python
s = 'ciao!' + ' ' + ('ciao ' * 2).strip() + '!!' + ('ciao ' * 3).strip() + '!!!'
# oppure più esplicito:
s = 'ciao!' + ' ' + 'ciao ciao' + '!!' + 'ciao ciao ciao' + '!!!'
print(s)
```

---

## Esercizio Cerchio 1: Area del Cerchio da Input
**Testo:** Chiedere all'utente il raggio del cerchio e stamparne l'area ($A = \pi \cdot r^2$).
```python
import math

r = float(input("Inserisci il raggio del cerchio: "))
area = math.pi * (r ** 2)
print("L'area del cerchio è:", area)
```

---

## Esercizio Cerchio 2: Area e Diametro su Due Righe
**Testo:** Chiedere il raggio e stampare su due righe differenti l'area ed il diametro.
```python
import math

r = float(input("Inserisci il raggio del cerchio: "))
area = math.pi * (r ** 2)
diametro = 2 * r

print("Area:", area)
print("Diametro:", diametro)
```

---

## Esercizio Cilindro 3: Volume del Cilindro
**Testo:** Chiedere raggio e altezza di un cilindro e stampare il volume ($V = \pi \cdot r^2 \cdot h$).
```python
import math

r = float(input("Inserisci il raggio di base: "))
h = float(input("Inserisci l'altezza: "))
volume = math.pi * (r ** 2) * h
print("Il volume del cilindro è:", volume)
```
