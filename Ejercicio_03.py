Personas = {}
Nombres = []
Documentos = []
Edades = []


cantidad = int(input('Introduce la cantidad de personas: '))
for num in range(cantidad):
    persona = {}
    Nombre = input(f'Escriba el nombre de la persona {num+1}: ')
    Nombres.append(Nombre)

    persona.update({'nombre': Nombre})

    Documento = int(input(f'Escribe el DNI de la persona {num+1}: '))
    Documentos.append(Documento)
    persona.update({'dni': Documento})

    Edad = int(input(f'Ingrese la edad de la persona {num+1}: '))
    Edades.append(Edad)
    persona.update({'edad': Edad})

    Personas.update({'Persona '+str(num + 1): persona})

Edades.sort()
for i in range(len(Edades)):
    for j in Personas:
        if Personas[j]['edad'] == Edades[i]:
            print(Personas[j])
    