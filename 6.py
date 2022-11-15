x=[]
for i in range(10):
    t=input()
    x.append(t)
for i in range(1,4,1):
    x.insert(0,x[-i])
del x[-4:]
print(x)
