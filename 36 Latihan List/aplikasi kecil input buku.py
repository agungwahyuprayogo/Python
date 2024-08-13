"""
jadi kali ini kita bakal buat aplikasi kecil 

disini kita input buku sama penulisnya
"""
print("Masukan Info Buku ")

daftar_buku = []

while True:
    judul = input("Judul Buku : ")
    penulis = input("Penulis : ")

    buku_baru = [judul, penulis]
    daftar_buku.append(buku_baru)

    for index, buku in enumerate(daftar_buku):
        print(f"{index}, {buku[0]}, {buku[1]}")

    lanjut = input("ingin melanjutkan program? (y/n)")

    if lanjut == "n":
        break

print("Program berakhir")