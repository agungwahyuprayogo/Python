dict_agung = {
    "Nama" : "Agung Wahyu Prayogo",
    "Jenis Kelamin" : "Laki - Laki",
    "Umur" : 24,
    "Sudah menikah?" : False
}

dict_ubj = {
    "Jenis" : "Kampus",
    "Kepemilikan" : "Swasta",
    "Lokasi" : "Bekasi"
}

"""
lanjut lagi, kita belajar akses, bukan akses juga sih
tapi lebih ke, pengen tau value dari key apa gitu
"""

print(f"Nama di dictioinary agung: {dict_agung['Nama']}")

# kalo tipo dikit, error
# print(f"Nama di dictioinary agung: {dict_agung['nama']}")

# nah cara ngatasinya
check = input("Check key di dictionary agung : ")
print(f"apakah ada key {check} di Dictionary Agung? {dict_agung.get(check)}") # make kurung biasa buka kurung siku

# hasilnya none kan, nah bisa kita edit dengan tampilan lain
print(f"apakah ada key {check} di Dictionary Agung? {dict_agung.get(check, "Gada ada banh key yang dimaksud")}") # make kurung biasa buka kurung siku