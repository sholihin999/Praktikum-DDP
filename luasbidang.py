print("-------------------")
print("Luas Bidang")
print("-------------------")
print("Pilih Bidang:",
      "\n1. Segitiga",
      "\n2. Lingkaran",
      "\n3. Persegi Panjang")
pilihan = int(input("\n Masukan Pilihan: "))

#percabangan
#segitiga
if(pilihan == 1):
    alas = eval(input("Masukan alas: "))
    tinggi = eval(input("Masukan tinggi: "))
    
    #hitung luas segitiga
    hasil = alas *  tinggi / 2
    print(f"Hasil dari perhitungan luas  segitiga adalah: {hasil}")
    
#lingkaran
elif(pilihan == 2):
    jari = eval(input("Masukan jari-jari: "))
    
    #hitung luas
    luas = 3.14 * jari ** 2
    print(f"Hasil dari perhitungan luas lingkaran adalah: {luas}")
    
#persegi panjang
elif(pilihan == 3):
    panjang = eval(input("Masukan panjang: "))
    lebar = eval(input("Masukan lebar: "))
    
    #hitung luas
    luaspersegipanjang = panjang * lebar
    print(f"Hasil dari perhitungan luas persegi panjang adalah: {luaspersegipanjang}")
    
else:
    print("Pilihan tidak tersedia")
    
print("\n Program selesai")






