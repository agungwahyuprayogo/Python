# --0++5--8++11--

# diantara 0 - 5 atau 
# diantara 8 - 11

angka = int(input("masukan angka diantara 0-5 atau 8-11 : "))

print(f"apakah '{angka}' diantara 0-5 ?", angka>=0 and angka <=5)
print(f"apakah '{angka}' diantara 8-11 ?", angka>=8 and angka <=11)

print(f"apakah '{angka}' memenuhi kriteria angka 0-5 atau 8-11 ? {(angka>=0 and angka <=5) or (angka>=8 and angka <=11)} ")

# 1-10 21-30

masang = int(input("Masukin angka diantara 1-10 atau diantara 21-30 : "))
print(f"apakah {masang} diantara 1-10 dan diantara 21-30 {(masang>=1 and masang<=10) or (masang>=21 and masang<=30)}")