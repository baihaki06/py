#scope variable global

NamaKucing = "casandra"
MakananKucing = "Royal canin"

def RubahNamaKucing(NamaBaru):
    global NamaKucing
    NamaKucing = NamaBaru
    nama = NamaBaru
    print("saya rubah nama kucing jadi : ", nama)

def KasihMakanKucing(makanan, nama):
    global NamaKucing, MakananKucing
    NamaKucing = nama
    MakananKucing = makanan

RubahNamaKucing('kettie')

KasihMakanKucing('universal', 'alex')

print("nama kucing saya menjadi ", NamaKucing, "dan Makan ", MakananKucing)