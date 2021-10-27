aream=0
cost1m=0
cost2m=0

print("Costat1\t\tCostat2\t\tArea")

for x in range(10,31,1):
    cost1=x
    cost2=100-2*x
    area=cost1*cost2
    print(cost1,"\t\t",cost2,"\t\t",area)
    
    if area>aream:
        aream=area
        cost1m=cost1
        cost2m=cost2

print("Larea maxima es ",aream," per a uns costarts de ",cost1m," i ",cost2m)