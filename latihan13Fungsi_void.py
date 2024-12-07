#membuat function void define by user
def hitungUmur(tahun_Sekarang):
    nama = input("Masukkan nama anda: ")
    tahun_lahir = int(input("Masukan tahun lahir anda: "))
    umur = tahun_Sekarang - tahun_lahir
    print ("Mahasiwa a.n %s yang lahir pada tahun %i saat ini berumur %2.f tahun" % (nama, tahun_lahir, umur))

#panggil function
hitungUmur(2024)