"""
oke kali ini kita akan buat list make cara yang lebih singkat tapi hasilnya tuh wew
kalo sebelumnya kan kudu ngetik manual
kali ini kita bakal make for dan if dalam membuat list
"""

# List Comprehensife 
list_make_for = [i for i in range(0,10,2)]
print(f"ini adalah list menggunakan for : {list_make_for}")

"""
[i for i in range(0,10)]
oke cara bacanya

didalam list saya ingin memasukan i (i awal) 
dimana i (for i) 
memiliki range dimulai dari 0 hingga sebelum 10
dengan langkah 2 step

maka ketika di run yang tampil adalah 0,2,4,6,8

kalo di kuadratin (^2) bisa ga banh?
nah inilah gunanya list menggunakan for
"""

list_kuadrat = [i**2 for i in range(0,10,2)]
print(f"ini adalah list yang di kuadrat kan : {list_kuadrat}")

"""
syntax yang mengindikasikan kuadrat adalah **2, 
angka ga harus dua, bisa di ganti 3 (kubik) dan seterusnya
karena kita make kuadrat maka hasilnya langsung dikuadratin :
[0, 4, 16, 36, 64]
"""

# list make for dan if

"""
oke ke yang lebih advance lagi nih, 
mirip2 diatas tapi ada if nya
misal kita pengen ngilangin angka tertentu dalam list
"""
list_5_ilang = [i for i in range(0,20) if i != 5]
print(f"didalam list ini : {list_5_ilang}")

"""
kirain angka yang mengandung 5 bakal ilang, taunya 15 masih ada di list
keh lanjut, sekarang pen buat list angka genap misalkan
"""

list_genap = [i for i in range(0,10) if i %2 == 0]
print(f"ini adalah list angka genap : {list_genap}")

list_ganjil = [i for i in range(0,10) if i %2 != 0]
print(f"ini adalah list angka ganjil : {list_ganjil}")