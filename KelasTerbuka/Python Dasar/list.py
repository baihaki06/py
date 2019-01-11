Data = [1,4,9,14,25,36,49,64]

#mengakses data
subdata = Data[3]
subdata2 = Data[-3]
subdata3 = Data[2:4]
subdata4 = Data[:4]
subdata5 = Data[:]

#cetak data
print(subdata)
print(subdata2)
print(subdata3)
print(subdata4)
print('subdata5')
print(subdata5)
#mengabungkan list
Data2 = [100,200,300,400,500,600,700,800]

Data3 = Data + Data2

print(Data3)

#mencopy list kedalam variable baru
a = Data3[:]
print(a)

#merubah conten dari list
a[10] = 30
print(a)

#merubah content list dengan metode slicing
Data3[3:4] = [11,12]
print(Data3)

#list dalam list
x = [Data, Data2]
print(x)

#mengakses list dalam multi dimension list
y = x[1][4]
z = x[0][2]

print(y)
print(z)

Data3.append(456)

print(Data3)

#menghitung panjang list
PanjangList = len(Data3)

print(PanjangList)