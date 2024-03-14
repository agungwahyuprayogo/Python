"""
disini bisa kita atur make format duit
"""
# tanpa parameter

ribuan1 = 10000
print(f"duit yang saya miliki adalah {ribuan1}")
# gaenak liatnya, bisa keder yang matanya minus atau sipit (rasis)

ribuan2 = 100000
print(f"duit saya masih {ribuan2:,}")
# tanda koma habis nama variable dan titik dua digunakan untuk memberi titik uang
# misal kalo kita masukin 1000, kita make koma jadi 1,000
# kalo masukin 100000 jadi 100,000
# pokoknya otomatis ada tanda koma setiap dari 3 digit paling belakang

# print(f"duit saya masih {ribuan2:.}")
# ternyata ga bisa selain koma

masuang = int(input("Berapa jumlah nominal uang anda sekarang?\n(jangan masukan tanda koma atau titik) : "))

print(f"Nominal uang anda sekarang adalah Rp. {masuang:,}")