import os

# Loja
clientes = []
produtos = {"consoles": {"Playstation": 3000, "Xbox": 3500, "Nintendo": 2500},
            "jogos": ["Fifa 22", "Call of Duty", "Resident Evil", "Assassin's Creed"]}
carrinho = []

# Registro
while True:
    print("\n----- Bem-vindo(a) à nossa loja! -----")
    print("1 - Registro")
    print("2 - Produtos da loja")
    print("3 - Carrinho")
    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        nome = input("Digite o seu nome: ")
        email = input("Digite o seu e-mail: ")
        senha = input("Digite a sua senha: ")
        clientes.append({"nome": nome, "email": email, "senha": senha})
        print("Cadastro realizado com sucesso!")

    # Produtos da loja
    elif opcao == 2:
        while True:
            print("\nProdutos da loja:")
            print("1 - Consoles")
            print("2 - Jogos")
            print("3 - Voltar ao menu anterior")
            opcao_produto = int(input("Escolha uma opção: "))

            # Consoles
            if opcao_produto == 1:
                while True:
                    print("\nConsoles:")
                    print("1 - Playstation")
                    print("2 - Xbox")
                    print("3 - Nintendo")
                    print("4 - Voltar ao menu anterior")
                    opcao_console = int(input("Escolha uma opção: "))
                    if opcao_console == 1:
                        carrinho.append({"produto": "Playstation", "preco": produtos["consoles"]["Playstation"]})
                        print("Playstation adicionado ao carrinho!")
                    elif opcao_console == 2:
                        carrinho.append({"produto": "Xbox", "preco": produtos["consoles"]["Xbox"]})
                        print("Xbox adicionado ao carrinho!")
                    elif opcao_console == 3:
                        carrinho.append({"produto": "Nintendo", "preco": produtos["consoles"]["Nintendo"]})
                        print("Nintendo adicionado ao carrinho!")
                    elif opcao_console == 4:
                        break
                    else:
                        print("Opção inválida!")

            # Jogos
            elif opcao_produto == 2:
                print("\nJogos disponíveis:")
                for jogo in produtos["jogos"]:
                    print(jogo)
                opcao_jogo = input("Digite o nome do jogo que deseja: ")
                if opcao_jogo in produtos["jogos"]:
                    carrinho.append({"produto": opcao_jogo, "preco": 100})
                    print(opcao_jogo, "adicionado ao carrinho!")
                else:
                    print("Jogo indisponível!")

            # Voltar ao menu anterior
            elif opcao_produto == 3:
                break

            else:
                print("Opção inválida!")

    # Carrinho
    elif opcao == 3:
        while True:
            print("\nCarrinho:")
            for produto in carrinho:
                print(produto["produto"], "R$", produto["preco"])
            print("\n1 - Valor total")
            print("2 - Formas de pagamento")
            print("3 - Voltar ao menu anterior")
            opcao_carrinho = int

            os.system("pause")