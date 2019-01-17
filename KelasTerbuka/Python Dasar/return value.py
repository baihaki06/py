#funsi dengan return value
def Kuadrat(argumen):
    total = argumen**2
    print("nilai kuadrat dari ", argumen, "adalah", total)
    return  total

a = Kuadrat(4)
print(a)

print("+"*100)

#fungsi dengan return value dan multi argumen
def Tambah(argumen1, argumen2):
    total = argumen1 + argumen2
    print(argumen2, "+", argumen2, "=", total)
    return  total

def Kali(argumen1, argumen2):
    Total = argumen1 * argumen2
    print(argumen1 , "x", argumen2, "=", Total)
    return  Total

a  = Kali(3, Tambah(3,4))

print(a)