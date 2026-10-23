class Squadra: 

  def __init__(self, nome): 
    self.nome = nome 

  def __str__(self): 
    return str(self.nome)

  def __repr__(self):
    return str(self)

  def __eq__(self,squadra):
    if type(self)==type(squadra) and self.nome==squadra.nome:
      return True
    return False

  def __ne__(self,squadra):
    if not self==squadra:
      return True
    return False

  def __hash__(self):
    return hash(self.nome)

# Nel metodo __hash__ definiamo come calcolare l'hash per un data Squadra
# utilizziamo l'hash dell'attributo 'nome'.
# L'hash è una funzione che restituisce un intero per un dato oggetto,
# rispettando la seguente regola: Due oggetti che sono uguali
# devono avere anche lo stesso valore hash, ma il contrario non
# è necessariamente vero. Noi qui usiamo l'hash del campo nome
# e usiamo questo come hash dell'oggetto squadra che ha quel nome
# NOTA: la definizione del metodo __hash__ rende l'oggetto IMMUTABILE
