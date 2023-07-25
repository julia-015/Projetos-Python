import os

# def do menu com o armazenamento clientes
# Menu é o nome da nossa função

#Isabelle

def Menu(clientes):

    # enquanto w == 0, continuamos no menu

    w = 0
    while w == 0:

        # exibimos as opções do menu
				# op é uma variável criada pelo grupo

        print("Informe a função desejada no menu: ")
        print("1 - Registro")
        print("2 - Produtos da loja")
        print("3 - Carrinho")
        print("4 - Sair")
        op = int(input())

        # o if nos mostra que se a variável "op" for igual "1", realzará o comando
				# o.system ("cls") serve para apagar o programa acima dele
				# Registro(clientes), onde registro é a primeira opção que o usuário pode selecionar e clientes seria nosso argumento

        if op == 1:
            os.system("cls")
            Registro(clientes)
            os.system("cls")

        # elif nos mostra que se a variável "op" for igual "2", realzará o comando
				# o.system ("cls") serve para apagar o programa acima dele
				# Produtos_da_loja(clientes), onde produtos_da_loja é a segunda opção que o usuário pode selecionar e clientes seria nosso argumento


        elif op == 2:
            os.system("cls")
            Produtos_da_loja(clientes)
            os.system("cls")

        # elif nos mostra que se a variável "op" for igual "3", realzará o comando
				# o.system ("cls") serve para apagar o programa acima dele
					# Carrinho(clientes), onde carrinho é a terceira opção que o usuário pode selecionar e clientes seria nosso argumento
        elif op == 3:
            os.system("cls")
            carrinho(clientes)
            os.system("cls")

        # elif nos ostra que se a variável "op" for igual "4", realzará o comando
				# o.system ("cls") serve para apagar o programa acima dele
				# w = 1 é para o software ser fechado

        elif op == 4:
            os.system("cls")
            w = 1
            os.system("cls")

        # o else vai nos mostrar a "Opção inválida" caso nenhuma das anteriores fossem escolhidas ou a opção seja falsa.

        else:
            print("Opção inválida")

# ----------------------------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------------------------

#Isabelle

			# def do Registro terá todas as funções para registrar o nome do cliente
			# Registro é o nome da nossa  função
			# (Clientes) é o argumento onde as informações será armazenada

def Registro(clientes):
    nome = input("Digite o nome: ")    # variável para adicionar o nome do cliente
    cadastro = []                      # criação de uma variável chamada cadastro
    email = input("Digite o email: ")  # variável para adicionar o email do cliente
    senha = input("Digite a senha: ")  # variável para adicionar a senha do cliente
    cadastro.append(email)             # Email está salvo na variável de cadastros
    cadastro.append(senha)             # Senha está salvo na variável de cadastro
    clientes[nome] = cadastro          # Todos os cadastros (email e senha) está salvo no nome do cliente




# ----------------------------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------------------------

#Alexandre

			# def dos produtos da loja terá todas as funções/informações sobre os produtos presentes na loja e também outros menu presentes nele.
			# Produtos_da_loja é o nome da nossa função
			# (clientes) é o nosso argumento onde as informações vão estar salvas 
			# global é uma variável que pode ser acessada em qualquer ponto do código (em qualquer função).
			# videogames_playstation_preço é uma variável que criamos pra poder acessar o preço de cada produto da playstation

def Produtos_da_loja(clientes):
    global videogames_playstation_preço

			# s = 0 para continnuar no software, com o while acima enquanto s == 0

    s = 0

    # colchetes "[]" são usados para criar uma lista, que é uma estrutura de dados que pode conter vários itens.
	  # Variáveis 

    Lista_playstation = []
    lista_xbox = []
    lista_nintendo = []

    # /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

#Alexandre

    # as chaves "{}" são usadas para criar um dicionário, que é uma estrutura de dados que permite armazenar valores associados a chaves únicas.
		# Variáveis

    dicionário_jogos = {}
    dicionário_playstation = {}
    dicionário_Xbox = {}
    dicionário_nintendo = {}

    # ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
 
#Alexandre
 
		# Menu Utilizando o def para mante-lo em uma caixa, sendo assim as alterações feitas no def de menu não afetarão nenhuma outra parte do código

    def menu(x):                  # menu para selecionar o que dejesa
        if x == 1:                # se sua escolha for "1" entrará no menu de Consoles
            os.system("cls")      # Apagar a sequência do menu anterior
            consoles(clientes)    # consoles é o nome que demos para nossa função, (clientes) é o argumento onde está armazenado as nossas informação
            s = 0                 # s = 0 é para permanecer no nosso software 

        elif x == 2:             # se sua escolha for "2" entrará no menu de jogos
            os.system("cls")     # Apagar a sequência do menu anterior
            jogos(clientes)      # jogos é o nome que demos para nossa função, (clientes) é o argumento onde está armazenado as nossas informação
            s = 0                # s = 0 é para permanecer no nosso software 

        elif x == 3:             # se sua escolha for "3" você sairá.
            os.system("cls")     # Apagar a sequência do menu anterior
            Menu(clientes)       # Menu é o nome que demos para nossa função, (clientes) é o argumento onde está armazenado as nossas informação

            s = 0                # s = 0 é para permanecer no nosso software 

        else:                    # caso você digite uma função inválida presente no código
            print("Opção invalida")
            s = 0

    # /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////



    def consoles(clientes):   # aqui começa o menu de consoles dentro da caixa def

        # C é uma variável na qual você poderá escolher 4 funções.
				# O int serve para numeros inteiros

        c = int(input("[1] Playstation\n[2] Xbox\n[3] Nintendo Switch\nEscolha o console desejado:"))
        if c == 1:            # se ele quiser playstation, vai apertar o 1, e vai aparecer apenas os videogames playstation
            os.system("cls")  # Apagar a sequência do menu anterior
            playstation(dicionário_playstation)  #Variável com argumento 

        elif c == 2:          # se ele quiser Xbox, vai apertar o 2, e vai aparecer apenas os videogames do Xbox
            os.system("cls")  # Apagar a sequência do menu anterior
            xbox(dicionário_Xbox) #Variável com argumento 

        elif c == 3:          # se ele quiser Nintendo, vai apertar o 3, e vai aparecer apenas os videogames da Nintendo
            os.system("cls")  # Apagar a sequência do menu anterior
            nintendo(dicionário_nintendo) #Variável com argumento

        else:  # Caso nenhuma das funções desejadas sejam válidas será definido como falso e mostrará a mensagem de opção inválida
            print("Opção invalida")

    # /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

    def playstation(dicionário_playstation):  # aqui começa o menu de Playstation dentro da caixa def. Playstation como  o nome da nossa função e o argumento como (dicionário_playstation)

        Lista_playstation = []                # uma lista com consoles da playstation
        videogames_playstation = {            # um dicionário para agregar valores em cada console, sendo assim ficando salvo neste dicionário
            "1": "Playstation 1",             # Opção 1 
            "2": "Playstation 2",             # Opção 2
            "3": "Playstation 3",             # Opção 3
            "4": "Playstation 4",             # Opção 4
            "5": "Playstation 5",             # Opção 5
        }

        videogames_playstation_preço = {  # os valores agregados para cada console dentro do dicionário
                "Playstation 1": 299.90,  # Opção 1 
                "Playstation 2": 558.00,  # Opção 2
                "Playstation 3": 1090.00, # Opção 3
                "Playstation 4": 2099.00, # Opção 4
                "Playstation 5": 4899.99, # Opção 5 
            }
        # /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

        print("Produtos dísponiveis:")

				# A função "for" está percorrendo todo o dicionário "videogame_playstation" listando os consoles e seus denominados valores

        for videogames_playstation, preco in videogames_playstation_preço.items():
            print(f"- {videogames_playstation}") #Serve para aparecer os itens disponíveis da playstation

        escolha_ps = input("Escolha o produto desejado:")
        # "escolha_ps" é uma varíavel para vc digitalizar o produto que seja adquirir

        if escolha_ps in videogames_playstation_preço:            # a variável escolha dentro do dicionário de "videogames":
            valor_ps = videogames_playstation_preço [escolha_ps]  # "valor" é uma variável na qual entra no dicionário de videogames, entrando no seu input(sua escolha feita)
            print(f"O preço do(a) {escolha_ps} é R${valor_ps:}")  # uma impressão com o preço da sua escolha(console desejado)
        else:
            print("Produto não encontrado")                       # caso sua escolha seja inválida
        Lista_playstation.append(escolha_ps)                      # a lista de consoles da playstation adicionando uma sêquencia para a variável de escolhas
																																	# O append permite adicionar um elemento ao final de uma lista existente
        dicionário_playstation[escolha_ps] = Lista_playstation

    # /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

    def xbox(dicionário_Xbox):     # aqui começa o menu do Xbox dentro da caixa def. Xbox como o nome da nossa função e o argumento como (dicionário_Xbox)

        lista_xbox = []            # uma lista com consoles do Xbox
        videogames_Xbox = {        # um dicionário para agregar valores em cada console, sendo assim dicando salvo neste dicionário
            "1": "Xbox primeiro",  # Opção 1 
            "2": "Xbox 360",       # Opção 2
            "3": "Xbox One",       # Opção 3
            "4": "Xbox Series S",  # Opção 4
            "5": "Xbox Series X",  # Opção 5
        }
        videogames_Xbox_preco = {  # os valores agregados para cada console dentro do dicionário
                "Xbox primeiro": 200,       # Opção 1 
                "Xbox 360": 699.99,         # Opção 2
                "Xbox One": 1399.99,        # Opção 3
                "Xbox Series S": 2100.00,   # Opção 4
                "Xbox Series X": 3450.00,   # Opção 5
            }
       
        # /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

        print("Produtos dísponiveis:")

				# A função "for" está percorrendo todo o dicionário "videogame_xbox" listando os consoles e seus denominados valores

        for videogames_Xbox, preco in videogames_Xbox_preco.items():
            
            print(f"- {videogames_Xbox}")  #Serve para aparecer os itens disponíveis do Xbox

        escolha_xbox = input("Escolha o produto desejado:")
			  # "escolha_xbox" é uma varíavel para vc digitalizar o produto que seja adquirir

        if escolha_xbox in videogames_Xbox_preco:                      # a variável escolha dentro do dicionário de "videogames":
            valorxbox = videogames_Xbox_preco[escolha_xbox]            #"valor" é uma variável na qual entra no dicionário de videogames, entrando no seu input(sua escolha feita)
            print(f"O preço do(a) {escolha_xbox} é R${valorxbox:}")    # uma impressão com o preço da sua escolha(console desejado)
  
        else:                                                          # caso sua escolha seja inválida
            print("Produto não encontrado")
        lista_xbox.append(escolha_xbox)                                # a lista de consoles do xbox vai adicionando uma sêquencia para a variável de escolhas
																																			 # O append permite adicionar um elemento ao final de uma lista existente
        dicionário_Xbox[escolha_xbox] = lista_xbox

    # /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

    def nintendo(dicionário_nintendo):  # aqui começa o menu da Nintendo dentro da caixa def. Nintendo como o nome da nossa função e o argumento como (dicionário_nintendo)

        lista_nintendo = []          # uma lista com consoles da Nintendo
        videogames_nintendo = {      # um dicionário para  agregar valores em cada console, sendo assim ficando salvo neste dicionário
            "1": "Nintendo Wii",     # Opção 1 
            "2": "Nintendo Wii u",   # Opção 2
            "3": "Nintendo Switch",  # Opção 3 
        }
        videogames_nintendo_preco = {  # os valores agregados para cada console dentro do dicionário
                "Nintendo Wii": 599.99,     # Opção 1 
                "Nintendo Wii u": 1399.99,  # Opção 2 
                "Nintendo Switch": 2299.99, # Opção 3 
            }

        # /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

        print("Produtos dísponiveis:")

        # A função "for" está percorrendo todo o dicionário "videogame_nintendo" listando os consoles e seus denominados valores

        for videogames_nintendo, preco in videogames_nintendo_preco.items():
         
            print(f"- {videogames_nintendo}") #Serve para aparecer os itens disponíveis do nintendo

        escolha_nin = input("Escolha o produto desejado:")
        # "escolha_nin" é uma varíavel para vc digitalizar o produto que seja adquirir

        if escolha_nin in videogames_nintendo_preco:                # a variável escolha dentro do dicionário de "videogames":
            valornin = videogames_nintendo_preco[escolha_nin]       #"valor" é uma variável na qual entra no dicionário de videogames, entrando no seu input(sua escolha feita)
            print(f"O preço do(a) {escolha_nin} é R${valornin:}")   # uma impressão com o preço da sua escolha(console desejado)
        else:                                                       # caso sua escolha seja inválida
            print("Produto não encontrado")                         
        lista_nintendo.append(escolha_nin)                          # a lista de consoles do xbox vai adicionando uma sêquencia para a variável de escolhas
																																	  # O append permite adicionar um elemento ao final de uma lista existente
        dicionário_nintendo[escolha_nin] = lista_nintendo

# ------------------------------------------------------------------------------------------------------------------------------------------------------


    # ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

    def jogos(clientes):        # aqui começa o menu de jogos dentro da caixa def. Jogos como o nome da nossa função e o argumento como (clientes) que já era usado no começo do código
        dicionário_jogos = []   # uma lista com todos os jogos
        jogos = {               # um dicionário para  agregar valores em cada jogo, sendo assim ficando salvo neste dicionário
            "1": "ResidentEvil 4",
            "2": "The last of us",
            "3": "God of War Ragnarok",
            "4": "Forza Horizon 5",
            "5": "Gears of war 4",
            "6": "Halo infinite",
            "7": "Super Mario 3D World",
            "8": "Zelda breath of the wild",
        }

        jogospreco = {           # os valores agregados para cada console dentro do dicionário
            "ResidentEvil 4": 250.00,
            "The last of us": 90.00,
            "God of War Ragnarok": 250.00,
            "Forza Horizon 5": 250.00,
            "Gears of war 4": 100.00,
            "Halo infinite": 250.00,
            "Super Mario 3D World": 299.99,
            "Zelda breath of the wild": 324.99,
        }
        # /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

        print("Produtos dísponiveis:")

# A função "for" está percorrendo todo o dicionário "jogos" listando os jogos e seus denominados valores

        for jogos, preco in jogospreco.items():
           
            print(f"- {jogos}") #Serve para aparecer os jogos que estão disponíveis

        escolhajg = input("Escolha o produto desejado:")
        # "escolhajg" é uma varíavel para vc digitalizar o produto que seja adquirir

        if escolhajg in jogospreco:                              # a variável escolha dentro do dicionário de "jogospreco":
            preco = jogospreco[escolhajg]                        #"preço" é uma variável na qual entra no dicionário de jogospreco, entrando no seu input(sua escolha feita)
            print(f"O preço do(a) {escolhajg} é R${preco:}")     # uma impressão com o preço da sua escolha(console desejado)
        else:                                                    # caso sua escolha seja inválida
            print("Produto não encontrado")
        dicionário_jogos.append(escolhajg)                       # a lista de consoles do xbox vai adicionando uma sêquencia para a variável de escolhas
																																 # O append permite adicionar um elemento ao final de uma lista existente
        clientes[escolhajg] = dicionário_jogos

    # //////////////////////////////////////////////////////////////////////////////////////

    clientes = {}   #um novo dicionário vázio
    while s == 0:   #Enquanto "s" for igual a "0"

        # Solicita que o usuário selecione uma opção que esteja presente no menu e armazena o valor na variável "op" 

        op = int(input("Produtos da loja\n[1] Consoles\n[2] Jogos\n[3] Sair\nInforme o que deseja:\n"))

        menu(op) # Chama a função "menu" com o valor da variável "op" como parâmetro

        # Verifica qual opção foi selecionada e executa diferentes ações de acordo com o resultado
        if op == 1:
            # Limpa a tela do console e aguarda a entrada do usuário
            os.system("pause") # Faz o software pausar
            os.system("cls")   # Apagar a sequência do menu anterior
            s = 0              # Define a variável "s" como zero

        elif op == 2:
            os.system("pause") # Faz o software pausar
            os.system("cls")   # Apagar a sequência do menu anterior
            s = 0              # Define a variável "s" como zero

        elif op == 3:
            s = 1              # A opção 3 serve para sair do nosso sistema, logo, enquanto s = 0, permanecerá, por isso colocamos s = 1, para poder sair do while e fechar o software

        else:
            print("Opção invalida")

    os.system()


# ----------------------------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------------------------


# Função para finalizar a compra
# def do carrinho terá uma lista das suas compras feitas na loja armazenadas no seu registro. E também o menu de confirmação da compra
def carrinho(clientes):# Definindo a função "carrinho" que recebe um parâmetro "clientes"
    # Limpando a tela do console 
    os.system("cls")

    #Variáveis globais são aquelas que podem ser acessadas em qualquer parte do código
    # Declarando as variáveis globais que serão usadas na função
    global dicionário_playstation_car
    global dicionário_xbox_car
    global dicionário_nintendo_car
    global dicionário_jogos_car

    # Variável que armazenará o total da compra
    total = 0

    #Declarando as listas vazias que serão usadas para armazenar os produtos selecionados pelos clientes
    Lista_playstation_car = []
    lista_xbox_car = []
    lista_nintendo_car = []
    lista_jogos_car = []
    # /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

    # as chaves "{}" são usadas para criar um dicionário, que é uma estrutura de dados que permite armazenar valores associados a chaves únicas.
    dicionário_jogos_car = { #contém o nome de alguns jogos e seus respectivos preços, armazenados como pares chave-valor
        "ResidentEvil 4": 250.00,
        "The last of us": 90.00,
        "God of War Ragnarok": 250.00,
        "Forza Horizon 5": 250.00,
        "Gears of war 4": 100.00,
        "Halo infinite": 250.00,
        "Super Mario 3D world": 299.99,
        "Zelda breath of the wild": 324.99,
    }
    dicionário_playstation_car = {# contém o nome de alguns modelos de consoles Playstation e seus respectivos preços.
        "Playstation 1": 299.90,
        "Playstation 2": 558.00,
        "Playstation 3": 1090.00,
        "Playstation 4": 2099.00,
        "Playstation 5": 4899.99,
    }
    dicionário_xbox_car = {#contém o nome de alguns modelos de consoles Xbox e seus respectivos preços.
        "Xbox primeiro": 200.00,
        "Xbox 360": 699.99,
        "Xbox One": 1399.99,
        "Xbox Series S": 2100.00,
        "Xbox Series X": 3450.00,
    }
    dicionário_nintendo_car = {#contém o nome de alguns modelos de consoles Nintendo e seus respectivos preços.
        "Nintendo Wii": 599.99,
        "Nintendo Wii U": 1399.99,
        "Nintendo Switch": 2299.99,
    }
    # Loop que permite adicionar produtos ao carrinho
    while True:
        # Exibe as opções do menu
        print("Escolha uma opção:")
        print("[1] Playstation")
        print("[2] Xbox")
        print("[3] Nintendo")
        print("[4] Jogos")
        print("[5] Sair")

        # Lê a opção de Playstation escolhida pelo usuário e converte para inteiro
        op = int(input())

        if op == 1:# Verifica a opção de Playstation escolhida pelo usuário
            os.system("cls")# Limpa a tela do console   
            # Exibe as opções de Playstation
            print("[1] Playstation 1 ")
            print("[2] Playstation 2")
            print("[3] Playstation 3")
            print("[4] Playstation 4")
            print("[5] Playstation 5")

            # Lê a opção de Playstation escolhida pelo usuário e converte para inteiro
            op_playstation = int(input())
            
            # Verifica a opção de Playstation escolhida pelo usuário
            if op_playstation == 1:
                os.system("cls")    

                #O operador += é usado em Python para adicionar um valor à variável existente.

                # Adiciona o preço de Playstation 1 ao total da compra
                total += dicionário_playstation_car["Playstation 1"]
                # Adiciona Playstation 1 à lista de itens do carrinho
                Lista_playstation_car.append("Playstation 1")
                # Exibe uma mensagem informando que Playstation 1 foi adicionado ao carrinho
                print("Playstation 1 adicionado ao carrinho.")


            
            # Verifica a opção de Playstation escolhida pelo usuário
            elif op_playstation == 2:
                os.system("cls")
                # Adiciona o preço de Playstation 2 ao total da compra
                total += dicionário_playstation_car["Playstation 2"]
                # Adiciona Playstation 2 à lista de itens do carrinho
                Lista_playstation_car.append("Playstation 2")
                # Exibe uma mensagem informando que Playstation 2 foi adicionado ao carrinho
                print("Playstation 2 adicionado ao carrinho.")

            # Verifica a opção de Playstation escolhida pelo usuário
            elif op_playstation == 3:
                os.system("cls")
                # Adiciona o preço de Playstation 3 ao total da compra
                total += dicionário_playstation_car["Playstation 3"]
                # Adiciona Playstation 3 à lista de itens do carrinho
                Lista_playstation_car.append("Playstation 3")
                # Exibe uma mensagem informando que Playstation 3 foi adicionado ao carrinho
                print("Playstation 3 adicionado ao carrinho.")

             # Verifica a opção de Playstation escolhida pelo usuário
            elif op_playstation == 4:
                os.system("cls")
                # Adiciona o preço de Playstation 4 ao total da compra
                total += dicionário_playstation_car["Playstation 4"]
                # Adiciona Playstation 4 à lista de itens do carrinho
                Lista_playstation_car.append("Playstation 4")
                # Adiciona Playstation 4 à lista de itens do carrinho
                print("Playstation 4 adicionado ao carrinho.")

             # Verifica a opção de Playstation escolhida pelo usuário    
            elif op_playstation == 5:
                os.system("cls")
                # Adiciona o preço de Playstation 5 ao total da compra
                total += dicionário_playstation_car["Playstation 5"]
                # Adiciona Playstation 5 à lista de itens do carrinho
                Lista_playstation_car.append("Playstation 5")
                print("Playstation 5 adicionado ao carrinho.")
                # Adiciona Playstation 5 à lista de itens do carrinho
            else:
                print("Opção inválida.")

        # Verifica a opção de Xbox escolhida pelo usuário
        elif op == 2:
            os.system("cls")
            # Exibe as opções de Playstation
            print("[1] Xbox primeiro")
            print("[2] Xbox 360")
            print("[3] Xbox One")
            print("[4] Xbox Series S")
            print("[5] Xbox Series X")

            # Lê a opção de Xbox escolhida pelo usuário e converte para inteiro
            op_xbox = int(input())

            # Verifica a opção de Xbox escolhida pelo usuário
            if op_xbox == 1:
                os.system("cls")
                # Adiciona o preço de Xbox primeiro ao total da compra
                total += dicionário_xbox_car["Xbox primeiro"]
                # Adiciona Xbox primeiro à lista de itens do carrinho
                lista_xbox_car.append("Xbox primeiro")
                # Exibe uma mensagem informando que Xbox primeiro foi adicionado ao carrinho
                print("Xbox primeiro adicionado ao carrinho.")

            # Verifica a opção de Xbox escolhida pelo usuário
            elif op_xbox == 2:
                os.system("cls")
                # Adiciona o preço de Xbox 360 ao total da compra
                total += dicionário_xbox_car["Xbox 360"]
                # Adiciona Xbox 360 à lista de itens do carrinho
                lista_xbox_car.append("Xbox 360")
                # Exibe uma mensagem informando que Xbox 360 foi adicionado ao carrinho
                print("Xbox 360 adicionado ao carrinho.")


            # Verifica a opção de Xbox escolhida pelo usuário
            elif op_xbox == 3:
                os.system("cls")
                # Adiciona o preço de Xbox 360 ao total da compra
                total += dicionário_xbox_car["Xbox One"]
                # Adiciona Xbox 360 à lista de itens do carrinho
                lista_xbox_car.append("Xbox One")
                # Exibe uma mensagem informando que Xbox 360 foi adicionado ao carrinho
                print("Xbox One adicionado ao carrinho.")


            # Verifica a opção de Xbox escolhida pelo usuário    
            elif op_xbox == 4:
                os.system("cls")
                # Adiciona o preço de Xbox Series S ao total da compra
                total += dicionário_xbox_car["Xbox Series S"]
                # Adiciona Xbox Series S à lista de itens do carrinho
                lista_xbox_car.append("Xbox Series S")
                # Exibe uma mensagem informando que Xbox Series S foi adicionado ao carrinho
                print("Xbox Series S adicionado ao carrinho.")

            # Verifica a opção de Xbox escolhida pelo usuário    
            elif op_xbox == 5:
                os.system("cls")
                # Adiciona o preço de Xbox Series X ao total da compra
                total += dicionário_xbox_car["Xbox Series X"]
                # Adiciona Xbox Series X à lista de itens do carrinho
                lista_xbox_car.append("Xbox Series X")
                # Exibe uma mensagem informando que Xbox Series X foi adicionado ao carrinho
                print("Xbox Series X adicionado ao carrinho.")
            else:
                print("Opção inválida.")

        elif op == 3:
            os.system("cls")
            print("[1]Nintendo Wii")
            print("[2] Nintendo Wii U")
            print("[3] Nintendo Switch")

            op_nin = int(input())

            if op_nin == 1:
                os.system("cls")
                total += dicionário_nintendo_car["Nintendo Wii"]
                lista_nintendo_car.append("Nintendo Wii")
                print("Nintendo Wii adicionado ao carrinho.")

            elif op_nin == 2:
                os.system("cls")
                total += dicionário_nintendo_car["Nintendo Wii U"]
                lista_nintendo_car.append("Nintendo Wii U")
                print("Nintendo Wii U adicionado ao carrinho.")

            elif op_nin == 3:
                os.system("cls")
                total += dicionário_nintendo_car["Nintendo Switch"]
                lista_nintendo_car.append("Nintendo Switch")
                print("Nintendo Switch adicionado ao carrinho.")

        elif op == 4:
            os.system("cls")
            print("Escolha um jogo:")
            print("[1] ResidentEvil 4")
            print("[2] The last of us")
            print("[3] God of War Ragnarok")
            print("[4] Forza Horizon 5")
            print("[5] Gears of war 4")
            print("[6] Halo infinite")
            print("[7] Super Mario 3D world")
            print("[8] Zelda breath of the wild")

            op_jogos = int(input())
            if op_jogos == 1:
                os.system("cls")
                total += dicionário_jogos_car["ResidentEvil 4"]
                lista_jogos_car.append("ResidentEvil 4")
                print("ResidentEvil 4 adicionado ao carrinho.")

            elif op_jogos == 2:
                os.system("cls")
                total += dicionário_jogos_car["The last of us"]
                lista_jogos_car.append("The last of us")
                print("The last of us adicionado ao carrinho.")

            elif op_jogos == 3:
                os.system("cls")
                total += dicionário_jogos_car["God of War Ragnarok"]
                lista_jogos_car.append("God of War Ragnarok")
                print("God of War Ragnarok adicionado ao carrinho.")
            if op_jogos == 4:
                os.system("cls")
                total += dicionário_jogos_car["Forza Horizon 5"]
                lista_jogos_car.append("Forza Horizon 5")
                print("Forza Horizon 5 adicionado ao carrinho.")

            elif op_jogos == 5:
                os.system("cls")
                total += dicionário_jogos_car["Gears of war 4"]
                lista_jogos_car.append("Gears of war 4")
                print("Gears of war 4 adicionado ao carrinho.")

            elif op_jogos == 6:
                os.system("cls")
                total += dicionário_jogos_car["Halo infinite"]
                lista_jogos_car.append("Halo infinite")
                print("Halo infinite adicionado ao carrinho.")
            elif op_jogos == 7:
                os.system("cls")
                total += dicionário_jogos_car["Super Mario 3D world"]
                lista_jogos_car.append("Super Mario 3D world")
                print("Super Mario 3D world adicionado ao carrinho.")

            elif op_jogos == 8:
                os.system("cls")
                total += dicionário_jogos_car["Zelda breath of the wild"]
                lista_jogos_car.append("Zelda breath of the wild")
                print("Zelda breath of the wild adicionado ao carrinho.")
        elif op == 5:
            os.system("cls")
            Menu(clientes)
            os.system()
        elif op == 6:
            break



# inicializa a lista de clientes vazia
clientes = {}

# chamamos a função Menu para começar o programa
Menu(clientes)