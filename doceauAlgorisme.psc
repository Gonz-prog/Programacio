Algoritmo BaseExponent
	Escribir 'Donam una base'
	Leer base
	Escribir 'Donam un exponent'
	Leer expo
	resultat <- base
	Si expo<2 Entonces
		Si expo==0 Entonces
			resultat <- 1
		FinSi
	SiNo
		Para i<-2 Hasta expo Hacer
			resultat <- resultat*base
		FinPara
	FinSi
	Si expo<0 Entonces
		Escribir 'No calcule exponents negatius'
	SiNo
		Escribir base,'^',expo,'=',resultat
	FinSi
FinAlgoritmo
