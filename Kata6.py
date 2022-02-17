
planets = ['Mercurio', 'Venus', 'Tierra', 'Marte', 'Jupiter', 'Saturno', 'Urano', 'Neptuno']
planets.append("Plutón")
print(planets)
nombrePlaneta = input("Dame el nombre de un planeta: ")
index = planets.index(nombrePlaneta);
print(index)
print("Es planeta mas cercano al sol es",planets[0],"y el planeta mas lejano es",planets.pop())
print(planets[0:index])
print(planets[index + 1:])