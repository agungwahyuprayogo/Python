print("===Input Data User====")
print("======Interger========")

"""
beda dari sebelumnya
kalo mau masukin angka, kasih int atau floas sebelum kata input
"""
nama = input("masukan nama anda : ")
tggl = int(input("masukan tanggal lahir : "))
bln = input("bulan : ")
thn = int(input("masukan tahun kelahiran : "))

print(f"{nama} lahir pada {tggl} {bln} {thn}")

# tb = int(input("masukan tinggi badan anda : "))
tb = float(input("masukan tinggi badan anda : "))
bb = float(input("masukan berat badan anda : "))

print(f"{nama} memiliki tinggi badan {tb} cm, dan berat badan {bb} kg")

"""
ketika butuh input data angka, 
dan memungkinkan bisa koma (misal berat badan dan tinggi)
disaranin make float

kalo kita dah bisa ngira ngira angka yang dimasukin bilangan bulat
cukup make interger
"""


berat_truk = float(input("Masukan berat badan truk (ton) : "))
# sengaja masukin float biar kalo angka yang dimasukin koma ga erro ketika di run
berat_bawaan = float(input("Masukan berat bawaan (ton) : "))

total = berat_bawaan + berat_bawaan

print(f"total berat truk dan bawaan adalah {total} ton") 