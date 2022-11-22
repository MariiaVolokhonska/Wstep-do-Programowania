values=[10,20,30]
keys= ['ten','twenty','thirty']
D=dict(zip(values,keys))
print(D)
D1=dict(thirty=30,forty=40,fifty=50)
print(D1)
D.update(D1)
print(D)
D3={}
D4={}
for i in range(len(keys)):
    D3[keys[i]]=values[i]
print(D3)
D4={keys[i]:values[i] for i in range (len(keys))}