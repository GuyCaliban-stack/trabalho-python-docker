def exercicio27(voltas, comprimento, tempo):
    distancia = voltas * comprimento
    distancia_km = distancia / 1000
    tempo_horas = tempo / 60

    velocidade = distancia_km / tempo_horas

    print("Velocidade média:", velocidade, "km/h")

def main():
    voltas = int(input("Número de voltas: "))
    comprimento = float(input("Comprimento do circuito em metros: "))
    tempo = float(input("Tempo em minutos: "))

    exercicio27(voltas, comprimento, tempo)

if __name__ == "__main__":
    main()