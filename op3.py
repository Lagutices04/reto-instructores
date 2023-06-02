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
if i1 in instructores.values():
        print("1 para lista de instructor 1")
        print("2 para lista de instructor 2")  
        print("3 para lista de instructor 3")  
        seleccion=int(input("seleccione la lista que quiera modificar "))   

op = int(input("¿Qué opción deseas realizar? "))

if op==3:
    sino=int(input("quieres eliminr un nombre 1 para si 2 para no"))
    if sino==1:
        if seleccion==1:
            del instructores["instructor 1"]
        elif seleccion==2:
            del instructores["instructor 2"]
        elif seleccion==3:
            del instructores["instructor 3"]
        
        print("se elimino el elemento de la lista")
    else:
        print("no se eilimino el elemento de la lista")
print(instructores)        
        
        
        