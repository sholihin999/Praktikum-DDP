#Belajar Looping While

print("---------------Cetak Bil 50 - 100-----------------")
awal = 50
akhir = 100
while(awal <= akhir):
    print("Bilangan", awal)
    awal += 1
 
print("---------------Cetak Bil Genap 100 - 50-----------------")
starting = 100
ending = 50
while(starting >= ending):
    if starting % 2 == 0:
        print("Bilangan Genap", starting)
    starting -= 1