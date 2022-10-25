a= int(input("Wprowadz 1 licbe"))
b= int(input("wprowadz 2 liczbe"))
s=' '
if a>b:
    (a,b)=(b,a)
while a<=b:
    if (a%2==0):
        print(a,end=" ")
        a += 1
    elif (a%2!=0):
        a += 1
        continue

