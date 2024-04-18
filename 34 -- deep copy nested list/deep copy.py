"""
dulu kita belajar kalo mau copy data, kita bisa make -> copy()
nah kalo di list kalo make cara itu, 
anggota di dalem nested list suka masih ikut keubah kalo, anggota di nested list diubah

langsung di kasih liat ke contoh aja kali ya biar ngerti maksudnya gmn
disini kita buat 2 list dulu
"""

data_genap = [2,4]
data_ganjil = [1,3]

# nah kita buat nested list

data_gnp_gnjl = [data_genap, data_ganjil]
print(f"data gabungan dari genap dan ganjil adalah \n{data_gnp_gnjl} \nalamatnya {hex(id(data_gnp_gnjl))} ")

data_copy = data_gnp_gnjl.copy()
print(f"data copy adalah \n{data_copy} \nalamatnya {hex(id(data_copy))} ")


"""
nah dulu kan kalo mau copy data tinggal make .copy() kan
alamatnya emang berubah dari data_gnp_gnjl sama data_copy 
tapi kalo misalkan kita pengen ngubah data genap 2 jadi 6
yang berubah tuh ga cuman di data_gnp_gnjl, tapi data_copy juga

sekarang kita ganti di data genap, 4 jadi 6 m
"""
data_gnp_gnjl[0][1] = 6
print(f"setelah data genap dirubah, hasilnya menjadi : \n{data_gnp_gnjl}\n{data_copy}")

"""
walau address data_gnp_gnjl dan data_copy berbeda, 
tapi data yg ada di dalem list (data_genap dan data ganjil)
kita tes coba
"""
print(f"\naddress data genap di data_gnp_gnjl : {hex(id(data_gnp_gnjl[0]))}")
print(f"\naddress data genap di data_copy : {hex(id(data_copy[0]))}")
# dari sini kita bisa simpulin, walaupun data nested list beda
# tapi data genap masih sama diantara dua nested list tadi

"""
nah cara buat secara keseluruhan di copy biar ga ada kasus datanya berubah lagi
 dengan cara import import deepcopy
"""

from copy import deepcopy

# sekarang kita coba liat semua address

data_deepcopy = deepcopy(data_gnp_gnjl)
print(f"address data_gnp_gnjl adalah {hex(id(data_gnp_gnjl))}")
print(f"address data_copy adalah {hex(id(data_copy))}")
print(f"address data_deepcopy adalah {hex(id(data_deepcopy))}\n")

# masih beda yekan
# sekarang kita liat apakah data nested list 

print(f"address data genap di data_gnp_gnjl adalah \n {hex(id(data_gnp_gnjl[0]))}")
print(f"address data genap di data_copy adalah \n {hex(id(data_copy[0]))}")
print(f"address data genap di data_deepcopy adalah \n {hex(id(data_deepcopy[0]))}")

# nah disini data genap udah berubah, gitu