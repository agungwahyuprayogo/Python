"""
ambil huruf dari berapa sampai berapa
make [:]

ngeselinya dari berapa sampai sebelum
gini deh
"""

nama = "agung wahyu prayogo"

print(f"index dari 0-4 dari {nama} adalah\n", nama[0:4])

"""
logikanya di index part 1, 4 itu sampe g
tapi ini 4 ga sampe g
"""
print(f"index dari 0-5 dari {nama} adalah\n", nama[0:5])


masnam = input("Masukan nama Anda : ")
maswaldex = int(input("Masukan index awal : "))
maskhirdex = int(input("Masukan inder dibelakang : "))

print(f"nama anda adalah '{masnam}', dimana index awal adalah '{maswaldex}' dan index akhir adalah '{maskhirdex}', yang berarti menjadi '{masnam[maswaldex:maskhirdex]}'")