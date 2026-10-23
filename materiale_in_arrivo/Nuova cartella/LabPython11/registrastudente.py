FILE = 'studente.txt'

f = open(FILE,'w', encoding = 'UTF-8')
matricola = input("inserire MATRICOLA: ")
cognome = input("inserire COGNOME: ").capitalize()
nome = input("inserire NOME: ").capitalize()
f.write(matricola+'\n'+cognome+'\n'+nome)
f.close()
