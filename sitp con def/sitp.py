# SITP sin tarjeta personalizada:
# costo del pasaje cuesta 3000
# si la tarjeta tiene >=3000 pasa el pasajero
# si tiene <3000 no pasa el pasajero
# si tiene un saldo mayor de 3000k, descontarlos y mostrar el saldo disponible

"""SITP SIN PERSONALIZAR
 1  el precio del pasaje es de 3000
 2 >=3000 puede pasar
 3 <3000 puede pasar pero queda debiendo
 4 si tiene mayor a 3000k descontar eso de su saldo total
 5 si tiene un saldo mayor a 3000 y debe pasajes, descontarlo del saldo total y mostrarl el saldo disponible"""
 
 # SIPT SIN TARJETA PERSONALIZADA
sino=int(input("¿tienes tarjeta personalizada? 1 para si 2 para no"))

saldoDisponible=int(500000)
valorPasaje=int(3000)
while True:
    if sino==2:
        print("no tienes tarjeta personalizada")
        precio=int(input("digite cuanto saldo tiene para subirse al sipt"))    
    elif valorPasaje<=3000:
        print("saldo insuficiente")
    elif valorPasaje>=3000:
        print("tienes saldo disponible ")
        
 