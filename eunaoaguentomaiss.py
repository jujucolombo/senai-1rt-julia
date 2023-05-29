while True:
    numero = int(input("Informe um número (ou um valor negativo): "))

    if numero < 0:
        print("Programa encerrado.")
        break

    if numero % 2 == 0:
        print(numero, "é um número par.")
    else:
        print(numero, "é um número ímpar.")