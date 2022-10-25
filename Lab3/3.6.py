n=int(input("Ile studentow"))
b=True
t=0
s=0
k=0
while b:
    if t > 100:
        while t <= n:
            t += 1
            continue
    if t >= n:
        break
    k+=1
    s=s+k
    t+=1
print("Szrednie: ",s/n)