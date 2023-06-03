fruver={}
while True:
    print("supermercado noe")
    print("1 añadir/modificar")
    print("buscar")
    print("borrar")
    print("listar")
    print("salir")
    opcion=int(input("que opcion deseas realizar"))
    if(opcion==1):
        articulo=input("ingrese el nombre del articulo")
        if articulo in fruver:
            print("articulo ya se encuentra registrado")
            opcion=input("1 modificar el precio del articulo, 2 modifica el tipo del articulo 3 terminar")
            if opcion=="1":
                precio=int(input("dame el precio del nuevo articulo"))
                fruver[articulo]['precio']=precio
            if opcion=="2":
                tipo=int(input("selecciona el nuevo tipo del articulo 1 vegetal 2 fruta"))
                if(tipo==1):
                    variedad="vegetal"
                elif(tipo==2):
                    variedad="fruta"
                    fruver[articulo]['tipo']=variedad
        else:
            fruver[articulo]={}
            precio=int(input("dame el precio del articulo"))
            fruver[articulo]['precio']=precio
            tipo=int(input("seleccione el tipo del articulo 1 vegetal 2 fruta"))
            if(tipo==2):
                variedad="fruta"
            fruver[articulo]['tipo']=variedad
            print("no esta")
    elif(opcion==2):
        texto=input("ingrese el articulo a buscar")
        print("se encontraron los siguientes resultados")


        for articulos,datos in fruver.items():
            if articulos.startswith(texto):
                print("el precio del articulo ingresado es{fruver [articulo] ['precio]}")
                print(articulo)
            elif(opcion==5):
                print("adios")
                break
           
