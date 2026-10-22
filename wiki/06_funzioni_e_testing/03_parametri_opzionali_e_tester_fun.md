# Parametri Opzionali e il Framework di Test Ufficiale del Corso (`tester_fun`)

## 1. Parametri Opzionali (Valori di Default)
Python consente di assegnare un valore predefinito a uno o più parametri formali:

```python
def incrementa(n, passo=1):
    return n + passo

print(incrementa(5))     # Usa il default: 5 + 1 = 6
print(incrementa(5, 3))  # Sovrascrive il default: 5 + 3 = 8
```

### Regole Sintattiche Fondamentali:
1. **Posizione Obbligatoria:** I parametri opzionali **devono trovarsi sempre per ultimi** nella firma della funzione. Non è ammesso un parametro obbligatorio dopo uno opzionale:
   ```python
   # ERRORE DI SINTASSI:
   def test(a=1, b): ...  # SyntaxError: non-default argument follows default argument
   ```
2. **Chiamata con Argomenti Posizionali vs per Nome (Keyword Arguments):**
   ```python
   def incrementa2(n, passo=1, lunghezza=1):
       return n + passo * lunghezza

   incrementa2(5, 3)             # passo=3, lunghezza=1 (in ordine posizionale)
   incrementa2(5, lunghezza=3)   # passo=1 (default), lunghezza=3 (per nome!)
   ```

---

## 2. Il Framework di Test Ufficiale: `tester_fun`
Nelle esercitazioni e negli esami del Prof. Lembo viene utilizzato il modulo `tester.py` che fornisce la funzione:

```python
tester_fun(funzione_da_testare, lista_argomenti_input, output_atteso)
```

### Implementazione di Riferimento di `tester_fun`:
Per poter testare tutto anche nel nostro ambiente o nella futura web app:

```python
def tester_fun(funzione, input_args, output_atteso):
    nome_fun = funzione.__name__
    print(f"Test funzione: {nome_fun}")
    print(f"Input funzione: {input_args}")
    print(f"Output atteso:\n{output_atteso}")
    
    try:
        output_ottenuto = funzione(*input_args)
        print(f"Output ottenuto:\n{output_ottenuto}")
        if output_ottenuto == output_atteso:
            print("Risultato Test: POSITIVO ✅")
        else:
            print("Risultato Test: FALLITO ❌")
    except Exception as e:
        print(f"ERRORE a runtime durante l'esecuzione: {e} ❌")
    print("*" * 35)
```

### Perché Scrivere i Test Prima del Codice (Test-Driven Development - TDD)?
1. Chiarisce subito i requisiti (tipi di input, tipi di output attesi).
2. Evita di modellare i test sulle debolezze del codice appena scritto.
3. Consente di coprire subito i **casi limite (*corner cases*)**:
   - Stringhe vuote `""`
   - Numeri zero `0` o negativi
   - Liste vuote o singoli elementi
   - Ricerca di elementi assenti o ripetuti
