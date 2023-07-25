import os

#Variáveis
s = 0

consoles1 = 0
jogo1 = 0

#colchetes "[]" são usados para criar uma lista 
# que é uma estrutura de dados que pode conter vários itens. 

Lista_playstation = []
lista_xbox = []
lista_nintendo = []

#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

#as chaves "{}" são usadas para criar um dicionário 
# que é uma estrutura de dados que permite armazenar valores associados a chaves únicas.

dicionário_jogos = {}
dicionário_playstation = {}
dicionário_Xbox = {}
dicionário_nintendo = {}

#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#Menu Utilizando o def para mante-lo em uma caixa 
# sendo assim as alterações feitas no def de menu não afetarão nenhuma outra parte do código

def menu(x): #menu para selecionar o que deseja


    if x == 1:  #se sua escolha for "1" entrará no menu de Consoles
        os.system("cls")
        consoles()
        s = 0
    elif x == 2:   #se sua escolha for "2" entrará no menu de jogos
        os.system("cls")
        jogos()
        s = 0
    elif x == 3:   #se sua escolha for "3" você sairá.
        s = 1      #while vai verificar se S é igual a 0 (s =0), porém S é 1 então o loop terminará causando a saída do programa
    else:          #caso você digite uma função inválida presente no código 
        print("Opção invalida")
        s = 0

#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

def consoles(): #aqui começa o menu de consoles dentro da caixa def
    #C é uma variável na qual você poderá escolher 4 funções.
    c = int(input("[1] Playstation\n[2] Xbox\n[3] Nintendo\nEscolha o console desejado:")) 
    if c == 1:         
        #se ele quiser playstation, vai apertar o 1, e vai aparecer apenas os videogames playstation
        playstation(dicionário_playstation)
        s = 0

    elif c == 2:       
        #se ele quiser Xbox, vai apertar o 2, e vai aparecer apenas os videogames do Xbox
        xbox(dicionário_Xbox)
        s = 0

    elif c == 3:       
        #se ele quiser Nintendo, vai apertar o 3, e vai aparecer apenas os videogames da Nintendo
        nintendo(dicionário_nintendo)
        s = 0


    else:              
        #Caso nenhuma das funções desejadas sejam válidas será definido como falso(else)
        print("Opção invalida")
#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

Lista_playstation = [] #uma lista com consoles da playstation

def playstation(dicionário_playstation): #aqui começa o menu de Playstation dentro da caixa def


    videogames_playstation = {  
        #um dicionário para  agregar valores em cada console, sendo assim dicando salvo neste dicionário
        "1": "Playstation 1",
        "2": "Playstation 2",
        "3": "Playstation 3",
        "4": "Playstation 4",
        "5": "Playstation 5",
    }

    videogames_playstation_preço = {  
        #os valores agregados para cada console dentro do dicionário
        "Playstation 1": 299.90,
        "Playstation 2": 558.00,
        "Playstation 3": 1090.00,
        "Playstation 4": 2099.00,
        "Playstation 5": 4899.99
    }
#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

    print("Produtos dísponiveis:")

    for videogames_playstation, preco in videogames_playstation_preço.items():
        #O loop "for" está percorrendo todo o dicionário "videogame" listando os consoles e seus denominados valores   
        print(f"- {videogames_playstation}")

    escolha_ps = input("Escolha o produto desejado:")
    #"escolha_ps" é uma varíavel para vc digitalizar o produto que seja adquirir

    if escolha_ps in videogames_playstation_preço:
        #a variável escolha dentro do dicionário de "videogames":   
        valor_ps = videogames_playstation_preço[escolha_ps] 
        #"valor" é uma variável na qual entra no dicionário de videogames, entrando no seu input(sua escolha feita)

        print(f"O preço do(a) {escolha_ps} é R${valor_ps:}")
        #uma impressão com o preço da sua escolha(console desejado)

    else:
        print("Produto não encontrado")
        #caso sua escolha seja inválida


#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

lista_xbox = []        #uma lista com consoles do Xbox

def xbox(dicionário_Xbox): #aqui começa o menu do Xbox dentro da caixa def

    videogames_Xbox = {           
        #um dicionário para  agregar valores em cada console, sendo assim dicando salvo neste dicionário
        "1": "Xbox primeiro",
        "2": "Xbox 360",
        "3": "Xbox One",
        "4": "Xbox Series S",
        "5": "Xbox Series X"
    }
    videogames_Xbox_preco = {          
        #os valores agregados para cada console dentro do dicionário
        "Xbox primeiro": 200,
        "Xbox 360": 699.99,
        "Xbox One": 1399.99,
        "Xbox Series S": 2100.00,
        "Xbox Series X": 3450.00,
    }
#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

    print("Produtos dísponiveis:")
    for videogames_Xbox, preco in videogames_Xbox_preco.items():
    #O loop "for" está percorrendo todo o dicionário "videogames_xbox" 
    # listando os consoles e seus denominados valores    
        print(f"- {videogames_Xbox}")
    
    escolha_xbox = input("Escolha o produto desejado:")
    #"escolha_xbox" é uma varíavel para vc digitalizar o produto que seja adquirir

    if escolha_xbox in videogames_Xbox_preco:
    #a variável escolha dentro do dicionário de "videogames": 
        valorxbox = videogames_Xbox_preco[escolha_xbox]
        print(f"O preço do(a) {escolha_xbox} é R${valorxbox:}")

    else: #caso sua escolha seja inválida
        print("Produto não encontrado")

#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

lista_nintendo = []            #uma lista com consoles da Nintendo

def nintendo(dicionário_nintendo): #aqui começa o menu da Nintendo dentro da caixa def

    videogames_nintendo = {        
            #um dicionário para  agregar valores em cada console, sendo assim ficando salvo neste dicionário
            "1": "Nintendo Wii",
            "2": "Nintendo Wii u",
            "3": "Nintendo Switch",
        }
    videogames_nintendo_preco = {   
        #os valores agregados para cada console dentro do dicionário
        "Nintendo Wii": 599.99,
        "Nintendo Wii u": 1399.99,
        "Nintendo Switch": 2299.99
    }
#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

    print("Produtos dísponiveis:")
    for videogames_nintendo, preco in videogames_nintendo_preco.items():
    #O loop "for" está percorrendo todo o dicionário "videogames_nintendo" listando os consoles e seus denominados valores       
        print(f"- {videogames_nintendo}")
    
    escolha_nin = input("Escolha o produto desejado:")
    #"escolha_nin" é uma varíavel para vc digitalizar o produto que seja adquirir

    if escolha_nin in videogames_nintendo_preco:
    #a variável escolha dentro do dicionário de "videogames":    
        valornin = videogames_nintendo_preco[escolha_nin]
        print(f"O preço do(a) {escolha_nin} é R${valornin:}")

    else: #caso sua escolha seja inválida
        print("Produto não encontrado")


#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

dicionário_jogos = [] #uma lista com todos os jogos

def jogos(): #aqui começa o menu de jogos dentro da caixa def

    jogos = {             
        #um dicionário para  agregar valores em cada jogo, sendo assim ficando salvo neste dicionário
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
        #os valores agregados para cada console dentro do dicionário
        "ResidentEvil 4": 250.00,
        "The last of us": 90.00,
        "God of War Ragnarok": 250.00,
        "Forza Horizon 5": 250.00,
        "Gears of war 4": 100.00,
        "Halo infinite": 250.00,
        "Super Mario 3D World": 299.99,
        "Zelda breath of the wild": 324.99
    }
#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

    print("Produtos dísponiveis:")
    for jogos, preco in jogospreco.items():
    #O loop "for" está percorrendo todo o dicionário "jogos" listando os jogos e seus denominados valores    
        print(f"- {jogos}")
    
    escolhajg = input("Escolha o produto desejado:")
    #"escolhajg" é uma varíavel para vc digitalizar o produto que seja adquirir
    if escolhajg in jogospreco:
        preco = jogospreco[escolhajg]
        print(f"O preço do(a) {escolhajg} é R${preco:}")

    else: #caso sua escolha seja inválida
        print("Produto não encontrado")


#//////////////////////////////////////////////////////////////////////////////////////

while s == 0:

    print("Este é um catálogo onde é possível verificar os preços dos produtos desejados em uma loja de eletrônicos. \n \n Aviso: Este é um software apenas para consulta dos preços, não é possível realizar a compra aqui. \n Compras apenas em nossas lojas físicas. \n \n")

    op = int(input("Produtos da loja\n[1] Consoles\n[2] Jogos\n[3] Sair\nInforme o que deseja:\n"))
    menu(op)
    if op == 1:
        os.system("pause")
        os.system("cls")
        consoles1 = 0
        while consoles1 == 0:
            consoles()
            consoles1 = 1
        os.system("pause")
        os.system("cls")
              
    elif op == 2:
        os.system("pause")
        os.system("cls")
        jogo1 = 0
        while jogo1 == 0:
            jogos()
            jogo1 = 1
        os.system("pause")
        os.system("cls")

        
    elif op == 3:
        s = 1
        
    else:
        print("Opção invalida")

os.system("pause")