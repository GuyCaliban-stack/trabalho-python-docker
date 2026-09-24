a = 0.0
b = 0.0
c = 0.0

def exercicio20():
    global a, b, c

    delta = b ** 2 - 4 * a * c

    if delta < 0:
        print("Não existem raízes reais.")

    elif delta == 0:
        x = -b / (2 * a)
        print("Existe uma raiz real:", x)

    else:
        x1 = (-b + delta ** 0.5) / (2 * a)
        x2 = (-b - delta ** 0.5) / (2 * a)

        print("Existem duas raízes reais.")
        print("X1:", x1)
        print("X2:", x2)


def main():
    global a, b, c

    a = float(input("Digite A:  "))
    b = float(input("Digite B:  "))
    c = float(input("Digite C:  "))


    exercicio20()



if __name__ == "__main__":
    main()