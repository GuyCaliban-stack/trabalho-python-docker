hora_inicio = 0
minuto_inicio = 0
hora_fim = 0
minuto_fim = 0

def exercicio25():
    global hora_inicio, minuto_inicio, hora_fim, minuto_fim

    inicio = hora_inicio * 60 + minuto_inicio
    fim = hora_fim * 60 + minuto_fim

    if fim <= inicio:
        fim = fim + 24 * 60

    duracao = fim - inicio

    horas = duracao // 60
    minutos = duracao % 60

    print("Duração:", horas, "hora(s) e", minutos, "minuto(s)")

def main():
    global hora_inicio, minuto_inicio, hora_fim, minuto_fim

    hora_inicio = int(input("Hora inicial: "))
    minuto_inicio = int(input("Minuto inicial: "))

    hora_fim = int(input("Hora final: "))
    minuto_fim = int(input("Minuto final: "))

    exercicio25()

if __name__ == "__main__":
    main()