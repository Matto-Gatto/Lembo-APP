# Istruzioni `break`, `continue`, Confronto While/For e Disegno di Figure

## 1. L'Istruzione `break`
- **Scopo:** Interrompe **immediatamente** l'esecuzione del ciclo in cui si trova, trasferendo il controllo alla prima istruzione che segue il ciclo.
- Di norma è inserita all'interno di un `if` quando si è raggiunto il risultato cercato (es. trovato un divisore, trovato un elemento cercato), evitando iterazioni inutili.

### Esempio Tipico d'Esame: Test di Primalità con `break`
Verifica se un numero naturale $n > 1$ è primo:
```python
n = int(input("Inserisci n > 1: "))
is_primo = True

# Basta cercare divisori fino a n // 2 (o sqrt(n))
for i in range(2, (n // 2) + 1):
    if n % i == 0:
        is_primo = False
        break  # Divisore trovato! Inutile continuare

if n > 1 and is_primo:
    print(n, "è primo")
else:
    print(n, "NON è primo")
```

---

## 2. L'Istruzione `continue`
- **Scopo:** Salta il resto del corpo dell'iterazione **corrente** e passa subito alla successiva (rivalutando la condizione nel `while` o prelevando il prossimo elemento nel `for`).

### Esempio: Stampare i numeri da 9 a 0 saltando il 5
```python
for var in range(9, -1, -1):
    if var == 5:
        continue  # Salta la stampa del 5
    print(var)
```

---

## 3. Guida alla Scelta: `while` oppure `for`?

| Situazione | Ciclo Consigliato | Motivazione |
| :--- | :---: | :--- |
| Si scorre una sequenza di elementi noti a priori (stringa, lista, intervallo `range`) | **`for`** | Sintassi più concisa, nessuna gestione manuale di indici e incrementi. |
| Il numero di iterazioni dipende da un evento esterno (input utente, valore sentinella) | **`while`** | Ciclo indefinito: impossibile stabilire in anticipo quante volte iterare. |
| L'indice deve fare salti variabili non uniformi o dipendenti dal contenuto | **`while`** | Flessibilità totale nell'aggiornamento della variabile di controllo. |
| La sequenza o collezione viene modificata durante l'iterazione stessa | **`while`** | Un `for` rischia salti o errori se la collezione cambia lunghezza. |

---

## 4. Disegno di Figure Geometriche con Caratteri

### A. Quadrato Pieno di Lato $L$:
```python
l = int(input("Lato: "))
# Soluzione con cicli annidati
for i in range(l):
    for j in range(l):
        print("*", end='')
    print()

# Soluzione compatta con operatori di stringa
# for i in range(l):
#     print("*" * l)
```

### B. Triangolo Rettangolo Isoscele di Cateto $C$:
```python
c = int(input("Cateto: "))
for i in range(c):
    print("*" * (i + 1))
```
