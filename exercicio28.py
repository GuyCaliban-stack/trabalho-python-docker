def exercicio28(preco, vendas):
    if vendas < 500 and preco < 30:
        novo_preco = preco * 1.10

    elif vendas >= 500 and vendas < 1000 and preco >= 30 and preco < 80:
        novo_preco = preco * 1.15

    elif vendas >= 1000 and preco >= 80:
        novo_preco = preco * 0.95

    else:
        novo_preco = preco

    print("Novo preço:", novo_preco)

def main():
    preco = float(input("Preço atual: "))
    vendas = float(input("Média mensal de vendas: "))

    exercicio28(preco, vendas)

if __name__ == "__main__":
    main()