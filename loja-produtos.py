import os

play = {}
xbo = {}
nin = {}

def menu(x): 
    s = 0
    while s == 0:
        print("\n\n========= Menu =========\n[1] Consoles\n[2] Jogos\n[3] Sair")
        x = int(input("Escolha uma opção: "))

        if x == 1:
            consoles(clientes)
        elif x == 2:
            jogos(clientes)
        elif x == 3:
            s = 1
        else:
            print("Opção inválida")

def consoles(clientes):
    while True:
        print("\n\n========= Consoles =========")
        print("[1] Playstation")
        print("[2] Xbox")
        print("[3] Nintendo Switch")
        print("[4] Voltar")
        c = int(input("Escolha o console desejado: "))
        if c == 1:
            playstation()
        elif c == 2:
            xbox()
        elif c == 3:
            nintendo()
        elif c == 4:
            break
        else:
            print("Opção inválida")

def playstation():
    play = []

    videogames = {
        "Playstation 1": 299.90,
        "Playstation 2": 558.00,
        "Playstation 3": 1090.00,
        "Playstation 4": 2099.00,
        "Playstation 5": 4899.99
    }

    videogames = {
        "Playstation 1": 299.90,
        "Playstation 2": 558.00,
        "Playstation 3": 1090.00,
        "Playstation 4": 2099.00,
        "Playstation 5": 4899.99
    }

    print("\n\n========= Playstation =========")
    print("Produtos disponíveis:")
    for videogame, preco in videogames.items():
        print(f"- {videogame}: R${preco:.2f}")
    escolha = input("Escolha o produto desejado: ")
    if escolha in videogames:
        preco = videogames[escolha]
        print(f"O preço do(a) {escolha} é R${preco:.2f}")
    else:
        print("Produto não encontrado")
        return
    play.append(escolha)
    playstation[escolha] = play

    print("Produtos dísponiveis:")
    for videogame, preco in videogames.items():
        print(f"- {videogame}")
    
    escolha = input("Escolha o produto desejado: ")

    if escolha in videogames:
        preco = videogames[escolha]
        print(f"O preço do(a) {escolha} é R${preco:.2f}")
    else:
        print("Produto não encontrado")
        return
    play.append(escolha)
    playstation[escolha] = play

def xbox():
    xbo = []

    videobox = {
        "1": "Xbox primeiro",
        "2": "Xbox 360",
        "3": "Xbox One",
        "4": "Xbox Series S",
        "5": "Xbox Series X",
    }

    videobox = {
        "Xbox primeiro": 200.00,
        "Xbox 360": 699.99,
        "Xbox One": 1399.99,
        "Xbox Series S": 2100.00,
        "Xbox Series X": 3450.00,
    }
    print("\n\n========= Xbox =========")
    print("Produtos disponíveis:")
    for videobox, preco in videobox.items():
        print(f"- {videobox}: R${preco:.2f}")
    escolha = input("Escolha o produto desejado: ")
    if escolha in videobox:
        preco = videobox[escolha]
        print(f"O preço do(a) {escolha} é R${preco:.2f}")
    else:
        print("Produto não encontrado")
        return
    xbo.append(escolha)
    xbox[escolha] = xbo

def nintendo():
    nin = []
    ningames = {
        "Nintendo Wii": 599.99,
        "Nintendo Wii u": 1399.99,
        "Nintendo Switch": 2299.99
    }
    print("\n\n========= Nintendo =========")
    print("Produtos disponíveis: ")
    for ningames, preco in ningames.items():
        print(f"- {ningames}: R${preco:.2f}")
        escolha = input("Escolha o produto desejado: ")
    if escolha in ningames:
        preco = ningames[escolha]
        print(f"O preço do(a) {escolha} é R${preco:.2f}")
    else:
        print("Produto não encontrado")
        return
    nin.append(escolha)
    nintendo[escolha] = nin

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
    print("Produtos disponíveis:")
    for jogo, preco in jogospreco.items():
        print(f"- {jogo}: R${preco:.2f}")
    
    escolha = input("Escolha o produto desejado: ")

    if escolha in jogospreco:
        preco = jogospreco[escolha]
        print(f"O preço do(a) {jogos[escolha]} é R${preco:.2f}")
    else:
        print("Produto não encontrado")
        return
    
    jg.append(jogos[escolha])
    clientes[escolha] = jg 

#//////////////////////////////////////////////////////////////////////////////////////

clientes = {}
s = 0
while s == 0:
    op = int(input("Produtos da loja\n[1] Consoles\n[2] Jogos\n[3] Sair\nInforme o que deseja:\n"))
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
        print("Opção inválida")
        os.system("pause")

os.system("pause")