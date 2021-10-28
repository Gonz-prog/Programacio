#El servei d’endocrinologia de l’Hospital de La Ribera 
#necessita un programa que calcule el pes
#recomanat d’una persona. Escriu un programa que llija 
#l’altura en metres i l’edat d’una persona i
#mostre el seu pes recomanat segons la fórmula 
#pes = (altura_en_cm – 100 + 10%edat) * 0.9

alt=float(input("Quan medixes en metres: "))

edat=int(input("Quina edat tens? "))

pes=float(alt*100-100+edat/10)*0.9

print("El teu pes ideal es",pes)