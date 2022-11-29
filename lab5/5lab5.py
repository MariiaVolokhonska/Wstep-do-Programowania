def person(wiek,imie="Itot"):
   '''funkcja wyoisuje wiek i imie.

   :param imie:
   :param wiek:
   :return:
   '''
   print(imie,wiek)

person("Marek",2)
person("Irngrid",6)
person(imie="Tomasz",wiek=42)
#print(person.__doc__)
#print(help(person))
person(12)