edat = int(input("Introdueix la teua edat: "))
if edat >= 18:
    print("Ets major dedat")
    restar = edat-18
    print("Ets major dedat desde fa ", restar, " anys")
else:
    print("Eres menor dedat")
    restar = 18-edat
    print("Et falten ", restar, " per a ser major dedat")

if edat >= 67:
    print("Estas jubilat/da/de")
    restar = edat-67
    print("Estas  ", restar, " anys jubilat/da/de")
else:
    restar = 67-edat
    print("Et falten ", restar, " anys per a jubilarte")
    