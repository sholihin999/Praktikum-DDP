#Belajar looping for

print("---------------Cetak Angka 1 Sampai Dengan 15-----------------")
angka = 15
for no in range(angka):
    #no = no + 1
    no += 1  #increment
    print("Angka", no)

print("---------------Cetak Angka 5 Sampai Dengan 25-----------------")
awal = 5
akhir = 25
step =1
for no in range(awal,akhir,step):
    print("Angka", no)
    no += 1
    
print("---------------Cetak Bilanagan Ganjil Angka 5 Sampai Dengan 25-----------------")
awal = 5
akhir = 25
step =2
for no in range(awal,akhir,step):
    #login modulus
    if(no % 2 == 1):
        print("Angka", no)
        no += 1
    