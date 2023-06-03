i1={
    "primer nombre 1":"laura",
     "apellido 1 ":"cespedes",
     "materia 1":"filosofia",
      "telefono 1":"3456354"
}
i2={
    "primer nombre 2":"valeria",
     "apellido 2":"espitia",
     "materia 2":"historia del arte",
     "telefono 2":"5867956"
}
i3={
    "primer nombre 3":"leia",
     "apellido 3":"gutierrez",
     "materia 3":"ingieneria electronica",
      "telefono 3":"864356324"    
}
instructores={
  "instructor 1":i1,
  "instructor 2":i2,
  "instructor 3":i3
}
print(instructores)

while True:
  
 print("1 agregar/modificar el nombre del instructor si no esta correcto segun la lista")
 print("2 buscar el nombre de instructor")
 print("3 borrar el nombre del instructor")
 print("4 listar todos los nombres de los instructores ")
 op=int(input(" que opcion deseas realizar")) 
 if(op==1):
     instructores={
     "instructor1":i1,
     "instructor2":i2,
     "instrcutor3":i3
     }
     print(instructores)
     if i1 in instructores.values():
        print("1 para lista de instructor 1")
        print("2 para lista de instructor 2")  
        print("3 para lista de instructor 3")  
        seleccion=int(input("seleccione la lista que quiera modificar "))   
                    
        print("1  cambiar nombre")
        print("2 cambiar apellido")
        print(" 3 cambiar materia")
        print("4 cambiar numero telefonico ")
        correccion1=int(input("si los datos de la lista de instructor 1  son incorrectos seleccione que opcion desea realizar para modificarlos "))
         
        if correccion1==1:
          nombreCo=input("ingrese el nuevo nombre ")
          instructores ["instructor1"] ["primer nombre 1"]=nombreCo
          print (instructores["instructor1"])
        elif correccion1==2:
             apellidoCo=input("ingrese el nuevo apellido")
             instructores["instructor1"] ["apellido 1"]=apellidoCo
             print(instructores["instructor1"])
        elif correccion1==3:
           materiaCo=input("ingrese la nueva materia")
           instructores["instructor1"]["apellido 1"]=materiaCo
           print(instructores["instructor1"])
        elif correccion1==4:
          telefonoCo=input("ingrese el nuevo numero telefonico")
          instructores["instructor1"]["telefono 1"]=telefonoCo
          print(instructores["instructor1"])
     print("1  cambiar nombre")
     print("2 cambiar apellido")
     print(" 3 cambiar materia")
     print("4 cambiar numero telefonico ")
     correccion2=int(input("si los datos de la lista de instructor 2  son incorrectos seleccione que opcion desea realizar para modificarlos "))
     if correccion2==1:
        nombreCo=input("ingrese el nuevo nombre ")
        instructores ["instructor2"] ["primer nombre 2"]=nombreCo
        print (instructores["instructor2"])
     elif correccion2==2:
       apellidoCo=input("ingrese el nuevo apellido")
       instructores["instructor2"]["apellido 2"]=apellidoCo
       print(instructores["instructor2"])
     elif correccion2==3:
       materiaCo=input("ingrese la nueva materia")
       instructores["instructor2"]["materia 2"]=materiaCo
       print(instructores["instructor2"])
     elif correccion2==4:
       telefonoCo=input("ingrese el nuevo numero de telefono")
       instructores["instructor2"]["telefono 2"]=telefonoCo
       print(instructores["instructor2"])
       
     print("1  cambiar nombre")
     print("2 cambiar apellido")
     print(" 3 cambiar materia")
     print("4 cambiar numero telefonico ")  
     correccion3=int(input("si los datos de la lista de instructor 3  son incorrectos seleccione que opcion desea realizar para modificarlos "))
     if correccion3==1:
       nombreCo=input("ingrese el nuevo nombre del instructor")
       instructores["instrcutor3"]["primer nombre 3"]=nombreCo
       print(instructores["instrcutor3"])
     elif correccion3==2:
       apellidoCo=input("ingrese el nuevo nombre")
       instructores["instrcutor3"]["apellido 3"]=apellidoCo
       print(instructores["instrcutor3"])
     elif correccion3==3:
       materiaCo=input("ingrese la nueva materia")
       instructores["instrcutor3"]["materia 3"]=materiaCo
       print(instructores["instrcutor3"])
     elif correccion3==4:
       telefonoCo=input("ingrese el nuevo numero telefonico")
       instructores["instrcutor3"]["telefono 3"]=telefonoCo
       print(instructores["instrcutor3"])
     else:
       print("valor incorrecro")
     ingresoDato = input("Ingrese un nombre: ")
 if ingresoDato in instructores["instructor1"].values():
    print("El dato ingresado ya existe, se agregará a la lista")
    instructores["instructor1"]["nueva clave"].append(ingresoDato)
 else:
    print("El dato no existe")
 
 
 
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
 instructores={
  "instructor 1":i1,
  "instructor 2":i2,
  "instructor 3":i3
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