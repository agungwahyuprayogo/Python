import os

"""
jadi kali ini kita bakal buat program sederhana buat ngitung luas dan keliling persegi
sebenernya bisa make cara biasa, make input, trus rumus
cuman kan biasanya kita make while loop kan
sebenernya while loop kalo programnya terlalu panjang 
nah nanti kita buat while loop make def aja
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
    LEBAR, PANJANG = input_user() # awalnya juga bingung, kok PANJANG DAN LEBAR di ketik, ternyata tujuannya buat nyimpen nilai sementara dari fungsi def. kalo ga ditulis dulu gitu nanti error, coba aja
    KELILING = keliling(LEBAR, PANJANG) # lalu ini dimasukin lagi (lebar, panjang), kalo ga dikasih gituan nanti muncul error missing 2 required positioan arguments 'panjang' and 'lebar'
    LUAS = luas(PANJANG, LEBAR) # sama kaya keliling

    display("keliling", KELILING)
    display("luas", LUAS)

    lanjut_ga = input("Jalankan kembali program? (y/n)")
    if lanjut_ga.lower() != ("y"):
        break