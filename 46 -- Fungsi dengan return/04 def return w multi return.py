def matematika(angka1, angka2):
    tambah = angka1 + angka2
    kurang = angka1 - angka2
    kali = angka1 * angka2
    bagi = angka1 / angka2

    return tambah, kurang, kali, bagi

k, l, m, n = matematika(10,5)
print(f"hasil tambah {k}")
print(f"hasil kurang {l}")
print(f"hasil kali {m}")
print(f"hasil bagi {n}")

# coba kalo cuman satu atau dua huruf doang

o = matematika(15,5)
print(o)
# tetep berkeja, 
# hanya saya ga jelas dapet angka (20, 10, 75, 3.0) dari mana