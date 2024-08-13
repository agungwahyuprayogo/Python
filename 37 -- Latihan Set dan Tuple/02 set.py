"""
oke kita kali ini belajar sets

kalo list make []
tuple make ()
nah sets ini make {}

kekuranganya adalah ga bisa index, ga bisa ubah
tapi kelebihannya bisa ditambah dan di hapus

nah sets ini 
"""

# misal nih kita masukin datanya asal, alias ga urut
ini_sets = {10,2,5,8,6,1} 
# ketika di run, hasilnya urut dari terkecil ke terbesar
print(f"ini sets sebelum di ubah {ini_sets}, {type(ini_sets)}")

# gabisa buat indexing
# print(f"{ini_sets[1]}") # 'set' object is not subscriptable

# bisa di tambah juga, tapi ga make append, makenya add
ini_sets.add(3) 
# misal di data udah ada data 1, kalo add 1 ga bakal nambah
print(f"ini_sets setelah di tambah 3")


# kalo untuk hapus bisa make remove atau discard

ini_sets.remove(3) # .discard juga bisa
print(f"ini sets ketika 3 dihapus kembali {ini_sets}")