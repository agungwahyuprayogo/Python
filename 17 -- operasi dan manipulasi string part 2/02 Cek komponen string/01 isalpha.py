## isalpha adalah syntax untuk mengecek value dari variable semuanya huruf

cekandricek = "agung"

print(f"apakah {cekandricek} huruf semua? {cekandricek.isalpha()}")


# inget -> .isalpha() ada buka kurung tutup kurung
# alpha = alpabet
# biar gampang ingetnya

# cek2 = 123
# print(f"apakah {cek2} huruf semua? {cek2.isalpha()}")
# ternyata harus string

cek2 = "123"
print(f"apakah {cek2} huruf semua? {cek2.isalpha()}")


# ngecek doang apakah yang didalem kurung bisa dimasukin sesuatu?

# cekandricek2 = "agung"

# print(f"apakah {cekandricek2} huruf semua? {cekandricek2.isalpha("agung")}")

# kata "agung" malah buat tulisan didalem kurung ada garis merah di bawahnya

masnam = input("Masukan nama anda (masukan dalam huruf) \n: ")
print(f"Nama anda adalah '{masnam}' \napakah benar yang dimasukan huruf? {masnam.isalpha()}")

# ternyata ketika masukin nama depan dan nama belakang yang dimana memasukan spasi
# ketika di cek isalpha hasilnya False, yang bikin false adalah spasinya
# tapi kalo masukinnya nama depan doang misal "agung" doang tanpa spasi dan nama belakang
# hasilnya True