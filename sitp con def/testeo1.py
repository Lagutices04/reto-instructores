saldo_disponible = 500000
valor_pasaje = 3000
deuda_acumulada = 0

def ingresar_al_SITP(tarjeta_personalizada):
    global saldo_disponible, deuda_acumulada
    
    if tarjeta_personalizada:
        precio = int(input("Digite cuánto saldo tienes para subirte al SITP: "))

        if precio >= valor_pasaje:
            deuda_acumulada += (precio - valor_pasaje)
            print("Te has subido al SITP. Deuda acumulada:", deuda_acumulada)
        else:
            print("Saldo insuficiente.")
    else:
        precio = int(input("Digite cuánto saldo tienes para subirte al SITP: "))

        if precio >= valor_pasaje:
            saldo_disponible -= valor_pasaje
            print("Te has subido al SITP. Saldo disponible:", saldo_disponible)
        else:
            print("Saldo insuficiente.")

def ejecutar():
    sino = int(input("¿Tienes tarjeta personalizada? 1 para sí, 2 para no: "))

    while True:
        if sino == 1 or sino == 2:
            ingresar_al_SITP(sino == 1)
        else:
            print("Opción inválida. Por favor, ingresa 1 o 2.")

ejecutar()

  
        
