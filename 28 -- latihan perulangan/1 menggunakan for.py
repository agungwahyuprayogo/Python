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
