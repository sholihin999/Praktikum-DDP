nama = input("Nama Mahasiswa: ")
bb = float(input("Berat Badan: "))
tb = float(input("Tinggi Badan: "))
imt  = bb/pow (tb,2)
#kondisifisik
if imt < 18.5: fisik =  "Kurus"
elif imt >= 18.5 and imt < 25: fisik = "Normal"
elif imt  >= 25 and imt < 30: fisik = "Kegemukan"
elif imt  >= 30: fisik = "Obesitas"
else:  fisik = "Tidak Diketahui"
#cetak
print("Nama Mahasiswa\t: %s"
      "\nBerat Badan\t: %.2f"
      "\nTinggi Badan\t: %.2f"
      "\nIMT\t\t: %.2f"
      %(nama,bb,tb,imt,fisik))
