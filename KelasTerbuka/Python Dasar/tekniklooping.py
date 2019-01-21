#teknik looping

NamaBand = [
    "Payung Teduh",
    "Fourtwnty",
    "Dialog Dini hari",
    "Mr.Sonjaya",
    "Parahyena"
]

KumpulanLagu = [
    "Akad",
    "Zona Nyaman",
    "Rumahku",
    "Sang Filsuf",
    "sindoro"
]

#enumerate
for  nomor,band in enumerate(NamaBand):
    print(nomor, ":", band)

#zip
for band,lagu in zip(NamaBand,KumpulanLagu):
    print(band, "Menyanyikan lagu :", lagu)

#set
PlayList = {"baby baby", "jejak langkah", "khayalan tingkat tinggi", "jarang Goyang", "ada apa", "kuda"}

for lagu in sorted(PlayList):
    print(lagu)

#dictionary
PlayList2 = {
    "payung teduh": "Akad",
    "fortwnty": "Zona Nyaman",
    "dialog dini hari":"Rumahku"
}

for i,v in PlayList2.items():
    print(i, "Lagunya :", v)

for i in reversed(range(1,10,1)):
    print(i)