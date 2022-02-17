planetaNuevo = ''
planets = []
while planetaNuevo.lower() != "done":
    planetaNuevo = input("Agrega los planetas que quieras, cuando acabes escribe done: ")
    planets.append(planetaNuevo)
for i in planets:
    print(i)