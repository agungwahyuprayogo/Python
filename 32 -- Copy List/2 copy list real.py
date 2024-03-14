"""
oke kali ini kita bakal melalukan full duplicate
cukup simple sebenernya
tinggal variable baru = variable list sebelumnya.copy()

misal kita masukin lagi list a dan b yang ada sebelumnya
abis itu kita masukin c, abis itu ngelakuin perubahan di c
"""

a = ["Universitas", "Bhayangkara", "Jakarta", "Raya"]
print(f"\nlist a terdiri dari : \n{a}")

# karena ga pengen ribet biasanya kita tinggal gini :

b = a
print(f"\nuntuk b memiliki list seperti berikut : \n{b}")

print("\nsekarang kita pengen ubah Universitas jadi University di list b[0]")
b[0] = "University"

# buat buktiin kita print 22nya
print(f"\nsetelah perubah di b[0], list a sekarang : \n{a}")
print(f"\nsetelah perubahan di b[0], list b sekarang : \n{b}")

a.sort()
a.reverse()

print(f"\nsekarang menggubah list di a menjadi terurut dari abjad belakang")
print(f"\nsetelah perubahan list a menjadi : \n{a} ")
print(f"\nsetelah perubahan list b menjadi : \n{b} ")

print(f"\n\naddress list a : {hex(id(a))}")
print(f"address list b : {hex(id(b))}")

# sekarang kita mau copy list a ke c

c = a.copy() # simple kan?
print(f"ini list c terbaru setelah a.copy : \n{c}")

print(f"sekarang kita pengen ubah jakarta jadi surabaya")

c[2] = "Surabaya"
print(f"\n\nsetelah melalukan perubahan di c[2] hasil dari list a hingga c adalah :")

print(f"\n\nlist a saat ini : \n{a} dengan alamat : {hex(id(a))}")
print(f"\n\nlist a saat ini : \n{b} dengan alamat : {hex(id(b))}")
print(f"\n\nlist a saat ini : \n{c} dengan alamat : {hex(id(c))}")

"""
sekarang setelah kita menggunakan a.copy()
semua terlihat kalo yang berubah itu cuman list yang ada di list c
begitupun dengan alamat di list c juga berbeda dari list a dan b : 0x2292b18fe40
list c alamatnya : 0x2292b1948c0
"""