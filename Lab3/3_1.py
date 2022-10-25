a= int(input("Wprowadz 1 licbe"))
b= int(input("wprowadz 2 liczbe"))
if a>b:
    (a,b)=(b,a)
while a<=b:
    print(a,end=" ")
    a+=1
