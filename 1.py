print("Wprowadz wiek klienta")
x= int(input())
if x<4:
    print("Wstep bezplatny")
elif 4<=x<18:
    print("10 zl")
elif x>=18:
    print("20 zl")