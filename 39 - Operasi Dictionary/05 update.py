"""
masih make dictionary yang dipake kemarin
kali ini kita belajar buat update dict
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

print(f"ini dict agung : \n{dict_agung}\n\ndan ini adalah dict ubj : \n{dict_ubj}")

"""
dan cara buat updatenya adalah dengan 
dictionary_nama[key_name] = new_value
"""

dict_agung["Jenis Kelamin"] = "cowo"
print(f"\nsetelah kelamin diubah : {dict_agung}")

"""
yang jadi permasalahan adalah kalo nama key salah
dan kita tau kalo python itu case sensitive
"""
dict_agung["jenis kelamin"] = "cw"
# bjir cok masih bisa

"""
yowes lah ya
ada cara lain buat update,
tapi ini update nya kalo misal belum ada, otomatis nambah
misal lu nambahin key pacar : ariana grande, sebelumnya kan belum ada
nah kalo belum ada nanti otomatis nambah
"""
                # hati hati, make kurung kurawal
dict_agung.update({"Girlfriend":"Ariana Grande"})
print(f"\nsetelah update pacar : {dict_agung}")
# see, sebelumnya ga ada jadi nambah
