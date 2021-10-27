Algoritmo Divisores
	cont <- 0
	Escribir 'Introduce un numero y te digo sus divisores'
	Leer n
	Para i<-1 Hasta n Hacer
		Si n%i==0 Entonces
			cont <- cont+1
			Escribir i,' es divisor de ',n
		FinSi
	FinPara
	Escribir n,' tiene ',cont,' divisores'
FinAlgoritmo
