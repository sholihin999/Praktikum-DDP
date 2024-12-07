#dictionary
p1 = {'nama' : 'Budi', 'jabatan' : 'Manager', 'agama' : 'Islam', 'status' : 'Menikah'}
p2 = {'nama' : 'Siti', 'jabatan' : 'Asisten manager', 'agama' : 'Islam', 'status' : 'Menikah'}
p3 = {'nama' : 'I Gede ', 'jabatan' : 'Supervisor', 'agama' : 'Hindu', 'status' : 'Menikah'}
p4 = {'nama' : 'Joko', 'jabatan' : 'Staf', 'agama' : 'Islam', 'status' : 'Belum Menikah'}
p5 = {'nama' : 'Alex', 'jabatan' : 'Staf', 'agama' : 'Kristen Prosten', 'status' : 'Belum Menikah'}

#list dictionary
list_dictionary = [p1, p2, p3, p4, p5]

#menghitung dan mencetak slip gaji pegawai
#gaji pokok (kondisional if)
for pegawai in list_dictionary:
    if pegawai['jabatan'] == 'Manager' :
        pegawai['gaji_pokok'] = 15000000
    elif pegawai['jabatan'] == 'Asisten manager' :
        pegawai['gaji_pokok'] = 10000000
    elif pegawai['jabatan'] == 'Supervisor' :
        pegawai['gaji_pokok'] = 7000000
    elif pegawai['jabatan'] == 'Staf' :
        pegawai['gaji_pokok'] = 4000000
    else :
        pegawai['gaji_pokok'] = 0
    
    #tunjangan jabatan (30% dari gaji pokok)
    pegawai['tunjangan_jabatan'] = pegawai['gaji_pokok'] * 30/100
            
    #BPJS (10% dari gaji pokok)
    pegawai['bpjs'] = pegawai['gaji_pokok'] * 10/100
    
    #tunjangan keluarga (Tuple & list)
    pegawai['tunjangan_keluarga'] = (0, pegawai['gaji_pokok'] * 0.1)[pegawai['status'] == 'Menikah']
    
    #gaji kotor 
    pegawai['gaji_kotor'] = pegawai['gaji_pokok'] + pegawai['tunjangan_jabatan'] + pegawai['bpjs'] + pegawai['tunjangan_keluarga']
    
    #zakat profesi (Tuple & list)
    pegawai['zakat_profesi'] = (0, pegawai['gaji_kotor'] * 2.5/100)[pegawai['agama'] == 'Islam' and pegawai['gaji_kotor'] >= 7000000]
    
    #gaji bersih
    pegawai['gaji_bersih'] = pegawai['gaji_kotor'] - pegawai['zakat_profesi']
    
    #cetak slip gaji
    print('=========== Slip Gaji Pegawai ===========')
    print(f"Nama \t\t\t: {pegawai['nama']} "
          f"\nJabatan \t\t: {pegawai['jabatan']}"
          f"\nAgama \t\t\t: {pegawai['agama']}"
          f"\nStatus \t\t\t: {pegawai['status']}"
          f"\nGaji Pokok \t\t: {pegawai['gaji_pokok']}"
          f"\nTunjangan Jabatan \t: {pegawai['tunjangan_jabatan']}"
          f"\nBPJS \t\t\t: {pegawai['bpjs']}"
          f"\nTunjangan Keluarga \t: {pegawai['tunjangan_keluarga']}"
          f"\nGaji Kotor \t\t: {pegawai['gaji_kotor']}"
          f"\nZakat Profesi \t\t: {pegawai['zakat_profesi']}"
          f"\nGaji Bersih \t\t: {pegawai['gaji_bersih']}"
          )
    print('========================================\n')
    
