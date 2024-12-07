print("----Gunakan Modul Secara Langsung----")
import mod_hitung
mod_hitung.tambah(9, 3)
mod_hitung.tambah(5, 4)
mod_hitung.kurang(5, 3)
mod_hitung.kali(2, 3)
mod_hitung.bagi(6, 3)
mod_hitung.pangkat(2, 3)

print("\n----Gunakan Modul Dialiaskan----")
import mod_hitung as hitung
hitung.tambah(9, 3)
hitung.tambah(5, 4)
hitung.kurang(5, 3)
hitung.kali(2, 3)
hitung.bagi(6, 3)
hitung.pangkat(2, 3)

print("\n----Gunakan Modul Sebagain Fungdi----")
from mod_hitung import kali, bagi, pangkat
kali(10, 3)
bagi(90, 3) 
pangkat(4, 3)

print("\n----Gunakan Modul Semua Fungsi----")
from mod_hitung import *
tambah(9, 3)
kurang(5, 3)
kali(2, 3)
bagi(6, 3)
pangkat(2, 3)

print("\n----Gunakan Modul, Fungsi Dialiaskan----")
from mod_hitung import kali as k, bagi as b, pangkat as p
k(10, 3)
b(90, 3)
p(4, 3)