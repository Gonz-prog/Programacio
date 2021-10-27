import time


def areaRectangle(base, altura):


return base*altura

base = int(input("Dis-me la base del rectangle: "))
altura = int(input("Dis-me l'altura del rectangle: "))
time.sleep(2)  # Espera dos segons

area = areaRectangle(base, altura)

print("L'àrea del rectangle és " + str(area))
