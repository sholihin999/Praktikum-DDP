string = ""
bar = 1
bebas = int(input ("masukkan jumlah baris: "))
#looping bintang menggunakan while
while bar <= bebas:
    col = bar 
    while col > 0:
        string +=  "*"
        col -= 1
    string += "\n"
    bar += 1 
print(string)