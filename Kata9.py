def promedioTanque(Tanques):
     suma = sum(Tanques)
     NumeroTanques = len(Tanques)
     promedio =  suma/NumeroTanques
     return promedio 
def reporteTanques(tanqueUno,tanqueDOS,tanqueTres):
    promedioTanques = promedioTanque([tanqueUno,tanqueDOS,tanqueTres])
    return print("Reporte de combustible: \nTanqueUno: "+ 
        str(tanqueUno) + "\nTanqueDos: " 
        + str(tanqueDOS) + "\nTanqueTres: " + 
        str(tanqueTres) + "\nPromedio de los tanques: " + str(promedioTanques))

reporteTanques(87,70,85)


def InformePreciso (horaPre,tiempoVuelo,destino,tanqueExterno,tanqueInterno):
    return print("\nLa hora de prelanzamiento es: " + 
        str(horaPre) + "\nTiempo de vuelo: " + 
        str(tiempoVuelo) + "\nDestino: " + 
        destino + "\nPromedio de combustible: " + 
        str((tanqueInterno + tanqueExterno)/2))

InformePreciso(15,25,"Marte",75,50)

def InformePreciso (destino,*Tiempominutos,**tanquesGasolina):
    total=  f"La mision es hacia : {destino} \nTiempo total de viaje: {sum(Tiempominutos)} minutos\n" 
    
    for nombreTanque,galones in tanquesGasolina.items():
        total += f"{nombreTanque} tanque --> contiene {galones} golanes\n"
    return total + f"total de combustible remanente: {sum(tanquesGasolina.values())}"

print(InformePreciso("Moon", 8, 11, 55, main = 300000, external = 200000))

