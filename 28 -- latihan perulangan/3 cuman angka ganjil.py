"""
oke kali ini kita bakalan bikin segiti tiga
tapi yang ditampilin cuman yg angkanya ganjil
misal 1,3,5,7 dst

trus make apaan biar nampil ganjil doang?
biar ketauan ganjil apa ga make modulus (%)

10 % 2 = 0
9 % 2 = 1
8 % 2 = 0

yang hasilnya 1 kita tampilin
"""

sisi = int(input("Masukan angka ganjil untuk membuat segitiga : "))

count = 1 # inisiasi variable untuk membantu iterasi


while True: # loop selama..
    if count%2: # Jika count habis dibagi 2 (count ganjil)
        print(" *"*count) # cetak * dengan sejumlah count
        count+=1
    else:
        count += 1 # jika count genap,
        continue # skip dan langsung looping kembali

    if count > sisi:
        break

print("berakhir")

"""
jadi ya kurang lebih kalo count%2 hasilnya ganjil atau 1 bakal print dan nambah 1
tapi kalo hasilnya genap tetep nambah satu tapi langsung looping lagi 
"""