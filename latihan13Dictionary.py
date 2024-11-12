nilai = {'firda' : 89, 'inaya' : 100, 'deden' : 59, 'fawaz' : 95}

#akses nilai dictionary
print("Nilai firda : ", nilai['deden'])

#Tambah nilai dictionary
nilai['inayaa'] = 80
nilai['aldi'] = 100

print("-----------------------------------")

#looping semua key
for i in nilai.keys() :
    kalimat = f"Nilai {i} adalah {nilai[i]}"
    print(kalimat)
    
print("-----------------------------------")

#Ubah nilai inaya 
nilai['inaya'] = 90

#hapus nilai aldi
nilai.pop('aldi')

#looping semua value
for v in nilai.values() :
    print(v)
    
print("-----------------------------------")

print("================ Cetak Items =================")
#looping items
for k,v in nilai.items() :
    kalimat = f"Nilai {k} adalah {v}"
    print(kalimat)