def fatorial(n):
    resultado = 1

    for i in range(1, n + 1):
        resultado = resultado * i

    return resultado

def divisao(a, b):
    return a / b

n = int(input("Digite o valor de N: "))

soma = 1

for i in range(1, n + 1):
    soma = soma + divisao(1, fatorial(i))

    print("Resultado:", soma)