#membuat fungsi sederhana

def SuaraAyam():
    print("kukuruyukkkk!!!")

def HargaAyam():
    SuaraAyam()
    print("harga ayam persatu kilo adalah 20 ribu")

def HargaTotalAyam(kg):
    SuaraAyam()
    harga = 2000
    HargaTotal = kg * harga
    print("harga", kg,  "kg ayam  adalah", HargaTotal)

HargaAyam()

HargaTotalAyam(2)
HargaTotalAyam(0.5)
HargaTotalAyam(1)
HargaTotalAyam(9)