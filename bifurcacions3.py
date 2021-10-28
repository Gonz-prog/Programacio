#Fes un programa que pregunte quants anys té algú i que 
#mostre per pantalla la quantitat d’anys
#que li falten per a la majoria d’edat i per a jubilar-se


edat=int(input("Digam els anys que tens! "))

if edat<18:
    
    res=18-edat

    res1=65-edat

    print("Ets menor dedat et falten",res,"anys per als 18 i",res1,"per a jubilarte")

elif edat>65:

    print("Ets jubilat")

else:

    res1=65-edat

    print("Ets major dedat i et falten",res1,"anys per a jubilarte")