"""
anpnymous function
currying <- Haskell Curry

jadi kalo make def kan biasanya ditentuin nih angka berapa, n berapa
misal kek dibawah ini deh
"""

def pangkat(angka,n):
    hasil = angka**n
    return hasil

print(pangkat(2,2))

"""
kalo make def, kita kudu masukin angka dan n 
nah kita bisa buat ga kudu masukin angka dan n
"""

def pgkt(n): 
    return lambda angka:angka**n

pangkat2 = pgkt(2)
print(f"pangkat 2 dari 3 adalah = {pangkat2(3)}") # sama aja deng, ga bikin jadi terlalu singkat juga ternyata
print(f"pangkat 2 dari 5 adalah = {pangkat2(5)}") 

pangkat3 = pgkt(3)
print(f"pangkat 3 dari 3 adalah = {pangkat3(3)}") 
print(f"pangkat 3 dari 5 adalah = {pangkat3(5)}") 
