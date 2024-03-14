## isspace() adalah syntax untuk mengecek 
# apakah value dari variable semuanya spasi, tab, new line \n

cek1 = "\"  \"" # spasi

print(f"apakah {cek1} spasi atau tab atau \\n? {cek1.isspace()}")


# inget -> .isspace() ada buka kurung tutup kurung
# space kan kosong ya, di langit jarak antar planet jauh dan kosong
# anggep aja space itu kosong

# cek2 = 123
# print(f"apakah {cek2} huruf semua? {cek2.isalpha()}")
# ternyata harus string

cek2 = "\"  \"" # tab
print(f"apakah {cek2} spasi atau tab atau \\n? {cek2.isspace()}")

cek3 = "\" \n \"" # new lline
print(f"apakah {cek3} spasi atau tab atau \\n? {cek3.isspace()}")

cek4 = "agung"
cek5 = "123"

print(f"apakah \"{cek4}\" spasi atau tab atau \\n? {cek4.isspace()}")

