"""
jadi kali ini kita bakkal bahas mengenai data
bukan data kaya yang di kk atau ktp
tapi data lebih ke nyimpen data ke variable, kek a nyimpen angka 5

buat nyoba interaktif atau kek run di cmd cuman versi vscode, bisa run dulu file ini

pertama arahin kursor ke paling kanan
abis itu ketik python (buat windows) kalo mac/linux python3
abis itu enter
masukin angka 10, enter
lalu coba 5 + 10 lalu enter hasilnya 15
lalu coba masukin a = 10, enter
lalu a + 5 lalu enter, maka hasilnya 15

kalo pen keluar tinggal ketik ctrl+Z, lalu enter
bisa juga ketika exit() lalu enter
"""

# ---------------------- VARIABLE ----------------------
# ----------- TEMPAT UNTUK MENYIMPAN NILAI -------------

agung = 5
"""
hal diatas sama ae kek, 5 dimasukin ke variable agung, atau bisa juga kek gini
nilai yang ada / value dari variable agung adalah 5
begitu dan seterusnya buat variable lain

variable ga harus panjang, bisa make 1 huruf 
angka ga bisa paling depan (misal 1agung, palingan agung1 baru boleh)
ada spasi juga ga boleh (agung why, bakal merah nanti, kalo mau agung_wh)
make tanda "-" juga ga boleh (agung-1, make underscore kalo mau)

diluar hal yang dilarang diatas, boleh dijadiin variable
"""
 
a = 10
# sama ae kek a mengandung value 10, nilai 10 dimasukin ke varible a, gitu
B = 20

print("nilai agung adalah", agung)
print("nilai a adalah", a)
print("nilai B adalah", B)

"""
cara biar gampang copy code diatas
pertama blok dulu yang pen di copy
abis itu klik alt+shif
kalo udah arahin kebawah (keyboard panah bawah)
"""

# ---------------- PEMANGGILAN KEDUA -------------------

"""
jadi kalo misalkan ada nama variable yang sama dalam satu file, 
value atau nilai yang ditampilkan yang akan ditampilkan sesuai kapan nilai itu dipanggil \
misal diatas kan nilai a nya 10, dan nilai a dibawah 20
maka, kalo file ini di run ya ngikutin kodingan yang dibawah hasilnya 20
diatas nilai a 10 dan nilai a yang dibawah 20

kalo di jupyter notebook atau google collab, nilai yang akan ditampilkan adalah yg terakhir

oiya, misal ada kek gini

a = 10 
a = 20
lalu print(a)

maka yang muncul adalah a yang terakhir (juga berlaku di file .py)
"""
a = 20
print("\nnilai a yang baru", a)

# ---------------- ASSIGNMENT INDIRECT -------------------
"""
sedikit berbeda dengan pengisian nilai dari suatu variable diatas
cara assignment ini make cara yang berbeda dan ga masukin angka, 
tapi gunain variable yang ada sebelumnya buat dijadiin patokan nilai variable yang baru
"""
b = a
print("tampilkan nilai b", b)
"""
maka ketika di run, nilai yang ada di variable b = 20
kalo masih bingung,.. 
gini nih, kan a yang terakhir nilai dari variable a = 20
nah karena b = a, sama aja kek "tolong dong samain nilai b kaya si a"
karena a 20, maka si b nurut nilainya juga 20
"""
