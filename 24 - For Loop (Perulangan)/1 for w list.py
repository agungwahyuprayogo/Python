"""
kalo di if else kemarin kan jalurnya kebawah
jadi kalo setiap kondisi terpenuhin, bakal lanjut ngarah ke akhir

beda dengan loop, loop bakal terus berjalan selama kondisinya terpenuhi
for (perulangan atau looping)

contoh gampangnya 
misal lagi di kebun binatang
binatang yg ada di kebun ada singa, macan, harimau dan gajah
44 nya itu masuk daftar binatang di kebun binatang
nah di loop ini kodingan akan terus berjalan selama kondisinya benar

misal disuruh sebutin binatang yg ada di kebun binatang tadi
anggep lah kebun binatangnya masih baru, cuman ada singa dkk
maka ketika di panggil yg muncul hanya ada singa, macan, harimau & gajah
diluar daftar itu kan ga ada, otomatis langsung berhenti

intinya terus berulang selama kriterianya memenuhi
untuk belajar , pertama kita gunakan terlebih dahulu list
"""

# for kondisi:
#     aksi

angka1 = [0,1,2,3,4]

for i in angka1:   # jadi, tolong sebutin angka apa saja yang ada di variable angka1
    print(f"posisi ke {i}") # tolong print posisi ke (setiap nilai yg ada di dalam variable angka1)
print("Program berakhir\n") # kalo misal semua udah ditampilin, langung berhenti

angka2 = [2,8,5,10] # angka ga harus urut, bisa acak dan bisa dari gede dulu baru ke kecil

for i in angka2:   # mirip yg diatas
    print(f"posisi ke {i}") # kaya diatas cuman beda nilai angka di dalam variable doang
print("Program berakhir\n") 


