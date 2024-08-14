"""
better kita buat dictionary baru deh ya, yg lama buat latihan aja
sekarang latihan buat tau berapa panjang suatu dictionary
"""

dict_agung = {
    "Nama" : "Agung Wahyu Prayogo",
    "Jenis Kelamin" : "Laki - Laki",
    "Umur" : 24,
    "Sudah menikah?" : False
}

# kita print dulu dict diatas
print(f"ini contoh dict agung : {dict_agung}")

# teruus kita pengen tau panjangnya berapa
print(f"panjang dict diatas adalah : {len(dict_agung)}")
# jawabanya 4, karena ada nama, kelamin, umur dan sudah menikah

# kita buat baru lagi buat buktiin
dict_ubj = {
    "Jenis" : "Kampus",
    "Kepemilikan" : "Swasta",
    "Lokasi" : "Bekasi"
}

print(f"ini contoh dict ubj : {dict_ubj}")
print(f"panjang dict ubj adalah : {len(dict_ubj)}")