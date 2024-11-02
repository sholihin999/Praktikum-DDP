gender = ('laki-laki','perempuan')
umur = ('0-10', '11-20', '21-30', '31-40', '41-50', '51-60')

#budi adalah muris smp  dengan umur dan berjenis kelamin laki-laki
print(f"Budi adalah seorang murid SMP dengan umur {umur[1]} dan berjenis kelamin {gender[0]}")
#Mawar adalah seorang mahasiswi semester akhir dengan umur..  dan berjenis kelamin perempuan
print(f"Mawar adalah seorang mahasiswi semester akhir dengan umur {umur[2]} dan berjenis kelamin {gender[1]}")
#Menghitung Jumlah Item Pada variabel
print(f'jumlah item pada variabel gender ada {len(gender)} sedangkan item pada variabel umur ada {len(umur)}')

#nested tuple
makanan = ['Mie Ayam', 'Karedok', 'Ayam Penyet', 'Pecel Lele'],
minuman = ['Es teh', 'Es Jeruk', 'Es Kelapa','Es Campur'],
dissert = ['Es Krim', 'Pisang Goreng', 'Puding']

menu = (makanan,minuman,dissert)
print(menu[1])
print(menu[2][1])
print(menu)



