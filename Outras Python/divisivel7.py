numero = 1

while True:
    if numero % 5 == 0 and numero % 7 == 0:
        print("O primeiro número divisível por 5 e 7 é:", numero)
        break
    numero += 1