n1 = 0.0
n2 = 0.0
n3 = 0.0
n4 = 0.0

def exercicio21():
    global n1, n2, n3, n4

    media = (n1 + n2 + n3 + n4) / 4

    print("Média:", media)

    if media >= 6:
        print("APROVADO")
    elif media >= 3:
        print("EXAME")
    else:
        print("RETIDO")

def main():
    global n1, n2, n3, n4

    n1 = float(input("Digite a primeira nota: "))
    n2 = float(input("Digite a segunda nota: "))
    n3 = float(input("Digite a terceira nota: "))
    n4 = float(input("Digite a quarta nota: "))

    exercicio21()

if __name__ == "__main__":
    main()