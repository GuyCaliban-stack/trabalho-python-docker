def exercicio29(tipo, valor):
    if tipo == 1:
        novo_valor = valor * 1.03
        print("Valor corrigido:", novo_valor)

    elif tipo == 2:
        novo_valor = valor * 1.05
        print("Valor corrigido:", novo_valor)

def main():
    tipo = int(input("Tipo de investimento (1-Poupança / 2-Renda Fixa): "))
    valor = float(input("Valor investido: "))

    exercicio29(tipo, valor)

if __name__ == "__main__":
    main()