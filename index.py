# inicio importações
from random import randint
# fim importações
# inicio dados
nenhuma = {'nome':'nenhuma', 'dano' : 0}
faca = {'nome':'faca', 'dano' : 3}
bastão = {'nome':'bastão', 'dano' : 6}
espada = {'nome':'espada', 'dano' : 7}

magias = ['nenhuma', 'fire', 'wind', 'earth', 'eletric', 'water']
nmagias = magias.__len__() - 1
armas = [nenhuma, faca, bastão, espada]
narmas = armas.__len__() - 1
# fim dados
# incio funções
def ficha():
    hp = int(randint(1,100))
    atk = int(randint(1,100))
    df = int(randint(1,100))
    spd = int(randint(1,100))
    man = int(randint(1,100))
    mag = int(randint(0,nmagias))
    magperc = int(randint(1,100))
    arm = int(randint(0,narmas))
    maestria = int(randint(1,100))
    if mag == 0:
        magper = 0
    if arm == 0:
        maestria = 0   
    print(60*'-')
    print('vida:',hp)
    print('Força:',atk)
    print('Defesa:',df)
    print('Velocidade:',spd)
    print('Mana:',man)
    print(60*'-')
    print('Magia:',magias[mag])
    print('Maestria da Magia: {}%'.format(magperc))
    print(60*'-')
    print('arma:',armas[arm])
    print('Maestria da Arma: {}%'.format(maestria))
    print(60*'-')
# fim funções
    # inicio body
rodadas = int(input('Quantas vezes '))
vezes = rodadas
ficha()        
    # fim body  
