#class

class Mahasiswa():
    nama = 'nama'

    def belajar(self, kondisi):
        print(self.nama, 'sedang belajar', kondisi)

    def tidur(self):
        print(self.nama, 'tidur dikelas')


#main program nya

otong = Mahasiswa()
ucup = Mahasiswa()

otong.nama = "otong surotong"
ucup.nama = "micheal ucup"

otong.belajar('dengan giat')
ucup.tidur()