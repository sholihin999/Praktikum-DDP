class gempa:
    #atribut
    lokasi = ""
    skala = 0

    #konstruktor
    def __init__(self, lokasi="-",skala=0):
        self.lokasi = lokasi
        self.skala = skala

    #method
    def dampak(self):
        if(self.skala < 2):
            ket = "Gempa tidak terasa"
        elif(self.skala >= 2 and self.skala < 4):
            ket = "Gempa Menyebabkab Bangunan Retak-Retak"
        elif(self.skala >= 4 and self.skala < 6):
            ket = "Gempa Menyebabkan Bangunan Roboh"
        else:
            ket = "Gempa Menyebabkan Tsunami"
        print("Telah terjadi gempa di", self.lokasi, "dengan skala", self.skala, "ritcher", ket)

#instansiasi objek
bekasi = gempa("Bekasi", 3)
bandung = gempa("Bandung", 5)
bogor = gempa("Bogor", 2)
jakarta = gempa("Jakarta", 7)
malang = gempa()

#Cetak panggil method 
bekasi.dampak()
bandung.dampak()
bogor.dampak()
jakarta.dampak()
malang.dampak()