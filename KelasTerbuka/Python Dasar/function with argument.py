#fungsi dengan mengunakan argumen biasa

def siswa(nama):
    print("siswa ini bernama: " , nama)

siswa("mario")

#fungsi dengan keyword arguments
def guru(nama, pelajaran):
    print("guru ini bernama :", nama)
    print("mengajar ", pelajaran)

guru(nama="bai", pelajaran="Python")
guru(pelajaran="javaScript", nama="Baihaki")
guru("bai","kotlin")

#fungsi dengan default argument
def PenjagaSekolah(nama, shif="siang", galak="tidak"):
    print("penjaga sekolah ini bernama : ", nama)
    print("shifnya ", shif)
    print("galak? ", galak)

PenjagaSekolah("asep")
PenjagaSekolah("maman", shif="malam")
PenjagaSekolah("Didi", galak="sangat")
#PenjagaSekolah(galak="iya", shif="malam") #jadi error


