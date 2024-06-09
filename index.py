# inicio importações
from random import randint
# fim importações
# inicio dados
nenhuma = {'nome':'nenhuma', 'dano' : 0, 'defesa': -100,}
faca = {'nome':'faca', 'dano' : 3, 'defesa': 0,}
bastão = {'nome':'bastão', 'dano' : 6, 'defesa': 0,}
espada = {'nome':'espada', 'dano' : 7, 'defesa': 0,}

magias = ['nenhuma', 'fire', 'wind', 'earth', 'eletric', 'water']
nmagias = magias.__len__() - 1
armas = [nenhuma, faca, bastão, espada]
narmas = armas.__len__() - 1
# fim dados
# incio funções
def ficha(x):
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
      

    print('Número da ficha: #{}'.format(x))  
    print('vida:',hp)
    print('Força:',atk)
    print('Defesa:',df)
    print('Velocidade:',spd)
    print('Mana:',man)
    print('Magia:',magias[mag])
    print('Maestria da Magia: {}%'.format(magperc))
    print('arma:',armas[arm])
    print('Maestria da Arma: {}%'.format(maestria))
    print(60*'-')
# fim funções
# inicio body
while True:

    print('')
    rodadas = int(input('Quantas fichas irão ser criadas? '))
    print('')
    vezes = rodadas
    whilecount = 0

    while vezes > 0:
    
        ficha(vezes)     
        vezes = vezes -1

    retry = str(input('Deseja finalizar o programa? '))    
    if retry in  ['s']:
        print('')
        print('Programa finalizado! ')
        print('')
        break


# fim body 
