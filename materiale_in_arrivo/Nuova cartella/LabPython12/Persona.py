class Persona: 

  def __init__(self,nome,annoNascita): 
    self.nome = nome
    self.annoNascita = annoNascita

  def __str__(self): 
    return '('+str(self.nome)+' ,'+str(self.annoNascita)+')'

  def __repr__(self):
    return str(self)

  def __eq__(self,pers):
    if type(self)==type(pers) and self.nome==pers.nome and self.annoNascita==pers.annoNascita:
      return True
    return False

  def __ne__(self,pers):
    if not self==pers:
      return True
    return False

