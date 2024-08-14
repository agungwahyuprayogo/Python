dict_agung = {
    "Nama" : "Agung Wahyu Prayogo",
    "Jenis Kelamin" : "Laki - Laki",
    "Umur" : 24,
    "Sudah menikah?" : False
}

"""
kalo tadi .keys() buat nampilin key
begitu pula yang .values() buat nampilin values dari dictionary
nah kali ini bisa 22nya
kita make .items(), jadi bisa liatin key dan value 
"""

for key, value in dict_agung.items():
    print(f"{key} saya {value}")

"""
keh dah berhasil ternyata
hasilnya Nama saya Agung Wahyu Prayogo
dst ..
tapi 
Sudah Menikah saya False, wtf
"""