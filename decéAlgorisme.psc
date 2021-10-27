Algoritmo Valors
	Escribir 'Introdueix dos valors'
	Leer a
	Leer b
	Si a>b Entonces
		Escribir a,' > ',b
	SiNo
		Repetir
			a <- a+2
			b <- b-3
		Hasta Que a>b
	FinSi
	Escribir a,' > ',b
FinAlgoritmo
