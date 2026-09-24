a = 0
b = 0

def exercicio26():
    global a, b

    if a > b:
        maior = a
        menor = b
    else:
        maior = b
        menor = a

    if maior % menor == 0:
        print(maior, "é múltiplo de", menor)
    else:
        print(maior, "não é múltiplo de", menor)

def main():
    global a, b

    a = int(input("Digite o primeiro valor: "))
    b = int(input("Digite o segundo valor: "))

    exercicio26()

if __name__ == "__main__":
    main()