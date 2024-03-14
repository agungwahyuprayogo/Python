# latihan biasa mengenai string
# kali ini latihan bagaimana menampilkan print ke console biar rapi
# dari yang biasanya kek gimana sampe yang bisa keliatan rata kanan

nmdpn = input("nama depan : ")
nmtgh = input("nama tengah : ")
nmblkg = input("nama belakang : ")
nmlngkp = f"{nmdpn} {nmtgh} {nmblkg}"
angkatan = int(input("angkatan tahun : "))
jrsn = input("jurusan : ")
fklts = input("fakultas : ")
univ = input("universitas : ")

# kalo pake cara lama
print(f"cara lama".center(20,"-"))
print(f"Nama lengkap : {nmlngkp}, angkatan : {angkatan}, jurusan : {jrsn}, fakultas : {fklts}, Univ : {univ} ")
# kalo make cara lama dan ga enak diliat, kesamping, jadi kaya list

# make enter atau \n
print(f"make enter".center(20,"-"))
print(f"Nama lengkap : {nmlngkp}, \nangkatan : {angkatan}, \njurusan : {jrsn}, \nfakultas : {fklts}, \nUniv : {univ} ")

# make triple kutip
print(f"triple kutip".center(20,"-"))
print(f"""Nama lengkap : {nmlngkp}
angkatan : {angkatan}
jurusan : {jrsn}
fakultas : {fklts}
Univ : {univ}
""")
# hasil yang ditampilkan sesuai apa yang ditulis diatas
# jadi kalo mau rapi ya diatur secara manual kek dibawah

# make triple kutip yang dirapihin
print(f"triple kutip tapi dirapihin manual".center(20,"-"))
print(f"""
Nama lengkap    : {nmlngkp}
angkatan        : {angkatan}
jurusan         : {jrsn}
fakultas        : {fklts}
Univ            : {univ}
""")


# ketika dirapihin ya mendingan, tapi ada cara biar keliatan rata kanan,
print(f"make :>25".center(20,"-"))
print(f"""
Nama lengkap anda   : {nmlngkp:>25} 
Tahun Angkatan      : {angkatan:>25}
Jurusan             : {jrsn:>25}
Fakultas            : {fklts:>25}
Universitas         : {univ:>25}
""")
# 25 itu total karakter yg pen diliat di konsol
# dan titik 2 (:) biar rapi ya kudu benerin manual dulu biar sejajar
# baru kalo variable inputan yang bisa dibuat otomatis sama python

print(f"make :<25".center(20,"-"))
print(f"""
Nama lengkap anda   : {nmlngkp:<25}
Tahun Angkatan      : {angkatan:<25}
Jurusan             : {jrsn:<25}
Fakultas            : {fklts:<25}
Universitas         : {univ:<25}
""")

# kalo make <25, ya cuman jadi keliatan rata kiri sih, 
# soal ada 25 karakter ke kanan (abis dari titik 2 ":") ga keitung

# print(f"""
# Nama lengkap anda   : {nmlngkp:=25}
# Tahun Angkatan      : {angkatan:=25}
# Jurusan             : {jrsn:=25}
# Fakultas            : {fklts:=25}
# Universitas         : {univ:=25}
# """)

# ga bisa kalo make =

desa = input("Masukan nama desa : ")
kecamatan = input("Masukan nama kecamatan : ")
kabupaten_kota = input("Masukan nama kabupaten / Kota : ")
provinsi = input("Masukan nama provinsi : ")

print(f"Informasi tempat anda tinggal adalah : ")
print(f"""
Desa        : {desa:>15}
Kecamatan   : {kecamatan:>15}
Kabupaten   : {kabupaten_kota:>15}
Provinsi    : {provinsi:>15}
""")