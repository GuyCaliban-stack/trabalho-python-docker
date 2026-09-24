numero = 0

def exercicio24():
    global numero

    if numero % 2 == 0 and numero % 3 == 0:
        print("É divisível por 2 e por 3.")
    else:
        print("Não é divisível por 2 e por 3.")

def main():
    global numero

    numero = int(input("Digite um número: "))

    exercicio24()

if __name__ == "__main__":
    main()