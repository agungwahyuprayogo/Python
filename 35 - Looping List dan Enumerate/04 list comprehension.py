# list comprahension
# jadi nampilin list dari list lain

list = [1,2,3,4,5,6,7,8,9,10]

# ini bentuk list comprehension
[print(f"sekarang angka ke {i}") for i in list]
# biar ga error, tanda kutip cuman sampe i, 
# abis tu tutup lagi baru ke for loop

# misal kita pengen buat list baru dari list lain dengan di kuadratkan

kuadrat = [i**2 for i in list]
print(kuadrat)