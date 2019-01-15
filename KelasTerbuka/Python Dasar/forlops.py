gorengan = ["bakwan", "cireng", "tahu isi", "tempe goreng", "ubi goreng"]

for g in gorengan :
    print(g)
    print(len(g))


#string sebagai iterable

bakwan  = 'bakwan'

for i in bakwan :
    print(i)

#for didalam for
gorengan = ["bakwan", "cireng", "tahu isi", "tempe goreng", "ubi goreng"]
buah = ["semangka", "jeruk","apel", "anggur"]
sayur = ["kangkung", "wortel", "tomat", "kentang"]

DaftarBelanja = [gorengan,buah,sayur]

for subdaftarbelanja in DaftarBelanja:
    print(subdaftarbelanja)
    for komponen in subdaftarbelanja:
        print(komponen)

        


