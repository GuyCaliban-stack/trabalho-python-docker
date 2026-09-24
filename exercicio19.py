a = 0.0
b = 0.0

def exercicio19():
    global a, b

    if a > b:
         print(a)
    else:
         print(b)

def main():
    global a, b

    a = float(input("Digite o primeiro valor:  "))
    b = float(input("Digite o segundo valor:  "))

    exercicio19()

if __name__ == "__main__":
    main()