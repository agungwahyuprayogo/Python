"""
oke sekarang targetnya buat segitiga yang makin ke bawah makin banyak
kek gini
      +
    + + +
  + + + + + 
+ + + + + + +

sebelumnya kan bentuk segitiga tapi mepet ke kiri
nah bagaimana caranya kalo buat segitiga yang jumlah nya kecil di tengah
"""

# Input dari pengguna untuk panjang sisi segitiga (harus ganjil)
sisi = int(input("Masukan angka ganjil untuk membuat segitiga : "))

# Inisialisasi variabel count sebagai pembantu iterasi
count = 1
# lalu buat ngasih jarak spasi dari paling kiri, kita akalin dari sisi dibagi 2
# misal kita masukin sisi 10, nah biar tanda + paling atas ke tengah, 10 dibagi 2 jadi 5
# jadi ada 5 spasi sebelum print + yang pertama
# biar ga jadi koma kalo sisi yang dimasukin ganjil, kita buletin kebawah make int
spasi = int(sisi/2)

# Loop tak terbatas (akan dihentikan oleh break statement)
while True:
    # 
    if count % 2: # Jika count habis dibagi 2 (count ganjil
        print(" " * spasi,"+" * count)  
        # pointnya disini ^ , spasi dikali hasil dari spasi baru di print tanda +
        # stelah spasi make koma biar langsung + dikali jumlah count
        spasi -= 1 
        # karena count awal awal pasti banyak, perlu di kurangin satu tiap turun
        # dan spasi -= hanya perlu dimasukin kalo hasilnya ganjil
        count += 1  # 
    else:
        count += 1  # di skip
        continue

    # 
    if count > sisi:
        break

# Cetak pesan 'berakhir' setelah loop selesai
print("berakhir")

"""
Kode ini memodifikasi pola segitiga dengan menambahkan spasi di awal setiap baris. 
Setiap iterasi mencetak sejumlah spasi diikuti dengan sejumlah karakter "+" sesuai 
dengan nilai variabel count. Proses ini dilakukan hingga panjang sisi tercapai. 
Pesan "berakhir" dicetak setelah loop selesai.
"""