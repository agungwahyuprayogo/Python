banyak = [1,2,3,4,5,6,7,8,9,10]

for i in banyak:
    print(i)
print("program 1 dah kelar\n")

"""
bayangin kalo list yang perlu dimasukin ada ribuan atau bahkan jutaan
ga mungkin kan ngetik ngetik satu satu dan manual
nah biar ga cape kita bisa masukin yang namanya range
range disini cukup masukin angka sebagai ujung terakhirnya

misal rang2(11), maka jika dipanggil lewat loop nanti paling mentok di angka 10 (sebelum 11)
begitupun kalo range(1000), maka sampe 99 (sebelum 100)
"""
b1 = range(11) # jadi bakal ngisi angka dari 0 hingga sebelum 11

for b in b1:
    print(f"angka ke {b}")
print("program 2 kelar\n")

print(b1)

for i in range(5): # dan ternyata ga perlu buat variable
    print(f"angka ke {i}")
print("program 3 kelar\n")

# ada lagi cara terakhir 
for i in range(1,5): # jadi range disini dimulai dari 1 sampe sebelum 5
    print(f"angka {i}")
print("program 4 kelar\n")

# kalo masih bingung 
for i in range(3,10): # jadi range disini dimulai dari 3 sampe sebelum 10
    print(f"angka {i}")
print("program 5 kelar\n")