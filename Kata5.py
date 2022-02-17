tierra = 149597870
jupiter = 778547200

print("La distancia entre la tierra y jupiter es de: " + str(abs(tierra - jupiter)) + " kms o " + str(round((abs(tierra - jupiter) * 0.621))) + " millas.")

nombrePP =input("Cual es el primer planeta: ")
primerPlaneta = int(input("Dame la distancia al sol del 1° planeta: "))
nombreSP = input("Cual es el segundo planeta: ")
segundoPlaneta = int(input("Dame la distancia al sol del 2° planeta: "))

print(f"La distancia entre {nombrePP} y {nombreSP} es de: {abs(primerPlaneta - segundoPlaneta)} kms o {round(abs((primerPlaneta - segundoPlaneta)) * 0.621)} millas.")
