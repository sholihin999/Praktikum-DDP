def hitungGaji() :
    nama = input("Masukkan nama\t\t: ")
    jabatan = input("Jabatan Anda (Manager/Asisten Manager/Supervisor/Staff)\n \t\t\t: ")
    agama = input ("Agama \t\t\t: ")
    status = input("Status Pernikahan\t: ")

    def gapok():
        match jabatan:
            case "Manager":
                return 15000000
            case "Asisten Manager":
                return 10000000
            case "Supervisor":
                return 7000000
            case "Staff":
                return 4000000
            case _:
                return 0

    tunjab = 0.3 * gapok()
    BPJS = 0.1 * gapok()

    def tunkel(s):
        match s:
            case "Ya"|"Iya"|"Done"|"Sudah"|"Menikah" :
                return 0.1 * gapok()
            case _:
                return 0
    
    gator = gapok() + tunjab + BPJS + tunkel(status)

    def zakat_profesi():
        return (0, 0.025 * gator)[agama == "Islam" and gator >= 7000000]
    
    gaber = gator - zakat_profesi()

    print("=========== Slip Gaji Pegawai ===========",
            "\nNama Pegawai\t\t: ", nama,
            "\nJabatan\t\t\t: ", jabatan,
            "\nAgama\t\t\t: ", agama,
            "\nStatus Pernikahan\t: ", status,
            "\nGaji Pokok\t\t: ", gapok(),
            "\nTunjangan Jabatan\t: ", tunjab, 
            "\nBPJS\t\t\t: ", BPJS,
            "\nTunjangan Keluarga\t: ", tunkel(status),
            "\nGaji Total\t\t: ", gator,
            "\nZakat Profesi\t\t: ", zakat_profesi(),
            "\nGaji Bersih\t\t: ", gaber,
            "\n=========================================")
    
hitungGaji()