pertama = int(input("masukan angka pertama : "))
operator = input("silahkan pilih operator ( + - / * % ) : ")
kedua = int(input("masukan angka kedua : "))

if (operator == "+"):
    hasil = int(pertama + kedua)
    print("hasil yang diperoleh adalah",hasil,":)")

elif (operator == "-"):
    hasil = int(pertama - kedua)
    print("hasil yang diperoleh adalah", hasil,":)")

elif (operator == "/") and (kedua != 0):
    hasil = int(pertama // kedua)
    print("hasil yang diperoleh adalah ", hasil, ":)")

elif (operator == "/") and (kedua == 0):
    print("hasil dengan 0 tidak terdefinisi")

elif (operator == "*"):
    hasil = int(pertama * kedua)
    print("hasil yang diperoleh adalah", hasil,":)")

elif (operator == "%"):
    hasil = int(pertama % kedua)
    print("hasil yang diperoleh adalah", hasil,":)")

else:
    print("Maaf operator tidak dikenali")


# angka = int(input("masukan angka : "))

# if angka < 0:
#     print(f"{angka} merupakan bilangan negatif")
# elif angka == 0:
#     print(f"{angka} merupakan nol")
# else:
#     print(f"{angka} merupakan angka positiv")