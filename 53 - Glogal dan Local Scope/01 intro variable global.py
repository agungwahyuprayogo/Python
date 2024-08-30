"""
oke kali ini kita bakal belajar soal variable
ternyata baru tau ada variable global sama local

jadi kalo global tuh bisa diakses ke berbagai syntax kaya function,
if, loop
nah kalo variable local tuh cuman ga bisa sembarang asal panggil

kita kasih liat yg global dulu aja kali ya
"""

nama = "Agoenk"

# manggil variable nama di fungsi
def pggl_nm():
    print(f"nama dia tuh {nama}")

pggl_nm() # hasilnya "nama dia tuh agoenk"


# manggil variable di loop
for i in range(0,5):
    print(f"halo {nama}, saya calon istri kamu yang ke - {i}")
# hasilnya ... beda di i doang ganti jadi angka 1-4

# manggil variable di if
if True:
    print(f"if nampilin {nama}")


