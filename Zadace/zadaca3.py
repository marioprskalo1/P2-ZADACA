#Potrebno napisati regex koji vraca podudaranje ukoliko se unese string koji počinje kao prvo slovo vašeg imena,
#a završava kao prvo slovo prezimena. String mora sadržavati bar jedan broj između 0 i 5 i razmak.

import re


regex = "^A[a-z]*[0-5]+ g$"

while 1:
    tekst= input("Unesi tekst: ")
    rezultat = re.findall(regex,tekst)
    if rezultat:
        break
print("Doslo je do podudaranja.")
    


