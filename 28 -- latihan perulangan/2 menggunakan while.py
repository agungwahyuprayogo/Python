sisi = int(input("Masukan panjang sisi : ")) # masukin dulu angka paling gedenya berape

count = 1 # kudu buat variable count baru lagi, kalo ga dibuat nanti cuman muncul 1 ketika di run
while True:
    print(" *"*count)
    count += 1

    if count > sisi: # kenapa make > ? karena kalo make == nanti kurang satu bintang
        break

print("awal program while".center(20,"-"))