print(20*"-")
print("Kalkulator Sederhana")
print(20*"-")

while True:
    print("Pilih Menu : ".center(20))
    print("ketik 1 untuk menu penjumlahan")
    print("ketik 2 untuk menu pengurangan")
    print("ketik 3 untuk menu perkalian")
    print("ketik 4 untuk menu pembagian")
    operator = int(input("nomor : "))

    angka1 = float(input("Masukan angka pertama : "))
    angka2 = float(input("Masukan angka kedua : "))

    if operator == 1:
        print(f"hasil dari {angka1} + {angka2} = {angka1 + angka2}")
    elif operator == 2:
        print(f"hasil dari {angka1} - {angka2} = {angka1 - angka2}")
    elif operator == 3:
        print(f"hasil dari {angka1} x {angka2} = {angka1 * angka2}")
    elif operator == 4:
        print(f"hasil dari {angka1} / {angka2} = {angka1 / angka2}")
    else:
        print("pilih yang bener cok")
    print("operasi berakhir")

    ulang = input("apakah anda ingin mengulang program ini? : (y/n)")

    if ulang != 'y':
        break