"""
kali ini kita mau bahas fungsi, atau function dalam bahasa inggris
jadi syntax fungsi ini bisa di panggil ketika kita membutuhkannya biar ga kebanyakan ngetik

for example aja biar gampang nangkepnya
kita pengen print biodata gw, ga perlu kita ketik semua lalu print 3x

tinggal kita buat di def (syntax fungsi) lalu masukan program yang kita mau
nah kalo kita pengen print biodata kita, tinggal panggil aja fungsi tersebut

kita langsung ke contoh aja ya kalo ga paham
atau coba liat video https://www.youtube.com/watch?v=ywE2eqG3-kc&pp=ygUXa2VsYXMgdGVyYnVrYSBweXRob24gNDQ%3D
buat lebih paham secara penggambaran
"""

# misal kita pengen print hellow world sebanyak 5x
print("Hello World")
print("Hello World")
print("Hello World")
print("Hello World")
print("Hello World")

"""
nah sebenarnya bisa kita make def buat nampilin itu juga, 
jadi ga perlu ngetik sampe 5x
"""

def hello_world():
    print("-hello world") # buat bedain dari function

# lalu kita panggil functionnya
hello_world()

"""
mungkin sampe sini kalian berpikir kalo,
"yailah gitu doang pake segala buat function"

gini, soalnya itu dikit, cuman ada kata "Hello World" 
jadi lu mikirnya ga terlalu penting

nah tapi bagaimana kalo misalkan lu buat bidodata diri gitu 5x
apa iya lu ketik semua dari nama, umur, jenis kelamin dan segala detailnya sebanyak 5x?
kan ga. mungkin bisa tapi tuh bakal buang waktu banget

nah makanya ada fungsi ini buat menghemat waktu kita
misal kita buat fungsi biodata ya
"""

def biodata():
    print("""
Nama    :   Agung Wahyu Prayogo
Umur    :   24
Status  :   Belum menikah
""")


"""
nah tinggal kita panggil 5x, ga perlu kita ketik ulang semua
""" 
biodata()
biodata()
biodata()
biodata()
biodata()


"""
maka lu bisa menghindari jari dan tangan lu dari cidera njir 
tanpa harus lu ketik semua dan lu ulang sebanyak 5x

dan untuk sementara perkenalan soal def atau function
kedepanya kita bisa buat fuction buat ngolah angka berdasarkan nilai input
"""