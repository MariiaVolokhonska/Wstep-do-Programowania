def oblicz(a,b):
    return a+b, a-b
print("Pierwsza to suma, druga to roznica",oblicz(34,12),type(oblicz(34,12)))
x,y=oblicz(12.2,15.6)
print(f"Suma to{x},a ruznica to {y}")
