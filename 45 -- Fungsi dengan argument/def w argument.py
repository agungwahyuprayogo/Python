"""
nah tadi kan udah belajar def itu apa
cara kerja nya gimana

nah sekarang kita lanjut lagi, 
tapi kali ini kita belajar memasukan inputan ke def atau function
"""

# misal kita buat fungsi yang nyebut nama sesuai yang kita input
def pakabs(nama):   # jadi yang di dalem kurung ini input / argument (tapi kebanyakan argument)
    print(f"hello whatsapp {nama}, gimana orang tua? sehat kan?")
    # nah argument ini semacam variable di dalam fungsi atau def

# misal deh
pakabs("agung")
"""
yang keluar setelah di run adalah "hello whatsapp agung, gimana orang tua? sehat kan?"
nah si "agung" ini masuk ke argument nama (yang dalem kurung dalam def / function) pakabs
nah ketika "agung" ini udah masuk ke argument pakabs
masuk lah "agung" ini ke body of function

function yang kita buat kan hello .. {nama} gimana ...
nah si "agung" ini masuk ke argument nama 
gituu

contoh lain dehh
tapi pake angka kali ini
misal pertambahan
"""

# buat fungsi 
def penjumlahan(angka1, angka2):
    print(f"hasil dari {angka1} + {angka2} = {angka1+angka2}")

penjumlahan(20,30)
"""
20 masuk ke angka1
30 masuk ke angka2
nah dua angka tadi ditambah di dalam fungsi penjumlahan

nah si function ini bisa buat naro angka, string, list, boolean dll
kita buat list deh ya
"""

def penyambutan(orang_orang):
    data_orang = orang_orang.copy()
    for orang in data_orang:
        print(f"selamat datang {orang} di Indonesia")

# kita buat deh contohnya boyband twice
twice = ["sana minatozaki", "tzuyu", "jihyo"]

# trus kita panggil deh fungsinya
penyambutan(twice)