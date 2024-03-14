"""
bagaimana cara nampilin angka plus dan minus dalam angka
bisa make format +d (int) +.3f (float, dan ga harus 3)
"""

int1 = 100
int2 = -100
des1 = 109.199
des2 = -109.120

print(f"angka di int1 adalah {int1} ")
# hasilnya ga bakal berubah tetep 100
print(f"angka di int1 kalo dikasih :+d {int1:+d}") 
# kalo dikasih +d jadi +100
print(f"angka di int2 kalo ga make :+d {int2} ")
# ternyata kalo ga make +d angka minusnya masih keliatan
print(f"angka di int2 kalo dikasih :+d {int2:+d} ")
# ga wajib ternyata buat nampilin angka negatif make +d


print(f"\nangka des1 kalo ga make embel apa2 : {des1}")
print(f"angka des1 kalo dikasih :f : {des1:f}") 
# kalo make float, angka 0 di belakang jadi banyak
print(f"angka des1 kalo dikasih .2f : {des1:.2f}") 
# karena cuman nampilin 2 angka setelah koma, jadi 109.20 (wow dibulatkan keatas ternyata)
print(f"angka des1 kalo dikasih +.2f : {des1:+.2f}")
# kalo dikasih +.2f keliatan ada positif sebelum angka (+109.199)

print(f"\nangka des2 kalo ga make embel apa2 : {des2}")
# hasilnya cuman -109.12 karena angka 0 setelah angka 2 ga ditampilin
print(f"angka des2 kalo dikasih :f : {des2:f}") 
# kalo make float, angka 0 di belakang jadi banyak
print(f"angka des2 kalo dikasih .2f : {des2:.2f}") 
# ga ngasih efek apa2
print(f"angka des2 kalo dikasih +.2f : {des2:+.2f}")
# ga dikasih +.2f juga ga masalah kalo angkanya minus