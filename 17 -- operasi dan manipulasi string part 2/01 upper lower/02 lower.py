"""
kali ini kita belajar gimana cara ngubah huruf yang awalnya
mungkin kapital, gede, gede kecil jadi huruf yang semuanya kecil 
"""

kapital = "Agung Wahyu Prayogo"
gede = "AGUNG WAHYU PRAYOGO"
alay = "aGuNg WaHyU pRaYoGo"

print(f"awal : {kapital}, lowercase jadi", kapital.lower())
print(f"awal : {gede}, lowercase jadi", gede.lower())
print(f"awal : {alay}, lowercase jadi", alay.lower())


print(f"""awal : {kapital} lower jadi : {kapital.lower()}
awal : {gede} lower jadi : {gede.lower()}
awal : {alay} lower jadi : {alay.lower()}
""")


"""
jangan lupa buat make () setelah lower
lower()
"""

masnam = input("Masukan nama Anda (nyalakan caps lock)\n : ")
print(f"Nama anda adalah '{masnam.lower()}'\n tak usah panik, semua huruf didalam nama menjadi huruf kecil")