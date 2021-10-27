Algoritmo While
	Escribir 'Digam un any de naixement i un de defuncio' 
	Leer naix
	Leer mort
	Mientras naix>mort Hacer
		Escribir 'No es pot morir abans de naixer'
		Escribir 'Digam un any de naixement i un de defunció raonable'
		Leer naix
		Leer  mort	
	FinMientras
	vida <- mort-naix
	Escribir 'Ha viscut '  ,vida,  ' anys'
FinAlgoritmo
