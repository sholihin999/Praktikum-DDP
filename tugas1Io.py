# Input data pegawai
nama_pegawai = input("Masukkan nama pegawai: ")
divisi = input("Masukkan divisi: ")
agama = input("Masukkan agama: ")
jabatan = input("Masukkan jabatan (staff/kabag/manager): ")

# Menentukan gaji pokok berdasarkan jabatan
if jabatan == "staff":
    gaji_pokok = 4000000  # 4 juta
elif jabatan == "kabag":
    gaji_pokok = 7000000  # 7 juta
elif jabatan == "manager":
    gaji_pokok = 10000000  # 10 juta
else:
    gaji_pokok = 0  # Jika jabatan tidak terdaftar

# Menghitung tunjangan jabatan
tunjangan_jabatan = 0.2 * gaji_pokok

# Menghitung gaji kotor
gaji_kotor = gaji_pokok + tunjangan_jabatan

# Menghitung zakat
zakat = (0.025 * gaji_kotor) if (agama == "islam" and gaji_kotor >= 7000000) else 0

# Menghitung gaji bersih
gaji_bersih = gaji_kotor - zakat

# Mencetak hasil
print(f"Nama                : {nama_pegawai}")
print(f"Agama               : {agama}")
print(f"Divisi              : {divisi}")
print(f"Jabatan             : {jabatan}")
print(f"Gaji Pokok          : Rp {gaji_pokok:,.2f}")
print(f"Tunjangan Jabatan   : Rp {tunjangan_jabatan:,.2f}")
print(f"Gaji Kotor          : Rp {gaji_kotor:,.2f}")
print(f"Zakat Profesi       : Rp {zakat:,.2f}")
print(f"Gaji Bersih         : Rp {gaji_bersih:,.2f}")