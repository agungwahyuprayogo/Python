import datetime as dt

print("tebak tanggal".center(20,"-"))

tggl_lhr = dt.date(2000,5,12)

print(f"tanggal lahir saya {tggl_lhr}, waktu itu saya lahir hari {tggl_lhr:%A}")

"""
kalo yang diatas kan cara manual tuh, 
ada cara masukin lewat input nih
dt.date(tahun,bulan,tanggal)
untuk bulan gausah make 0 didepan
misal mo masukin bulan 5, masukin ae langsung 5 gausah 05
bakal error kalo masukin 05
"""

intah = int(input("Masukan tahun : "))
inbul = int(input("Masukan bulan : "))
intangg = int(input("Masukan tanggal : "))

tanggal = dt.date(intah,inbul,intangg)
print(f"tanggal yang anda masukan adalah \n'{tanggal:%c}' atau normalnya {tanggal:%x}, jatuh pada hari {tanggal:%A}, {tanggal:%d} {tanggal:%B} tahun {tanggal:%Y}")

"""
https://www.w3schools.com/python/python_datetime.asp
"""