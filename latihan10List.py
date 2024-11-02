#membuat struktur data list baru
ar_buah = ['Pepaya','Mangga','Pisang','Jambu','Belimbing']

#ganti buah pisang dnegan apel
ar_buah[2] = 'Apel'

#mengahpus buah belimbing
del ar_buah[4]

#tambah element list
ar_buah.insert(2,'Naga')
ar_buah.append('Jeruk')
ar_buah.append('Salak')
ar_buah.append('Melon')
ar_buah.append('Manggis')

#cetak
print('------------All Buah-------------')
for buah in ar_buah:
    print('buah',buah)
    
print('------------Potongan Buah-------------')
print('Buah', ar_buah[3:6])