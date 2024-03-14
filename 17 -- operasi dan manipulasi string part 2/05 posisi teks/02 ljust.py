"""
sama kek di word, ada rata kiri, rata kanan, rata tengah
 rjust ljust sama center gitu juga
"""

rt_kr = "kiri".ljust(20) # jumlah karakter
print(f"'{rt_kr}'") 
# baca komentar di center!

rt_kr1 = "kiri".ljust(10) # jumlah karakter
print(f"'{rt_kr1}'") 

# biar keliatan keren, bisa di tambah parameter

rt_kr3 = "kiri".ljust(20,"-") # jumlah karakter
print(f"'{rt_kr3}'") 
# mirip di center, kita merintah masukin 20 karakter
# kita pen masukin kiri ada di posisi paling kiri
# dan sisanya adalah - ke kanan
# bisa dihitung kalo kiri ada 4 huruf
# dan strip otomatis ada 16 (20 - 4 = 16) dari

rt_kr4 = "kiri".ljust(20,">") # jumlah karakter, ">" karakter selain spasi
print(f"'{rt_kr4}'") 

maskir = input("Masukan kata buat rata kiri : ")
print(f"{maskir.ljust(20,"<")}")