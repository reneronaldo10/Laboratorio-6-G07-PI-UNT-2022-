numero_de_listas = int(input("Cuantas listas quiere escribir?"))
for j in range(numero_de_listas):
    print("Dígame cuántas palabras tiene la lista", j+1)
    numero = int(input())
    if numero<1:
        print("error")
    else:
       lista = []
       for i in range(numero):
        print("Dígame la palabra", str(i+1)+":", end="")
        palabra = input()
        lista += [palabra]
    print("La lista creada es:", lista)
     

  