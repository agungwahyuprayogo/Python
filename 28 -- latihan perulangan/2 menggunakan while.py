sisi = int(input("Masukan panjang sisi : ")) # masukin dulu angka paling gedenya berape

count = 1 # kudu buat variable count baru lagi, kalo ga dibuat nanti cuman muncul 1 ketika di run
while True: # kenapa while true? biar jalan terus bre, kalo ga dibikin true dan ga ada kondisinya nanti ga jalan. sengaja dibikin while true biar jalan terus
    print(" *"*count)
    count += 1

    if count > sisi: # kenapa make > ? karena kalo make == nanti kurang satu bintang
        break # nah kalo count udah sebanyak sisi, maka akan berhenti

print("awal program while".center(20,"-"))
