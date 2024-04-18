"""
nah di list itu bisa nih kita buat list di dalam list
jadi dalam list baru, bisa dimasukin dari list lain yg udah ada
"""

genap = [2,4,6,8]
print(f"list data angka genap adalah {genap}")

# kita buat list data angka ganjil
ganjil = [1,3,5,7]
print(f"data angka ganjil = {ganjil}")

gnp_gnjl_1 = [genap, ganjil]
print(f"gabungan antara genap dan ganjil = {gnp_gnjl_1}")

"""
jadi ada [[list satu], [list dua]]

nah bisa tuh data list gabungan data ganjil dikasih angka lagi 
misal kek gini
"""

gnp_gnjl_2 = [ganjil,genap,0,0,0,0]
print(f"gabungan ganjil genap dan angka tambahan {gnp_gnjl_2}")

