# Raccolta Completa Compiti d'Esame con Soluzioni Ufficiali

Questo documento raccoglie tutti i compiti d'esame presenti nell'archivio del docente con codice ufficiale verificato.

---

## 📅 Compito 1 — Varianti A, B, C, D

### Variante A
- **A_Ex1(s1, s2): Prefisso comune più lungo**
  ```python
  def A_Ex1(s1, s2):
      i = 0
      ris = ''
      while i < min(len(s1), len(s2)) and s1[i] == s2[i]:
          ris += s1[i]
          i += 1
      return ris
  ```
- **A_Ex2(l): Rimozione stringhe con massimo numero di maiuscole (in-place)**
  ```python
  def A_Ex2(l):
      massimo = 0
      lista = []
      for e in l:
          cont = sum(1 for c in e if c.isupper())
          if cont > massimo:
              massimo = cont
              lista = [e]
          elif cont == massimo:
              lista.append(e)
      i = 0
      while i < len(l):
          if l[i] in lista:
              l.remove(l[i])
          else:
              i += 1
      return l
  ```
- **A_Ex3(file): Collezionisti d'Arte con più dipinti**
  *(File CSV: `Acquirente,Venditore,Pittore`. Se venditore è vuoto è acquisto primario; se vende ha il quadro, si toglie dal venditore e si dà all'acquirente. Restituisce la lista ordinata dei collezionisti che possiedono il maggior numero di quadri).*
  ```python
  def A_Ex3(file):
      with open(file, 'r', encoding='UTF-8') as f:
          f.readline()  # header
          d = {}
          for riga in f:
              lista = riga.strip().split(',')
              acquista, vende, pittore = lista[0], lista[1], lista[2]
              if acquista not in d: d[acquista] = []
              if vende == '':
                  d[acquista].append(pittore)
              else:
                  if vende in d and pittore in d[vende]:
                      d[vende].remove(pittore)
                      d[acquista].append(pittore)
                      
      if len(d) == 0: return []
      massimo = max(len(quadri) for quadri in d.values())
      ris = [acq for acq, quadri in d.items() if len(quadri) == massimo]
      ris.sort()
      return ris
  ```

---

### Variante B
- **B_Ex1(s1, s2): Lunghezza del suffisso comune**
  ```python
  def B_Ex1(s1, s2):
      i = -1
      ris = 0
      while i >= -min(len(s1), len(s2)) and s1[i] == s2[i]:
          ris += 1
          i -= 1
      return ris
  ```
- **B_Ex2(l): Duplicazione stringhe con massimo numero di minuscole**
  ```python
  def B_Ex2(l):
      massimo = 0
      lista = []
      for e in l:
          cont = sum(1 for c in e if c.islower())
          if cont > massimo:
              massimo = cont
              lista = [e]
          elif cont == massimo:
              lista.append(e)
      i = 0
      while i < len(l):
          if l[i] in lista:
              l.insert(i + 1, l[i])
              i += 2
          else:
              i += 1
      return l
  ```
- **B_Ex3(file): Stazioni ferroviarie e treni presenti**
  *(File CSV: `Treno,Stazione,Evento`. `A` = arrivo in stazione, `P` = partenza da stazione. Restituisce `{stazione: lista_ordinata_treni_attualmente_fermi}`).*
  ```python
  def B_Ex3(file):
      d = {}
      with open(file, 'r', encoding='UTF-8') as f:
          for riga in f:
              treno, stazione, ap = [x.strip() for x in riga.strip().split(',')]
              if stazione not in d:
                  d[stazione] = []
              if ap == 'P':
                  if treno in d[stazione]:
                      d[stazione].remove(treno)
              else:
                  if treno not in d[stazione]:
                      d[stazione].append(treno)
                      d[stazione].sort()
      return d
  ```

---

## 📅 Compito 2 — Esercizi Salienti
- **A_Ex1(l): Caratteri con parità indici riga/colonna (`i % 2 == j % 2`)**
  ```python
  def A_Ex1(l):
      ris = []
      for i in range(len(l)):
          for j in range(len(l[i])):
              if (i % 2 == j % 2) and l[i][j] not in ris:
                  ris.append(l[i][j])
      ris.sort()
      return ris
  ```
- **A_Ex2(file): Consonanti più frequenti per riga escluse le vocali**
  ```python
  def A_Ex2(file):
      esclusi = set('aeiouAEIOU \n\t')
      d = {}
      with open(file, 'r', encoding='UTF-8') as f:
          linea = 1
          for riga in f:
              massimo = 0
              for c in riga:
                  if c not in esclusi and riga.count(c) > massimo:
                      massimo = riga.count(c)
              for c in riga:
                  if c not in esclusi and riga.count(c) == massimo and massimo > 0:
                      d.setdefault(c, []).append(linea)
              linea += 1
      return d
  ```

---

## 📅 Compito 3 — Esercizi Salienti
- **A_Ex1(s1, s2): Verifica se $s_1$ è la speculare di $s_2$**
  ```python
  def A_Ex1(s1, s2):
      return s1 == s2[::-1]
  ```
- **A_Ex2(file, n): Lettere dell'alfabeto presenti almeno $n$ volte per riga**
  ```python
  def A_Ex2(file, n):
      lettere = 'abcdefghijklmnopqrstuvwxyz'
      d = {}
      with open(file, 'r', encoding='UTF-8') as f:
          linea = 1
          for riga in f:
              for l in lettere:
                  if riga.lower().count(l) >= n:
                      d.setdefault(l, []).append(linea)
              linea += 1
      return d
  ```

---

## 📅 Compito 4 — Esercizi Salienti
- **A_Ex1(s1, s2): Distanza tra due stringhe (differenza lunghezze + caratteri discordanti)**
  ```python
  def A_Ex1(s1, s2):
      distanza = abs(len(s1) - len(s2))
      m = min(len(s1), len(s2))
      for i in range(m):
          if s1[i] != s2[i]:
              distanza += 1
      return distanza
  ```
- **A_Ex2(file): Mappa dei numeri che precedono ciascun numero**
  ```python
  def A_Ex2(file):
      d = {}
      with open(file, 'r', encoding='UTF-8') as f:
          numeri = [int(x) for x in f.read().split()]
      for i in range(1, len(numeri)):
          succ = numeri[i]
          prec = numeri[i - 1]
          if succ not in d:
              d[succ] = [prec]
          elif prec not in d[succ]:
              d[succ].append(prec)
      if len(numeri) > 0 and numeri[0] not in d:
          d[numeri[0]] = []
      return d
  ```

---

## 📅 Compito 5, 6, 7 — Gestione Transazioni, Domini e Classifiche
- **Compito 6 - Ex2: Estrazione domini email di 2° livello**
  ```python
  def Ex2(file):
      d = {}
      with open(file, 'r', encoding='UTF-8') as f:
          parole = f.read().split()
      for m in parole:
          if m.count('@') == 1:
              at = m.find('@')
              dominio_completo = m[at + 1:]
              parti = dominio_completo.split('.')
              if len(parti) >= 2:
                  dominio = parti[-2] + '.' + parti[-1]
                  d[dominio] = d.get(dominio, 0) + 1
      return d
  ```
- **Compito 7 - Ex3: Bonifici e trasferimenti tra conti bancari con controllo capienza**
  ```python
  def A_Ex3(file_utenti, file_trasferimenti):
      saldi = {}
      with open(file_utenti, 'r', encoding='UTF-8') as f:
          f.readline()
          for riga in f:
              user, saldo = riga.strip().split(',')
              saldi[user] = int(saldo)
              
      with open(file_trasferimenti, 'r', encoding='UTF-8') as f:
          f.readline()
          for riga in f:
              mittente, destinatario, importo = riga.strip().split(',')
              importo = int(importo)
              # Il trasferimento avviene solo se il mittente ha fondi sufficienti
              if saldi.get(mittente, 0) >= importo:
                  saldi[mittente] -= importo
                  saldi[destinatario] = saldi.get(destinatario, 0) + importo
                  
      return saldi
  ```
