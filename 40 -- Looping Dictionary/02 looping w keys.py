dict_agung = {
    "Nama" : "Agung Wahyu Prayogo",
    "Jenis Kelamin" : "Laki - Laki",
    "Umur" : 24,
    "Sudah menikah?" : False
}

"""
karena kalo make cara biasa ga jelas, kita mau break down 
pertama kita mau looping tapi key nya dulu
"""

for biodata in dict_agung.keys():  # awas .keys(), dalem kurung ga bisa di isi apa2 lo ya
    print(f"key nya ada : {biodata}")

"""
itu baru key
nah di file selanjutnya kita akses looping make value
"""