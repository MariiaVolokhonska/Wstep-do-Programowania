zwierzenta=[]
n=0
while n<=10:
    a=input("Podaj nazwe")
    zwierzenta.append(a)
    n += 1

print(zwierzenta)
zwierzenta.sort()
print(zwierzenta)
print(zwierzenta[0], zwierzenta[2:5])
print("Ilosc:",len(zwierzenta))