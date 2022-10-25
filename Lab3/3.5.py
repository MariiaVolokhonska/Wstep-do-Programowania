n=int(input("Ile studentow"))
t=n
s=0
while n>0:
    k=int(input("Wprowadz punkt"))
    s=s+k
    n-=1
print("Szrednie: ",s/t)