a = 0
b = 0

def exercicio22():
    global a, b

    if a < b:
        print(a, b)
    else:
        print(b, a)

def main():
    global a, b

    a = int(input("Digite o primeiro valor: "))
    b = int(input("Digite o segundo valor: "))

    exercicio22()

if __name__ == "__main__":
    main()
    