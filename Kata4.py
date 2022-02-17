text = """Interesting facts about the Moon. The Moon is Earth's only satellite. There are several interesting facts about the Moon and how it affects life here on Earth. " \n "On average, the Moon moves 4cm away from the Earth every year. This yearly drift is not significant enough to cause immediate effects on Earth. The highest daylight temperature of the Moon is 127 C."""

parts = text.split('. ')
parts


words = ["average","temperature","distance"]


for i in parts:
    for y in words:
      if y in i:
        print(i.replace('C','Celsius'))
        break    


name = "Luna"
gravity = 0.00162 *1000 # in kms
planet = "Tierra"
print(("\nLa gravedad de la tierra \n------------------------------------------------------- \nTenemos datos sobre: %s \nNombre del planeta: %s \nGravedad en Ganymede: %s m/s2 " %(name, planet, gravity)).title())