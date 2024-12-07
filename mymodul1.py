def LuasLingkaran():
    jari_jari = int(input("Masukkan jari-jari lingkaran: "))
    hitung_luas = 3.14 * (jari_jari ** 2)
    print(f"Luas lingkaran dengan jari-jari {jari_jari} cm adalah {hitung_luas}")

def LuasPersegi():
    sisi = int(input("Masukkan panjang sisi persegi: "))
    hitung_luas = sisi ** 2
    print(f"Luas persegi dengan panjang sisi {sisi} cm adalah {hitung_luas}")

def LuasSegitiga():
    alas = int(input("Masukkan alas segitiga: "))
    tinggi = int(input("Masukkan tinggi segitiga: "))
    hitung_luas = alas * tinggi / 2
    print(f"Luas segitiga dengan alas {alas} cm dan tinggi {tinggi} cm adalah {hitung_luas}")

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