import mymodul1
def main():
    while True:
        pilihan = str(input("Silahkan pilih bangun datar yang ingin dihitung luasnya (1. Luas lingkaran, 2.Luas persegi, 3. Luas Segitiga): "))
        if pilihan == "1":
            mymodul1.LuasLingkaran()
        elif pilihan == "2":
            mymodul1.LuasPersegi()
        elif pilihan == "3":
            mymodul1.LuasSegitiga()
        else:
            print("Pilihan tidak ada bro, aneh lu yang gaada malah lu pilih KOCAK")
main()