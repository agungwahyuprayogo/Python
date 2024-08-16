import os

"""
ini buat cek aja kalo konstanta di hapus kenapa
"""

# header program
def header():
    os.system("cls")
    print(f"{"HITUNG KELILING DAN":^40}")
    print(f"{"KELILING PERSEGI PANJANG":^40}")
    print("-"*40)

# input angka user
def input_user():
    panjang = int(input("Masukan panjang : "))
    lebar = int(input("Masukan lebar : "))
    return panjang, lebar

# rumus keliling
def keliling(panjang, lebar):
    return 2*(panjang+lebar)

def luas(panjang, lebar):
    return panjang*lebar

def display(massage, value):
    print(f"Hasil perhitungan {massage} = {value}")
    return

while True:

    header()
    PANJANG, LEBAR = input_user() # lebar dan panjang perlu di tampilin lagi, biar ga error
    KELILING = keliling(PANJANG, LEBAR)
    LUAS = luas(PANJANG, LEBAR)

    display("keliling", KELILING)
    display("luas", LUAS)

    lanjut_ga = input("Jalankan kembali program? (y/n)")
    if lanjut_ga.lower() != ("y"):
        break