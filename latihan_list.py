#latihan bareng asdos

toping_seblak = ['Sosis', 'Baso', 'Jamur Enoki', 'Ceker']
print('-----------toping seblak pilihan-----------')
print(toping_seblak[1])

#hapus toping index 3 yaitu ceker
del toping_seblak[3]

#print toping dengan berjejer kesamping
print('-----------Semua toping seblak kesamping-----------')
print(toping_seblak)

#print toping dengan berjejer kebawah
print('-----------Semua toping seblak kebawah-----------')
for topping in toping_seblak:
    print(topping)
    
#nambahin dumpling keju di antara sosis dan baso
toping_seblak.insert(1, 'Dumpling Keju')
#nambahin toping diakhir list
toping_seblak.append('Makaroni')
print(toping_seblak)

#memotong list
print(toping_seblak[0:3])
print(toping_seblak[1:4])