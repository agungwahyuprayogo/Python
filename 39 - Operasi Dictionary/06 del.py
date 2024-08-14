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

print(f"dictionary sebelum hapus key: {dict_ubj}")

del dict_ubj["Kepemilikan"]
print(f"\ndictionary sesudah hapus key kepemilikan: {dict_ubj}")