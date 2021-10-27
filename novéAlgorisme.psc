Algoritmo Nombres
	Escribir 'Donam un nombre inicial'
	Leer in
	Escribir 'Donam ara un nombre final	'
	Leer fi
	pa <- 0
	im <- 0
	Para i<-in Hasta fi Hacer
		Escribir i
		Si i%2==0 Entonces
			pa <- pa+i
		SiNo
			im <- im+i
		FinSi
	FinPara
	Escribir 'El resultat dels parells es ',pa 
	Escribir 'la suma dels imparells es ',im
FinAlgoritmo
