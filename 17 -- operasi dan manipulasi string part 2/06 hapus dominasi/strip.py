"""
ketika di kelas strip buat apus karakter
disini buat hapus .. bingung bahasanya
"""
while True: 
    misal = 10*"-" + "tengah" + 10*"-"
    print(misal)

    contoh = misal
    print(contoh)
    contoh.strip("-")
    print(f"ketika contoh\n {contoh} \ndi strip dengan '-' jadi \n{contoh.strip('-')}")

    input_kata = input("masukan sebuah kalimat : ")
    hapus_karakter = input("Masukan karakter yang ingin anda hapus : ")

    print(f"{input_kata.strip(hapus_karakter)}")

    ulang = input("\n\nIngin mengulang program? : (y/n)")
    if ulang != 'y':
        break

"""
oke jadi sebenernya dari syntax strip ini ada error ntah dari pythonya apa dari mana
jadi kalo misalkan kalimat yg lu masukin dikit, dia berkerja
tapi kali kalimat yg lu masukin kalimat nya panjang, dia kek ga berkerja
coba aja make "ooookooooo" dengan hapus karakter "o"
sama make "oke kali ini gw belajar lgi setelah sekian lama ga belajar" dengan hapus karakter "a"

nah pas make kalimat yang kedua ini, ga jalan coy, ga ada "a" yang kehapus
justru kehapus kalo kalimantnya dikit
"""