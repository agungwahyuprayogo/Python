"""
kali ini kita bakal belajar mengenai tuple
tuple ini diawali dan diakhiri dengan kurung biasa -> ()
kalo list kan kurung siku []

terus juga tuple ini ga bisa diedit atau ditambahkan
kalo list kan bisa nih

kita coba aja deh langsung
"""

ini_list = [1,2,3,4,5,6,7,8,9,10]
print(f"ini adalah angka2 di list : {ini_list}")

# kita test ubah
ini_list.append(1)
print(f'ketika di tambah angka baru, list menjadi : {ini_list}')

# misal kita ubah data
ini_list[1] = 10
print(f"setelah di ubah lagi jadi : {ini_list}")

# ---------------------------------------------------------------------
# nah kalo tuple tuh bentukanya gini
ini_tuple = (9,8,7,6,5,4) # make kurung
print(f"ini tuple sebelum diubah : {ini_tuple}")

print(f"ini tuple sebelum dirubah {ini_tuple}")

# misal kita pen ubah, gabisa si harusnya
# ini_tuple[1] = 99
# 'tuple' object does not support item assignment

# atau kita tambahkan
# ini_tuple.append(1)
# TypeError: 'tuple' object does not support item assignment

"""
trus fungsinya tuple buat apa? kok ga bisa diubah atau apa?
fungsinya buat nyimpen nilai yg ga bisa diubah ubah, 

ga bisa diubah ubah lewat di tambah atau di kurangin
serta ga bisa di ubah lewat ubahan datanya langsung

intinya penting, tapi buat liat seberapa penting tuple, di latihan nanti

sebenernya bisa diubah, tapi ribet
https://www.w3schools.com/python/python_tuples_update.asp
"""