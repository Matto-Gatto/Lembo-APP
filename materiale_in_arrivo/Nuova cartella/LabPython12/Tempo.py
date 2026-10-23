class Tempo: 

  def __init__(self, Ore=0, Minuti=0, Secondi=0): 
    self.Ore = Ore 
    self.Minuti = Minuti 
    self.Secondi = Secondi 

  def __str__(self): 
    return str(self.Ore) + ":" + \
        str(self.Minuti) + ":" + \
        str(self.Secondi)

  def __repr__(self):
    return str(self)

  def __eq__(self,tempo):
    if type(self)==type(tempo) and self.Ore==tempo.Ore and self.Minuti==tempo.Minuti and self.Secondi==tempo.Secondi:
      return True
    return False

  def __ne__(self,tempo):
    if not self==tempo:
      return True
    return False

  def __lt__(self,tempo):
    if type(self)!=type(tempo):
      return False
    if self.Ore<tempo.Ore:
      return True
    if self.Ore > tempo.Ore: 
      return False
    if self.Minuti<tempo.Minuti:
      return True
    if self.Minuti > tempo.Minuti:
      return False
    if self.Secondi<tempo.Secondi:
      return True
    if self.Secondi > tempo.Secondi: 
      return False   
    return False

  def __le__(self,tempo):
    if type(self)!=type(tempo):
      return False
    if self.Ore<tempo.Ore:
      return True
    if self.Ore > tempo.Ore: 
      return False
    if self.Minuti<tempo.Minuti:
      return True
    if self.Minuti > tempo.Minuti:
      return False
    if self.Secondi<tempo.Secondi:
      return True
    if self.Secondi > tempo.Secondi: 
      return False   
    return True

  def __gt__(self,tempo):
    if type(self)!=type(tempo):
      return False
    if self.Ore>tempo.Ore:
      return True
    if self.Ore<tempo.Ore: 
      return False
    if self.Minuti>tempo.Minuti:
      return True
    if self.Minuti<tempo.Minuti:
      return False
    if self.Secondi>tempo.Secondi:
      return True
    if self.Secondi<tempo.Secondi: 
      return False   
    return False

  def __ge__(self,tempo):
    if type(self)!=type(tempo):
      return False
    if self.Ore>tempo.Ore:
      return True
    if self.Ore<tempo.Ore: 
      return False
    if self.Minuti>tempo.Minuti:
      return True
    if self.Minuti<tempo.Minuti:
      return False
    if self.Secondi>tempo.Secondi:
      return True
    if self.Secondi<tempo.Secondi: 
      return False   
    return True

