## isalnum adalah syntax untuk mengecek 
# value dari variable semuanya ANGKA dan HURUF
# jadi mau valuenya angka doang, True
# huruf doang juga True

cekandricek = "123"

print(f"apakah {cekandricek} angka dan huruf ? {cekandricek.isalnum()}")


# inget -> .isanum() ada buka kurung tutup kurung
# num.. num gapaham dah

# cek2 = 123
# print(f"apakah {cek2} huruf semua? {cek2.isalpha()}")
# ternyata harus string

cek2 = "agung"
print(f"apakah {cek2} angka dan huruf ? {cek2.isalnum()}")

cek3 = "agung123"
print(f"apakah {cek3} angka atau huruf? {cek3.isalnum()}")

# masang = int(input("Masukan tinggi anda dalam satuan cm : "))
# print(f"tinggi anda adalah {masang} cm. \napakah {masang} angka? {masang.isalnum()}")

# ketika nyoba make atribut int(input) error, 
# isalnum ga bisa cek variable yang berupa angka
# bisa sebenernya di casting, tapi disini cuman mau ngecek berfungsi atau ga nya isalnum

mastang = input("Masukan tanggal lahir anda (tggl/bln/thn) : ")
print(f"tanggal lahir anda adalah adalah {mastang} cm. \napakah {mastang} ada huruf dan angka {mastang.isalnum()}")

"""
bjir cok error lagi gegara ada spasi doang, baru ga error kalo ga dimasukin spasi
dan tadi ngecek lagi make 12/05/2000 tetep salah
pas masukin angka doang kek 12 atau 05 (bulan) doang hasilnya true cok 
"""