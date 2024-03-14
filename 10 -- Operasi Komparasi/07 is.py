# operasi komparasi
# jadi is ini membandingkan 2 nilai dari suatu variable dengan output boolean

# > , < , >= , <= , == , != , is , is not

"""
misal bandingin umur mahasiswa
umur gw = 23
umur awang = 23

disini kita make is kaya gini

umur gw is umur awang (apakah umur gw sama dengan umur awang?)
hasilnya yes

jadi bisa sama fungsi nya kaya == secara boolean
"""

print("==Bandingin umur coy, (masukin bilangan bulat)==")

umur_gw = int(input("Masukan umur elu gung : "))
umur_org = int(input("Masukin umur temen lu : "))

print(f"berdasarkan umur yang elu dan temen lu masukin, apakah umur kalian sama? {umur_gw is umur_org}")