# bisa diubah ke biner, oktal, hexadesimal
# default desimal

while True:

    angka = 255
    # biner
    print(f"{angka} kalo jadi biner = \n{bin(angka)}")

    # oktal
    print(f"{angka} kalo jadi oktal = \n{oct(angka)}")

    # hexadecimal
    print(f"{angka} kalo jadi hexadesimal = \n{hex(angka)}")

    tengah = "Konversi angka".center(20,"-")
    masang = int(input("Masukan bilangan yang ingin dikonversi : "))

    print(f"\n{tengah}\n'{masang}' bila diubah menjadi biner hasilnya : {bin(masang)}\ndalam oktal hasilnya : {oct(masang)}\ndalam hexadesimal hasilnya : {hex(masang)}")

    ulang = input("apakah anda ingin mengulang program ini? : (y/n)")

    if ulang != 'y':
        break