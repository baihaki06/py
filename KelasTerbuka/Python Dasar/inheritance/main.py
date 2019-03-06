class Ojek():

    def __init__(self, nama, tranmisi, daerah):
        self.nama = nama
        self.tranmisi = tranmisi
        self.daerah = daerah

    def cekIdAbang(self):
        print('nama', self.nama, '\nmotor', self.tranmisi, '\ndaerah : ',self.daerah)


class Gojek(Ojek):

    def cekIdAbang(self):
        print('cek aplikasi gojek')


ojek1 = Ojek('mario', 'manual', 'bandung kota')
ojek2 = Gojek('jackson', 'matik', 'bekasi')

ojek1.cekIdAbang()
ojek2.cekIdAbang()

