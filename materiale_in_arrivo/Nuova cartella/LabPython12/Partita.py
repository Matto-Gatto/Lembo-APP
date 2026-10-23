class Partita: 

  def __init__(self, casa, ospiti, goalCasa=0, goalOspiti=0): 
    self.casa = casa
    self.ospiti = ospiti
    self.goalCasa = goalCasa
    self.goalOspiti = goalOspiti

  def __str__(self): 
    return str(self.casa) + "-" + \
        str(self.ospiti) + " " + \
        str(self.goalCasa)+ ":" +str(self.goalOspiti)

  def __repr__(self):
    return str(self)

  def __eq__(self,partita):
    if type(self)==type(partita) and self.casa==partita.casa and self.ospiti==partita.ospiti:
      return True
    return False

  def __ne__(self,partita):
    if not self==partita:
      return True
    return False
