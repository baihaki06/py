class mahasiswa():

    jurusan = "teknik komputer"
    __nilai = 0 #private

    def __init__(self, input_nama, input_nilai):
        self.nama = input_nama
        self.nilai = input_nilai


    def uts(self, input_nilai):
        self.__nilai += input_nilai

    def uas(self, input_nilai):
        self.__nilai += input_nilai

    def cek_status(self):
        if self.__nilai <= 50:
            print(self.nama, "Tidak Lulus")
        else:
            print(self.nama, "lulus")

amin  = mahasiswa("Muh Amin", 12123456)
dara = mahasiswa("dara Nur", 12134543)

amin.uts(10)
amin.uas(30)

amin.cek_status()

dara.uts(80)
dara.uas(55)
dara.__nilai =70
dara.cek_status()