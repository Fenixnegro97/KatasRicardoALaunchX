from datetime import date 
date.today()
print("La fecha es: " + str(date.today()))

parsec = 1
parsec = int(input("dame los parsec a convertir: "))

lightyears = parsec * 3.26156

print(str (parsec) + " parsecs son: " + str(lightyears) + " lightyears")