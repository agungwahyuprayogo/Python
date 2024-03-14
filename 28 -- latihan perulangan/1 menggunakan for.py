"""
jadi targetnya buat segitiga siku siku
misal kek gini :
* 
* *
* * *
* * * *
dan seterusnya
nah kalo make perulangan begimane? nih kalo make for
"""

# menggunakan for

sisi = int(input("Masukan panjang sisi : ")) # masukin dulu angka paling gedenya berape

# dummy variable
count = 1 # ini berfungsi biar nanti makin kebawah nambah satu nantinya
print("awal program for".center(20,"-"))
for i in range(sisi): # panggil angka dari paling kecil sampe angka inputan
    print(" *"*count) # tiap ke bawah di kali count (disini masih 1)
    count += 1 # nah disini make += 1 biar ke bawahnya makin nambah

print("akhir program for".center(20,"-"))

"""
jujur baru tau gw sih kalo misalkan kita input angka 4, lalu dipanggil menggunakan fot
bakal muncul dari 1 sampe 4, kita coba 
"""

input_angka = int(input("Masukan input coba2 : "))

for i in range(input_angka):
    print(i)

"""
oke make kodingan diatas ternyata berhasil
cumann... kalo kita input angka nya 2
nanti ketika dipanggil make for cuman muncul 0, dan 1
karena di python sendiri kita tau, kalo masukin 4, yang tampil cuman 3
begitu dan seterusnya

makanya for diatas make += biar ga ada 0, langsung 1 sampe angka inputan
"""
# menggunakan while
# inget, kalo make while ga bakal berhenti selama hasilnya true
# jadi bisa diakalin make break biar berhenti

print("awal program while".center(20,"-"))