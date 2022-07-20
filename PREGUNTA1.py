
fila = int(input('Ingresa el número de filas: '))

for i in range(fila):
    for columna in range(fila, i, -1):
        print(end=' ')
    

    for valores in range(1, columna+1, 1):
        print(valores, end=' ')
    print()