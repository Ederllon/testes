# inicio importações

from random import randint

# fim importações

# inicio dados                                                                                       

nenhuma = {'nome':'nenhuma', 'dano' : 0, 'defesa': 0, 'critico': 0, }
faca = {'nome':'faca', 'dano' : 2, 'defesa': 1, 'critico': 6, }
bastão = {'nome':'bastão', 'dano' : 3, 'defesa': 5, 'critico': 0, }
espada = {'nome':'espada', 'dano' : 7, 'defesa': 6, 'critico': 10, }
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



magias = ['nenhuma', 'fire', 'wind', 'earth', 'eletric', 'water']
nmagias = magias.__len__() - 1



# fim dados

# incio funções

def ficha(x):
    hp = int(randint(1,100))
    atk = int(randint(1,100))
    df = int(randint(1,100))
    spd = int(randint(1,100))
    car = int(randint(1,100))
    man = int(randint(1,100))
    magperc = int(randint(1,100))
    maestria = int(randint(1,100))
    luck = int(randint(1,100))
    prec = int(randint(1,100))

# inicio dados com adicionaveis     

    anel = {'nome':'anel do poder', 'dano' : magperc, 'defesa': man, 'critico': maestria, }
    arco = {'nome':'arco', 'dano' : 3, 'defesa': 1, 'critico': prec, }
    cajado = {'nome':'cajado', 'dano' : int((magperc + maestria)/2), 'defesa': man, 'critico': maestria, }
    anel_de_energia = {'nome':'anel de energia', 'dano' : man, 'defesa': man, 'critico': man, }
    sai = {'nome':'sai', 'dano' : 2, 'defesa': 2, 'critico': spd, }
    soco = {'nome':'soco inglês', 'dano' : atk , 'defesa': df-30, 'critico': -1 }
    luva = {'nom':'luvas', 'dano' : 1, 'defesa': 1, 'critico': atk-50,}
    pedra = {'nome':'pedra', 'dano' : atk-prec, 'defesa': 0, 'critico': prec, }

# fim dados com adicionaveis
    
    # inicio dados insert 
    armas = [nenhuma, faca, bastão, sai,pedra, luva, cajado, espada, arco, machado, martelo, soco, lança, escudo, bengala, manopla, chicote, canivete, machete, pá, foice, marreta , anel, anel_de_energia]
    narmas = armas.__len__() - 1
    # fim dados insert
    mag = int(randint(0,nmagias))
    arm = int(randint(0,narmas))

    if mag == 0:
        magperc = 0
    if arm == 0:
        maestria = 0   
      

    print('Ficha: #{} | Média De Poder: {}'.format(x,  int((hp+atk+df+spd+car+man+maestria+magperc+luck+prec)/10)))
    print('Vida:',hp)
    print('Força:',atk)
    print('Defesa:',df)
    print('Velocidade:',spd)
    print('Carisma:', car)
    print('Precisão: ',prec )
    print('Sorte: ', luck)
    print('Mana:',man)
    print('Magia:',magias[mag])
    print('Maestria da Magia: {}%'.format(magperc))
    print('Arma:',armas[arm])
    print('Maestria da Arma: {}%'.format(maestria))
    print(62*'-')

# fim funções
    
# inicio body
    
while True:

    print('')
    rodadas = int(input('Quantas fichas irão ser criadas? '))
    print('')
    vezes = rodadas
    
    for count in range(0,vezes):
        ficha(count+1)     

    retry = str(input('Deseja finalizar o programa? '))    
    if retry in  ['s']:
        print('')
        print('Programa finalizado! ')
        print('')
        break


# fim body 
