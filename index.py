
from random import randint
# armas
nenhuma = {'name':'nenhuma', 'atack' : 0}
faca = {'name':'faca', 'atack' : 0}
bastão = {'name':'bastão', 'atack' : 0}
espada = {'name':'espada', 'atack' : 0}


magias = ['fire', 'wind', 'earth', 'eletric', 'water']
nmagias = magias.__len__() - 1
armas = [nenhuma, faca, bastão, espada]
narmas = armas.__len__() - 1

hp = int()
atk = int()
df = int()
spd = int()
man = int()
mag = int()
magperc = int()
arm = int()
maestria = int()



def ficha():
    print(magias[nmagias])
    print(armas[2])



       # print("dado {} : {}" .format((count+1),randint(1,pointDice)))
ficha()
