# inicio importações

from random import randint

# fim importações

# inicio dados

maestria = 0

nenhuma = {'nome':'nenhuma', 'dano' : 0, 'defesa': 0, 'critico': 0, }
faca = {'nome':'faca', 'dano' : 2, 'defesa': 1, 'critico': 6, }
bastão = {'nome':'bastão', 'dano' : 3, 'defesa': 5, 'critico': 0, }
espada = {'nome':'espada', 'dano' : 7, 'defesa': 6, 'critico': 10, }
arco = {'nome':'arco', 'dano' : 3, 'defesa': 1, 'critico': 10, }
machado = {'nome':'machado', 'dano' : 10, 'defesa': 4, 'critico': 9, }
martelo = {'nome':'martelo', 'dano' : 7, 'defesa': 4, 'critico': 1, }
lança = {'nome':'lança', 'dano' : 6, 'defesa': 5, 'critico': 7,}
escudo = {'nome':'escudo', 'dano' : 2, 'defesa': 50, 'critico': 0, }
bengala = {'nome':'bengala', 'dano' : 1, 'defesa': 3, 'critico': 0, }
manopla = {'nome':'manopla', 'dano' : 2, 'defesa': 10, 'critico': 0, }
chicote = {'nome':'chicote', 'dano' : 2, 'defesa': -90, 'critico': 1, }
canivete = {'nome':'canivete', 'dano' : 3, 'defesa': 0, 'critico': 5, }
machete =  {'nome':'machete', 'dano' : 4, 'defesa': 6, 'critico': 6, }
pá = {'nome':'pá', 'dano' : 3, 'defesa': 4, 'critico': 0, }
foice = {'nome':'foice', 'dano' : 6, 'defesa': 5, 'critico': 6, }
trident = {'nome':'trident', 'dano' : 6, 'defesa': 6, 'critico': 6, }
marreta = {'nome':'marreta', 'dano' : 8, 'defesa': 5, 'critico': 1, }
anel = {'nome':'anel de poder', 'dano' : maestria, 'defesa': maestria, 'critico': 0, }

armas = [nenhuma, faca, bastão, espada, arco, machado, martelo, lança, escudo, bengala, manopla, chicote, canivete, machete, pá, foice, marreta  ]
narmas = armas.__len__() - 1

magias = ['nenhuma', 'fire', 'wind', 'earth', 'eletric', 'water']
nmagias = magias.__len__() - 1



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
    print(62*'-')

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
