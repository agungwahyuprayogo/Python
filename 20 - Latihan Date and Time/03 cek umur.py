# cek umur (tahun dan bulan)

import datetime as dt

print(f"Cek Umur".center(20,"-"))

print("masukan tanggal lahir anda dalam angka")
tggl = int(input("Tanggal  \t: "))
bln = int(input("Bulan  \t\t: "))
thn = int(input("Tahun  \t\t: "))
# semua di masukan dalam bentuk int
# karena datetime tidak mendukung string

tggl_lhr = dt.date(thn,bln,tggl) 
# sesuai aturan date python, tahun dahulu, bulan lalu tanggal
print(f"tanggal lahir anda adalah tanggal {tggl_lhr:%c}") 
# :%A untuk menampilkan hari pada saat itu
hari_ini = dt.date.today()
print(f"sekarang tanggal {hari_ini:%c}")

total_hari = hari_ini - tggl_lhr
print(f"\ntotal hari dari tanggal {tggl_lhr} ke {hari_ini} adalah {total_hari}")

# karena satu tahun 365 hari, brarti
# umur = total_hari // 365 -> kalo ga diubah jadi .days hasilnya jadi 23 mulu 
# 23 dari mana? tahun saat ini (2023) dikurang tahun kelahiran (2000)
umur = total_hari.days // 365 
# .days biar hasilnya ga ada days di belakang
# make // biar hasilnya bulet

# untuk menghitung bulanya bisa % 365 lalu // 30, karena 1 bulan 30 hari
umur_bln = (total_hari.days % 365) // 30
# kalo masih bingung, jadi .days kan ketauan nih total harinya berapa
# dimodulus 365 (total hari dalam setahun)
# kenapa make modulus (%)? biar yang diambil sisa dari pembagian 
# misal 8614 % 365 = 219 (perhitungan normal dapet 23 sisa 219) 
# ^ saat ini 12 desember 2023
# karena 1 bulan terdiri dari 30 hari, 219 tadi dibagi 30
# lalu dibagi 30 (total hari dalam 1 bulan)
# 219 // 30 dapet 7.3 
# karena floor devition ga nampilin koma, makanya yg tampil hanya 7


umur_hari = (total_hari.days % 365) % 30
# nah buat nyari hari
# kita tadi dah dapet 8614 % 365 = 219 (23 sisa 219)
# nah karena satu bulan terdiri dari 30 hari, 
# kita modulus lagi buat dapetin hasil sisanya 
# 219 % 30 = 9 (perhitungan normal 219 : 30 = 7 sisa 9)
# jadi deh 9 hari dari situ
 
print(f"jadi umur anda saat ini adalah {umur} tahun {umur_bln} bulan {umur_hari} hari")