class Bank:
    #atribut / properti
    norek = ''
    nama = ''
    saldo = 0
    jmlNasabah = 0
    BANK = 'Bank Syariah Nurul Fikri'

    #method
    #konstruktor
    def __init__(self, norek, nasabah, saldo):
        self.norek = norek
        self.nama = nasabah
        self.saldo = saldo
        Bank.jmlNasabah += 1

    def cetak(self):
        print(Bank.BANK, 
                '\n=================================='
                '\nNo Rekening \t: ', self.norek,
                '\nNama Nasabah \t: ', self.nama,
                '\nSaldo \t\t: Rp.', format(self.saldo, ','),
                '\n=================================='
                )
    #method nabung tambah saldo
    def nabung(self, nominal):
        self.saldo += nominal
        print('\nNabung Berhasil !','Saldo Anda saat ini: Rp.', format(self.saldo, ','))
    
    #method tarik saldo
    def tarik(self, nominal):
        self.saldo -= nominal
        print('\nTarik Tunai Berhasil !','Saldo Anda saat ini: Rp.', format(self.saldo, ','))

#instansiasi objek
solihin = Bank('9105326', 'Solihin', 1000000)
anwar = Bank('9985276', 'Anwar', 2000000)

#cetak
# solihin.cetak()
solihin.nabung(500000)
solihin.tarik(300000)