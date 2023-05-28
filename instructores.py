instructores={"jennifer fajardo","paola ballen","jonathan espitia"}
while True:
 print(" 1 agregar el nombre del instructor")
 print (" 2 lista los nombres de los instructores")
 print (" 3 modificar el nombre de un instructor en la lista")
 print (" 4 borrar elemento de la lista ")
 print (" 5  buscar elemento determinado en la lista")
 print (" 6 orfrnar alfabeticamente la lista")
 op=int(input(" que opcion deseas realizar"))

 if (op==1):
  instructores={"jennifer fajardo","paola ballen","jonathan espitia"}
  nombre=input("agregue el nombre de un instructor /n")
  instructores.add(nombre)
  print (instructores)
  print("el nombre del instructor se agrego correctamente")
 elif (op==2):
     instructores={"jennifer fajardo","paola ballen","jonathan espitia"}
     for listar in instructores:
         print(listar)
 elif (op == 3):
    instructores = ["jennifer fajardo", "paola ballen", "jonathan espitia"]
    modificar = int(input("¿Qué elemento quieres modificar?"))
    nuevoValor = input("Ingresa el nuevo valor")
    instructores[modificar] = nuevoValor
    print(instructores)

   
 elif (op==4):
     instructores={"jennifer fajardo","paola ballen","jonathan espitia"}
     eliminar=input("que elemento quieres eliminar")
     instructores.remove(eliminar)
     print(instructores)
 elif (op==5):
      instructores={"jennifer fajardo","paola ballen","jonathan espitia"}
      buscar=input("que elemento quieres buscar de la lista")
      print(buscar in instructores)

 elif (op == 6):
    instructores = {"jennifer fajardo": "", "paola ballen": "", "jonathan espitia": ""}
    instructores_ordenados = sorted(instructores.keys())
    for instructores in instructores_ordenados:
        print(instructores)

   
 
     

else:
    print("opcion invalida ")


     
   
   




     
    
    

    
   
  
  


