class mahasiswa():

    jumlah_mahaiswa = 0

    def __init__(self, input_nama, input_nilai):
        self.nama = input_nama
        self.nilai = input_nilai
        mahasiswa.jumlah_mahaiswa += 1


amin =  mahasiswa("Muh Amin", 121232123)
bai = mahasiswa("Baihaki", 12131516)
dara = mahasiswa("dara Nur", 34345656)



print(mahasiswa.jumlah_mahaiswa)

