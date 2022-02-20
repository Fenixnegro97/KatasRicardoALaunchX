planet ={
    'nombre' : 'Marte',
    'lunas' : 2
}

print("El planeta " + planet.get('nombre') + " tiene " + str(planet.get('lunas')) + " lunas")
planet['Polar'] = 6752
planet['equatorial'] = 6792

print("El planeta " + planet.get('nombre') + " tiene de circuferencia polar de: " + str(planet.get('Polar'))  + " km \ny equatorial de: " + str(planet.get('equatorial')) + " km\n")

planeta_lunas = {
    'Mercurio': 0,
    'Venus': 0,
    'Tierra': 1,
    'Marte': 2,
    'Jupiter': 79,
    'Saturno': 82,
    'Uranos': 27,
    'Neptuno': 14,
    'Pluton': 5,
    'Haumea': 2,
    'Makemake': 1,
    'Eris': 1
}
totalLunas = 0
totalPlanetas = len(planeta_lunas.keys())

for LLave in planeta_lunas.keys():
    print(f"{LLave} tiene {planeta_lunas[LLave]} numero de lunas")
    totalLunas = planeta_lunas.get(LLave) + totalLunas


print("\nHay un total de: " + str(totalLunas) + " numero de lunas y su media es de : " + str(totalLunas/int(totalPlanetas)))
