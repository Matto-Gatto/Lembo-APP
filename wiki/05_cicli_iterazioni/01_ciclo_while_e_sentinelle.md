# Il Ciclo While, Valori Sentinella e Pattern di Scansione

## 1. Il Concetto di Iterazione
In programmazione, un ciclo (*loop*) permette di ripetere l'esecuzione di un blocco di istruzioni finché una data condizione booleana resta vera.

```python
while condizione:
    istruzione_1
    istruzione_2
```

### Meccanismo di Esecuzione:
1. Viene valutata la `condizione`.
2. Se è `True`, si esegue il corpo del ciclo e si torna al punto 1.
3. Se è `False`, il ciclo termina immediatamente e l'esecuzione prosegue con la prima istruzione all'esterno (dopo l'indentazione).

> [!NOTE]
> Se il blocco del ciclo viene eseguito $k$ volte, la condizione del `while` viene valutata complessivamente **$k + 1$ volte** (l'ultima volta è quella in cui la condizione risulta `False` e causa l'uscita).

---

## 2. Componenti Fondamentali di un Ciclo
Un ciclo ben progettato necessita sempre di 4 elementi:
1. **Inizializzazione** della variabile di controllo prima del ciclo (es. `i = 0`).
2. **Condizione di continuazione** (es. `i < len(s)`).
3. **Elaborazione** del dato (es. `print(s[i])`).
4. **Aggiornamento / Incremento** della variabile verso la terminazione (es. `i += 1`).  
   *Se si dimentica l'incremento, il programma entra in un **ciclo infinito (loop infinito)**.*

---

## 3. Cicli Definiti vs Cicli Indefiniti
- **Ciclo Definito:** Il numero di iterazioni è calcolabile/noto a priori prima di iniziare (es. iterare su una stringa di lunghezza nota `len(s)`).
- **Ciclo Indefinito:** Il numero di iterazioni **non è prevedibile** prima dell'esecuzione perché dipende da eventi a runtime (es. l'utente inserisce dati finché non digita un valore di stop, oppure estrazione casuale fino a trovare un carattere target).

---

## 4. Il Pattern con "Valore Sentinella"
Una tecnica classica: l'utente inserisce elementi uno alla volta; l'inserimento termina quando digita un valore speciale (detto **sentinella**, es. `*` o stringa vuota `""`) che non deve essere elaborato.

### Approccio A: Lettura Fuori e poi in Coda al Ciclo (Consigliato per pulizia)
Si legge una prima volta fuori dal ciclo, e si riesegue la lettura in fondo al corpo del while:
```python
valore = input("Inserisci un intero (* per terminare): ")
while valore != "*":
    # Elaborazione sicura (senza bisogno di if)
    n = int(valore)
    print("Hai inserito:", n)
    valore = input("Inserisci un intero (* per terminare): ")
```

### Approccio B: Lettura Solo Dentro il Ciclo (con variabile sentinella o flag)
```python
finito = False
while not finito:
    valore = input("Inserisci un intero (* per terminare): ")
    if valore == "*":
        finito = True
    else:
        n = int(valore)
        print("Hai inserito:", n)
```

---

## 5. Ripetizione dell'Intero Programma
Pattern molto frequente per consentire all'utente di rieseguire un'operazione:
```python
ancora = 'si'
while ancora.lower() == 'si':
    # Esecuzione del task principale
    n = int(input("Inserisci un numero: "))
    print("Quadrato:", n ** 2)
    ancora = input("Vuoi continuare (si/no)? ")
```
