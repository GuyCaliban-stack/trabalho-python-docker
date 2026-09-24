a = 0
b = 0
c = 0
d = 0

def exercicio23():
    global a, b, c, d

    if d < a:
        print(d, a, b, c)
    elif d < b:
        print(a, d, b, c)
    elif d < c:
        print(a, b, d, c)
    else:
        print(a, b, c, d)

def main():
    global a, b, c, d

    a = int(input("Digite o primeiro valor: "))
    b = int(input("Digite o segundo valor: "))
    c = int(input("Digite o terceiro valor: "))
    d = int(input("Digite o quarto valor: "))

    exercicio23()

if __name__ == "__main__":
    main()