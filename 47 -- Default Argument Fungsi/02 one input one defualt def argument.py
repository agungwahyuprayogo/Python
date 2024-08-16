"""
kalo tadi belajar buat satu default argument
nah ini kita coba buat satu inputan argument yg wajib di isi
yang satu ga di isi gpp
"""
# misal kita buat def lagi, kita edit dikit
# nah dalam kasus ini, kita wajib masukin nama, kalo ga error
# kalo pesan ga di isi gpp
def salam(nama, pesan = "Selamat datang di UBJ yaa, semoga kamu betah disini dan nemu bakal dan potensi kamuu"):
    print(f"haloo {nama}, {pesan}")

salam("agungg") 
# ga perlu isi 2 inputan argument, cukup nama aja dan ga error

# bisa ga kalo pesannya kita ganti? coba ya
salam("agoenk", "okee") # bisa ternyata

""" 
bisa juga kok ga harus urut pas input
misal diatas kan nama dulu baru pesan
kita bisa masukin pesan dulu baru nama
tapi variable argument perlu kita masukin juga biar ga error
"""

# tapi kudu masukin variable dulu kek pesan =, nama = 
salam(pesan="Kamu guantenk dehh", nama="Agungg kunn")
# ketika di run tetep ngikutin rumus deh, nama dulu baru pesannya apa

# trus kalo nama atau pesanya ga dihapus gmn?
# jawabanya bakal error
# salam(pesan="Kamu guantenk abiezz", "Agungg kunn") # di agungkun bakal ada garis merah


# kita coba lagi tapi make angka
def pangkat(angka, pangkat = 2):
    hasil = angka**pangkat
    return hasil

a = pangkat(5) # kalo kita masukin satu gini, 5^2 = 25
print(a)

b = pangkat(5,3)
print(b)