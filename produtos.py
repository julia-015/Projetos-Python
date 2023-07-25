import os

s = 0

play = {}
xbo = {}
nin = {}
ps = 0

jg = {}

ps1 = {}
xbo1 = {}
nin1 = {}

def menu(x): #menu para selecionar o que dejesa
    if x == 1:
        consoles(clientes)
        s = 0
    elif x == 2:
        jogos(clientes)
        s = 0
    elif x == 3:
        s = 1
    else:
        print("Opção invalida")
        s = 0

#///////////////////////////////////////////////////////////////////////////////////////////

def consoles(clientes): #aqui começa o menu de consoles
    c = int(input("[1] Playstation\n[2] Xbox\n[3] Nintendo Switch\nEscolha o console desejado:"))
    if c == 1: #se ele quiser playstation, vai apertar o 1, e vai aparecer apenas os videogames playstation
        playstation(ps)
    elif c == 2:
        xbox(xbo1)
    elif c == 3:
        nintendo(nin1)
    else:
        print("Opção invalida")

def playstation(ps):
    play = [] 
    videogames = {
        "1": "Playstation 1",
        "2": "Playstation 2",
        "3": "Playstation 3",
        "4": "Playstation 4",
        "5": "Playstation 5",
    }

    videogames = {
        "Playstation 1": 299.90,
        "Playstation 2": 558.00,
        "Playstation 3": 1090.00,
        "Playstation 4": 2099.00,
        "Playstation 5": 4899.99
    }
    print("Produtos dísponiveis:")
    for videogame, preco in videogames.items():
        print(f"- {videogame}")
    
    escolha = input("Escolha o produto desejado: ")

    if escolha in videogames:
        preco = videogames[escolha]
        print(f"O preço do(a) {escolha} é R${preco:}")
    else:
        print("Produto não encontrado")
    play.append(escolha)
    ps[escolha] = play


def xbox(xbo1):
    xbo = []
    videobox = {
        "1": "Xbox primeiro",
        "2": "Xbox 360",
        "3": "Xbox One",
        "4": "Xbox Series S",
        "5": "Xbox Series X"
    }
    xboxpreco = {
        "Xbox primeiro": 200,
        "Xbox 360": 699.99,
        "Xbox One": 1399.99,
        "Xbox Series S": 2100.00,
        "Xbox Series X": 3450.00,
    }
    print("Produtos dísponiveis:")
    for videobox, preco in xboxpreco.items():
        print(f"- {videobox}")
    
    escolha = input("Escolha o produto desejado: ")

    if escolha in xboxpreco:
        preco = xboxpreco[escolha]
        print(f"O preço do(a) {escolha} é R${preco:}")
    else:
        print("Produto não encontrado")
    xbo.append(escolha)
    xbo1[escolha] = xbo

def nintendo(nin1):
    nin = []
    ningames = {
        "1": "Nintendo Wii",
        "2": "Nintendo Wii u",
        "3": "Nintendo Switch",
    }
    ninpreco = {
        "Nintendo Wii": 599.99,
        "Nintendo Wii u": 1399.99,
        "Nintendo Switch": 2299.99
    }
    print("Produtos dísponiveis:")
    for ningames, preco in ninpreco.items():
        print(f"- {ningames}")
    
    escolha = input("Escolha o produto desejado: ")

    if escolha in ninpreco:
        preco = ninpreco[escolha]
        print(f"O preço do(a) {escolha} é R${preco:}")
    else:
        print("Produto não encontrado")
    nin.append(escolha)
    nin1[escolha] = nin

#/////////////////////////////////////////////////////////////////////////////////////////////

def jogos(clientes):
    jg = []
    jogos = {
        "1": "ResidentEvil 4",
        "2": "The last of us",
        "3": "God of War Ragnarok",
        "4": "Forza Horizon 5",
        "5": "Gears of war 4",
        "6": "Halo infinite",
        "7": "Super Mario 3D World",
        "8": "Zelda breath of the wild"
    }
    jogospreco = {
        "ResidentEvil 4": 250.00,
        "The last of us": 90.00,
        "God of War Ragnarok": 250.00,
        "Forza Horizon 5": 250.00,
        "Gears of war 4": 100.00,
        "Halo infinite": 250.00,
        "Super Mario 3D World": 299.99,
        "Zelda breath of the wild": 324.99
    }
    print("Produtos dísponiveis:")
    for jogos, preco in jogospreco.items():
        print(f"- {jogos}")
    
    escolha = input("Escolha o produto desejado: ")

    if escolha in jogospreco:
        preco = jogospreco[escolha]
        print(f"O preço do(a) {escolha} é R${preco:}")
    else:
        print("Produto não encontrado")
    jg.append(escolha)
    clientes[escolha] = jg 

#//////////////////////////////////////////////////////////////////////////////////////

clientes = {}
while s == 0:
    op = int(input("Produtos da loja\n[1] Consoles\n[2] Jogos\n[3] Sair\nInforme o que deseja:\n"))
    menu(op)
    if op == 1:
        os.system("cls")
        consoles(clientes)
        os.system("pause")
        os.system("cls")
    elif op == 2:
        os.system("cls")
        jogos(clientes)
        os.system("pause")
        os.system("cls")
    elif op == 3:
        os.system("cls")
        s = 1
        os.system("cls")
    else:
        print("Opção invalida")

os.system("pause")