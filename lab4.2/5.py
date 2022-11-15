import random
punkty=[float(round(random.uniform(0,50),2)) for i in range(15)]
list1=[]
list2=[]
t=max(punkty)
m=min(punkty)
s1=0
s2=0
print("Najwieksza liczba: ",t)
print("Najmniejsza liczba: ",m)
l=float(input("Wprowadz liczbe"))
if l in punkty:
    print(l)
elif l not in punkty:
    print("W listu nie ma danej liczby")
else: print("To nawet nie liczba....")
suma=0
r= sum(punkty)
u=r/len(punkty)
print("Szreidnie:",round(u,2))
for i in range(15):
    if u>=punkty[i]:
        s1+=1
        list1.append(punkty[i])
    elif u<punkty[i]:
        s2+=1
        list2.append(punkty[i])
print("Ilosc wiecej za srednie",s1)
print("Ilosc miencej za srednie",s2)
print("Ponirzej sderniej:",list1)
print("Powyrzej sredniej",list2)