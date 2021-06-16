from csv import reader
# open file in read mode
with open('rezultati.csv', 'r') as read_obj:
    # pass the file object to reader() to get the reader object
    csv_reader = reader(read_obj)
    # Get all rows of csv from csv_reader object as list of tuples
    rezultati = list(map(tuple, csv_reader))
    # display all rows of csv
    rezultati.sort()
    #print(rezultati)
print("-"*20)
ocjene={}
for ime,prezime,bodovi in rezultati:
        if int(bodovi)<49:
                ocjene[ime]=1
        elif int(bodovi)>49 and int(bodovi)<64:
                ocjene[ime]=2
        elif int(bodovi)>64 and int(bodovi)<79:
                ocjene[ime]=3
        elif int(bodovi)>79 and int(bodovi)<89:
                ocjene[ime]=4
        elif int(bodovi)>89 and int(bodovi)<=100:
                ocjene[ime]=5
                
                
novi_rezultati = []
for ime, prezime, bodovi in rezultati:
	novi_rezultati.append((bodovi, prezime, ime))
	
novi_rezultati.sort(reverse=True)
print(novi_rezultati)
		
		
for bodovi, prezime, ime in novi_rezultati:
	print("Bodovi:" ,bodovi, prezime, ime, "Ocjena:", ocjene[ime])








