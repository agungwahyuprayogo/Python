masang1 = int(input("Masukan angka pertama untuk menjadi biner : "))
masang2 = int(input("Masukan angka kedua untuk menjadi biner : "))

print(f"{masang1} jika dalam biner adalah : {format(masang1,'08b')}")
print(f"{masang2} jika dalam biner adalah : {format(masang2,'08b')}")

print(f"jika dilakukan sebuah operasi logika dalam bentuk biner, maka :")

print(f"{masang1} ---- {format(masang1,"08b")}")
print(f"{masang2} ---- {format(masang2,"08b")}")
print(f"------------------ | ")
print(f"{masang1 | masang2} ---- {format(masang1|masang2,"08b")}\n\n")

print(f"{masang1} ---- {format(masang1,"08b")}")
print(f"{masang2} ---- {format(masang2,"08b")}")
print(f"------------------ & ")
print(f"{masang1 & masang2} ---- {format(masang1&masang2,"08b")}\n\n")

print(f"{masang1} ---- {format(masang1,"08b")}")
print(f"{masang2} ---- {format(masang2,"08b")}")
print(f"------------------ ^ ")
print(f"{masang1 ^ masang2} ---- {format(masang1^masang2,"08b")}\n\n")

print(f"{masang1} ---- {format(masang1,"08b")}")
print(f"------------------ ~ ")
print(f"{~masang1} ---- {format(~masang1,"08b")}\n\n")

pembalik = 0b11111111

print(f"{masang1} ---- {format(masang1,"08b")}")
print(f"------------------ flip ")
print(f"{masang1^pembalik} ---- {format(masang1^pembalik,"08b")}\n\n")

print(f"{masang2} ---- {format(masang2,"08b")}")
print(f"------------------ flip ")
print(f"{masang2^pembalik} ---- {format(masang2^pembalik,"08b")}\n\n")