#class

class Mahasiswa():
    nama = 'nama'

    def __init__(self, input_nama, input_nim):
        self.nama = input_nama
        self.nim = input_nim

    def belajar(self, kondisi):
        print(self.nama, 'sedang belajar', kondisi)

    def tidur(self):
        print(self.nama, 'tidur dikelas')


#main programnya

otong = Mahasiswa("otong surotong", 12319800)

print(otong.nama)


otong.nama = 'otong suratang'

print(otong.nama)


otong.belajar('dengan giat')

