"""
nah kalo sebelumnya kita dah liatin contoh variable global 
yang bisa di panggil berbagai macam syntax

kali ini kita liatin contoh variable local 
yang ga bisa sembarangan dipanggil lagi diluar

misal def sih
"""

def fungsi_pangkat(angka, pangkat):
    hasil = angka**pangkat

# nah kita panggil si variable 'hasil' di fungsi pangkat
# print(hasil) # bakal error, tulisannya its not defined

