"""
ada kemungkinan kalo mau biner yang dimasukin tuh flip
yang awalnya dari 0 jadi 1, trus dari 1 jadi 0
bisa kita akalin dengan buat satu variable baru lagi yang full 11111111
dan make xor
karena kalo make xor dimana kalo 0 ketemu 1 jadi
dan kalo 1 ketemu 1 jadi 0
"""

pembalik = 0b11111111

angka = int(input("Masukan angka biner yang ingin anda balik : "))
print(f"angka yang anda masukan adalah : {angka}, dalam bentuk biner menjadi {format(angka,"08b")}")

print(f"sedangkan biner {format(angka,"08b")} jika dibalik akan menjadi : {format(pembalik^angka,"08b")}")