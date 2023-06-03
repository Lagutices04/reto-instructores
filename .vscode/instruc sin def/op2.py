i1 = {
    "primer nombre 1": "laura",
    "apellido 1": "cespedes",
    "materia 1": "filosofia",
    "telefono 1": "3456354"
}

i2 = {
    "primer nombre 2": "valeria",
    "apellido 2": "espitia",
    "materia 2": "historia del arte",
    "telefono 2": "5867956"
}

i3 = {
    "primer nombre 3": "leia",
    "apellido 3": "gutierrez",
    "materia 3": "ingenieria electronica",
    "telefono 3": "864356324"    
}

instructores = {
    "instructor 1": i1,
    "instructor 2": i2,
    "instructor 3": i3
}

print(instructores)

op = int(input("¿Qué opción deseas realizar? "))

if op == 2:
    elemento = input("Ingrese el nombre que desea buscar: ")
    encontrado = False
    
    for instructor, datos in instructores.items():
        for valor in datos.values():
            if valor.lower() == elemento.lower():
                encontrado = True
                break
        if encontrado:
            break
    
    if encontrado:
        print(f"El elemento '{elemento}' fue encontrado.")
    else:
        print(f"El elemento '{elemento}' no fue encontrado.")
