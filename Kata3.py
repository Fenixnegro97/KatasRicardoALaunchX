asteroide = int(input("A que velocidad vuela el asteroide: "))
tamaño_Asteroide = int(input("Cual es el tamaño del asteroide: "))

if asteroide > 25 and tamaño_Asteroide > 25 :
  print("ADVERTENCIA!!!! Un asteroide pasara cerca de la tierra y lleva una velocidad de : " + str(asteroide) + " Km/s" + " y dimension de: " + str(tamaño_Asteroide) + " metros")
elif asteroide >= 20 :
  print("Un asteroide podra ser visto y tiene una velocidad de: " + str(asteroide) + " Km/s" + " y dimension de: " + str(tamaño_Asteroide) + " metros")
else:
  print("Hay un asteroide cerca que NO sera visible y tiene una velocidad de: " + str(asteroide) + "Km/s" + " y dimension de: " + str(tamaño_Asteroide) + " metros")
