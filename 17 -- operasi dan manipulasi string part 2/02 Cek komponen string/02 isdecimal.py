## isaldecimal() adalah syntax untuk mengecek 
# value dari variable semuanya ANGKA atau bilangan bulat doang
# kalo value angka hasilnya TRUE
# kalo huruf hasilnya False

cek1 = "123"

print(f"apakah {cek1} angka semua? {cek1.isdecimal()}")


# inget -> .decimal() ada buka kurung tutup kurung
# decimal berkaitan dengan angka
# biar gampang ingetnya 

cek2 = "agung"
print(f"apakah {cek2} angka semua? {cek2.isdecimal()}")

cek3 = "agung123"
print(f"apakah {cek3} angka ? {cek3.isdecimal()}")

cek4 = "123.5"
print(f"apakah {cek4} angka ? {cek4.isdecimal()}")
# bjir yang 123.5 salah, cuman gegara ada titik doang
# jadi emang harus murni angka doang di decimal ini