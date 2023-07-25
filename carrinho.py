clientes: {}

elif opcao == 3:
    while True:
        carrinho = print("\nCarrinho:")
        for produto in clientes:
            print(produto["produto"], "R$", produto["preco"])
            c = 0
            for i in range(carrinho):
                c += i
            print(f"\nValor total: {c}")