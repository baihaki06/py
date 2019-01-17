Barang = ["kunci", "ember", "jaket", "ban", "mobil"]
print(Barang)


#beberapa method yang bisa dipakai untuk memanipulasi list

Barang.append("sepeda")
print(Barang)

Barang.extend("dompet")
print(Barang)

Barang.insert(3, "sepeda")
print(Barang)


Jumlahsepeda = Barang.count("sepeda")
print("Jumlah sepada yang ada dalam list :",Jumlahsepeda)

Barang.remove("sepeda")
print(Barang)

Barang.reverse()
print(Barang)

print("+"*100)

stuff = Barang.copy()

stuff.append("gelas")
print(stuff)
print(Barang)