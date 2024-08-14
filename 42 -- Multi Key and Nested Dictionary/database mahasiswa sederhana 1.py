"""
jadi kali ini kita latihan buat database mahasiswa make python
jadi pertama kita buat 3 dictionary mahasiswa dulu
abis itu, tiap dictionary kita masukin ke satu dictionary 
"""
import datetime as dt 

mahasiswa1 = {
    "Nama" : "Agung Wahyu Prayogo",
    "NIM" : "201910225300",
    "SKS" : 89,
    "Lahir" : dt.datetime(2000,5,12) #tahun, bulan, tanggal
}

mahasiswa2 = {
    "Nama" : "Martaulina Simanungkalit",
    "NIM" : "201910225298",
    "SKS" : 90,
    "Lahir" : dt.datetime(2001,7,15) #tahun, bulan, tanggal
}

mahasiswa3 = {
    "Nama" : "Eko Saputro",
    "NIM" : "201910225399",
    "SKS" : 89,
    "Lahir" : dt.datetime(1999,1,1) #tahun, bulan, tanggal
}

print(f"\nini mahasiswa 1\n{mahasiswa1}")
print(f"\nini mahasiswa 2\n{mahasiswa2}")
print(f"\nini mahasiswa 3\n{mahasiswa3}")

"""
terus kita buat satu dictionary biar bisa nampung 3 mahasiswa tadi
"""

data_mahasiswa = {
    "MHS001":mahasiswa1,
    "MHS002":mahasiswa2,
    "MHS003":mahasiswa3,
}

print(f"\n\nini data mahasiswa : \n{data_mahasiswa} ")
# masih berantakan kan, nah di file berikutnya kita bakal rapihin
# silahkan lanjut ke file berikutnya