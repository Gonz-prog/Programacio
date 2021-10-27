print("1. bicicleta")
print("2. moto")
print("3. cotxe")
print("4. camio")
print("5. eixir")

sel=int(input("Selecciona una opcio: "))

imp=100

while sel<=0 or sel>=6:
    print("Donam una instruccio valida")
    sel=int(input("Selecciona una opcio: "))
    
if sel==1:
    print("Import = ",imp)

elif sel==2:
    km=int(input("Kilometres: "))
    print("Import = ",imp+30*km)

elif sel==3:
    km=int(input("Kilometres: "))
    print("Import = ",imp+30*km)

elif sel==4:
    km,ton=input("Kilometres i tones: ").split()
    print("Import = ",imp+30*int(km)+25*int(ton))

elif sel==5:
    print("Fi del programa")
