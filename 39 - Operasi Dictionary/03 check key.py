"""
sekarang latihan buat check key dalam dictionary
"""

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
cukup mudah buat check ada atau ga nya key dalam dictionary
tinggal -> key in dictionary
"""
print(f"apakah agung punya kelamin? {"Jenis Kelamin" in dict_agung}")
print(f"apakah agung punya Umur? {"Umur" in dict_agung}") # pertanyaan macam apa itu

print(f"apakah ubj punya key Kepemilikan? : {"Kepemilikan" in dict_ubj}")

"""
gitu doang sih sebenernya
"""