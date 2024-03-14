# operasi komparasi
# jadi is not ini kebalikan dari is 
# kalo is akan menghasilkan True bila nilai 2 atau lebih nilai variable sama
# sedangkan kalo is not ini hasilnya True kalo 2 nilai dari variable berbeda

# > , < , >= , <= , == , != , is , is not

"""
misal bandingin umur mahasiswa
umur gw = 23
umur awang = 23

disini kita make is not kaya gini

umur gw is umur awang (apakah umur gw TIDAK SAMA dengan umur awang?)
hasilnya yes
"""

print("=== Bandingin umur, masukin bilangan bulat btw")

umur_gw = int(input("Masukin umur lu : "))
umur_org = int(input("Masukin umur temen lu : "))

print(f"berdasarkan umur yang elu dan temen lu masukin, apakah umur kalian berdua berbeda? {umur_gw is not umur_org}")