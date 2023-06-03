instructor1 = {
    "primer nombre 1": "Laura",
    "apellido 1": "Cespedes",
    "materia 1": "Filosofia",
    "telefono 1": "3456354"
}

instructor2 = {
    "primer nombre 2": "Valeria",
    "apellido 2": "Espitia",
    "materia 2": "Historia del Arte",
    "telefono 2": "5867956"
}

instructor3 = {
    "primer nombre 3": "Leia",
    "apellido 3": "Gutierrez",
    "materia 3": "Ingenieria Electronica",
    "telefono 3": "864356324"
}

instructores = {
    "instructor 1": instructor1,
    "instructor 2": instructor2,
    "instructor 3": instructor3
}

print(instructores)


def agregar_modificar_nombre():
    global instructores
    print(instructores)
    seleccion = int(input("Seleccione la lista que desea modificar: "))
    
    if seleccion == 1:
        instructor = instructores["instructor 1"]
    elif seleccion == 2:
        instructor = instructores["instructor 2"]
    elif seleccion == 3:
        instructor = instructores["instructor 3"]
    else:
        print("Opción inválida.")
        return
    
    print("1. Cambiar nombre")
    print("2. Cambiar apellido")
    print("3. Cambiar materia")
    print("4. Cambiar número telefónico")
    opcion = int(input("Seleccione la opción que desea realizar: "))
    
    if opcion == 1:
        nombre_nuevo = input("Ingrese el nuevo nombre: ")
        instructor["primer nombre " + str(seleccion)] = nombre_nuevo
        print(instructor)
    elif opcion == 2:
        apellido_nuevo = input("Ingrese el nuevo apellido: ")
        instructor["apellido " + str(seleccion)] = apellido_nuevo
        print(instructor)
    elif opcion == 3:
        materia_nueva = input("Ingrese la nueva materia: ")
        instructor["materia " + str(seleccion)] = materia_nueva
        print(instructor)
    elif opcion == 4:
        telefono_nuevo = input("Ingrese el nuevo número telefónico: ")
        instructor["telefono " + str(seleccion)] = telefono_nuevo
        print(instructor)
    else:
        print("Opción inválida.")


def buscar_nombre():
    elemento = input("Ingrese el nombre que desea buscar: ")
    encontrado = False
    
    for instructor in instructores.values():
        if instructor["primer nombre " + str(seleccion)].lower() == elemento.lower():
            encontrado = True
            break
    
    if encontrado:
        print(f"El elemento '{elemento}' fue encontrado.")
    else:
        print(f"El elemento '{elemento}' no fue encontrado.")


def borrar_nombre():
    global instructores
    seleccion = int(input("Seleccione la lista que desea borrar: "))
    
    if seleccion == 1:
        del instructores["instructor 1"]
    elif seleccion == 2:
        del instructores["instructor 2"]
    elif seleccion == 3:
        del instructores["instructor 3"]
    else:
        print("Opción inválida.")
        return
    
    print("El elemento ha sido eliminado de la lista.")
    print(instructores)


