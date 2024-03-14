# +++0---5+++8---11+++

angka = int(input("masukan angka kurang dari 0 / 5-8 / 11 keatas : "))

print(f"apakah '{angka}' < 0 ?", angka<0)
print(f"apakah '{angka}' 5-8 ?", angka>=5 and angka <=8)
print(f"apakah '{angka}' > 11 ?", angka>11)

print(f"apakah '{angka}' memenuhi aturan ? ", (angka<0)or(angka>=5 and angka <=8)or(angka>11))

# 1-10 atau 21-30 atau 41-50

masang = int(input("Masukan angka diantara 1-10 / 21-30 / 41-50 : "))

print(f"apakah {masang} sudah memenuhi kriteria? {(masang>=1 and masang<=10) or ((masang>=21 and masang<=30)) or (masang>=41 and masang<=50)}")