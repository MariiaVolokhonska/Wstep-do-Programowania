imiona=['Kasia', 'Tomek', 'Jan', 'Ola', 'Jerzy', 'Marek', 'Piotr',
'Zuzia', 'Bartek', 'Jacek']
imiona[3]='Natalia'
imiona.insert(4,"Lola")
imiona.pop(6)
print(imiona)
for i in range(3):
    n=input()
    imiona.insert(i,n)
imiona[-1]="Dora"

print(imiona[1:4])
print(imiona[-3:])
