Algoritmo Linies
	Escribir 'Introdueix un nombre'
	Leer n
	cadena <- '1'
	suma <- 1
	Escribir cadena,' = ',suma
	Para i<-2 Hasta n Hacer
		cadena <- cadena+' + '+convertirATexto(i)
		suma <- suma+i
		Escribir cadena,' = ',suma
	FinPara
FinAlgoritmo
