"""
kali ini kita belajar gimana cara ngubah huruf yang awalnya
mungkin kapital, kecil, gede kecil jadi huruf yang semuanya gede 
"""

kapital = "Agung Wahyu Prayogo"
kecil = "agung wahyu prayogo"
gede_kecil = "aGuNg WaHyU pRaYoGo"

print(f"awal : \t\t {kapital}, \nuppercase jadi\t", kapital.upper())
print(f"\nawal : \t\t {kecil}, \nuppercase jadi\t", kecil.upper())
print(f"\nawal : {gede_kecil}, \nuppercase jadi", gede_kecil.upper())


print(f"""\nawal : {kapital} upper jadi : 
      {kapital.upper()}

awal : {kecil} upper jadi : 
        {kecil.upper()}

awal : {gede_kecil} upper jadi : 
        {gede_kecil.upper()}
""")


"""
jangan lupa buat make () setelah uppper
variable.upper()
"""

masang = input("Masukan nama Anda\n : ")
print(f"Nama anda adalah {masang.upper()}")