nilai = 75

if nilai == 75: #equal eksplisit
    print("Nilai anda ", nilai)

if nilai is 60: #equal
    print("Nilai anda ", nilai)

if nilai is not 60 : #not equal
    print("Nilai anda bukan : 60")

print(100*"=")

nilai = 65

if 80 <=  nilai <= 100:
    print("Nilai anda adalah A")
elif 70 <= nilai  < 80:
    print("nilai anda adalah B")
elif 60 <= nilai < 70 :
    print("Nilai anda adalah C")
elif 50 <= nilai < 60 :
    print("Nilai anda adalah D, Lakukan HER")
else:
    print("Maaf anda Tidak lulus")

print("Operator Logika untuk List dan string")

gorengan = ["bakwan", "cireng", "bala-bala", "gehu", "combro", "pisang goreng", "pukis", "risole"]
beli = "sepatu"

if beli in gorengan:
    print('mamang bilang "Iya saya jual', beli,'"')

if not  beli in gorengan:
    print('"saya gak jual' ,beli, '"')


karakter = "z"

if  karakter in beli:
    print("ada", karakter, "di",beli)
else:
    print("tidak ada", karakter, "di ", beli)