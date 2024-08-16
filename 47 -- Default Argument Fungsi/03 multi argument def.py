"""
oke yang terakhir, 
ini kita coba buat default argument nya ada banyak
misal 4 deh dikit aja, nah nanti kita bisa edit

langsung aja dah biar ga pusing
"""

# kita buat fungsi, yang argumennya banyak, taro 4 deh
def penjumlahan(angka1 = 5, angka2 = 4, angka3 = 3, angka4 = 2, angka5 = 1):
    hasil = angka1+angka2+angka3+angka4+angka5
    return hasil

# kita tampilin hasil default dulu
i = penjumlahan()
print(i)

# nah kita masih bisa edit salah satu argumen
h = penjumlahan(angka1=10) # harusnya 20
print(h)
