list_makanan = [
    ['Bakwan','Combro','Misro','Tahu','Tempe'],
    ['Sop Iga','Sop Buntut','Sop Ayam','Soto Mie'],
    ['Nasi Uduk','Nasi Goreng','Nasi Rames','Nasi Padang'],
]

#cetak makanan
print('------Cetak Makanan Tertentu------')
print(list_makanan[0][3]) #tahu
print(list_makanan[1][3]) #soto mie
print(list_makanan[2][3]) #Nasi Padang

#nested loop
print('------Cetak Semua Makanan------')
for menu in list_makanan:
    for food in menu:
        print(food) #mencetak semua menu makanan