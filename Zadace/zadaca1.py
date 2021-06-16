#Koristeći listu imena iz prethodnog zadatka svakom studentu generirati nasumičnu ocjenu od 1 do 5.
#Prebrojati u rječnik koliko ima kojih ocjena.
#Izračunati postotak prolaznosti. (sve ocjene veće od 1)
import random
imena=['Josip', 'Ivan', 'Ivan', 'Josip', 'Ivan', 'Ivan', 'Katarina', 'Božena', 'Ivona', 'Marija', 'Josipa',
         'Marko', 'Dario', 'Mihael',
         'Stana', 'Bruno', 'Anamarija', 'Andrea', 'Petar', 'Marko', 'Amnesa', 'Nikola', 'Antonela', 'Leon',
         'Ivan', 'Ante', 'Ivan',
         'Jure', 'Jan', 'Florijan', 'Boris', 'Ivan', 'Stipe', 'Damir', 'Ana', 'Tin', 'Iva', 'Kristina', 'Josip',
         'Tomislav', 'Luka', 'Ivan',
         'Martin', 'Marko', 'Ante', 'Nikolina', 'Ivan', 'Toni', 'Ante', 'Darija', 'Dominik', 'Lucija', 'Luka',
         'Ana', 'Emanuel',
         'Petar', 'Matej', 'Stjepan', 'Josip', 'Luka', 'Marija', 'Toni', 'Iva ', 'Perica', 'Antonio', 'Ante',
         'Marijan', 'Mario',
         'Antonio', 'Stipe', 'Filip', 'Ivan', 'Ivan', 'Luka', 'Ante Bruno', 'Ivan', 'Vinko', 'Ivan', 'Matijas',
         'Ivan', 'Freda', 'Kristina',
         'Josip', 'Lucija']


ocjene={}
for student in imena:
    ocjene[student]=random.randint(1,5)
    
jedan=0
dva=0
tri=0
cet=0
pet=0

for v in ocjene.values():
    if v == 1:
        jedan+=1
    elif v == 2:
        dva+=1
    elif v == 3:
        tri+=1
    elif v==4:
        cet+=1
    elif v==5:
        pet+=1
ukupno=dva+tri+cet+pet      

duljina= len(imena)
postotak=(ukupno/duljina)*100
for ime, ocjena in ocjene.items():        
    print(ime,ocjena)
    
print("Nedovoljno: ",jedan,
      "|Dovoljno: ",dva,
      "|Dobro: ",tri,
      "|Vrlo dobro: ",cet,
      "|Odlicno: ", pet)
print("Postotak prolaznosti: ", round(postotak,2))

