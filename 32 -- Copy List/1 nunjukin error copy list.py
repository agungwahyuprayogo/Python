"""
oke sekarang dah part 32 copy list,
sebenernya gatau si kalo ga liat video masih bisa paham apa ga
tapi coba dulu deh

jadi kalo biasanya kita pen copy data ke variable lain kan cuman kek gini :
misal a = 12
trus kita pengen ada variable baru ikutin a
tinggal b = a
maka nanti kalo kita print b ya muncul angka 12

tapi kalo di dalam list itu fatal sih
dalam artian kalo kita pengen ngubah sesuatu di variable a, variable b akan ikut berubah
kok bisa?

oke kita buat list dulu buat a trus kita masukin ke b
"""

a = ["Universitas", "Bhayangkara", "Jakarta", "Raya"]
print(f"\nlist a terdiri dari : \n{a}")

# karena ga pengen ribet biasanya kita tinggal gini :

b = a
print(f"\nuntuk b memiliki list seperti berikut : \n{b}")

"""
sampe sini ga ada yang aneh
tapi sekarang coba kita liat
kalo kita ubah data di list a, si b juga ikut berubah
"""

print("\nsekarang kita pengen ubah Universitas jadi University di list b[0]")
b[0] = "University"

# buat buktiin kita print 22nya
print(f"\nsetelah perubah di b[0], list a sekarang : \n{a}")
print(f"\nsetelah perubahan di b[0], list b sekarang : \n{b}")

"""
so weird right
padahal yang kita ubah di list b dengan index 0
tapi pas di print malah 22nya yang keubah

oke kalo masih ga percaya kita ubah lagi deh
ubah list a jadi urut
"""
a.sort()
a.reverse()

print(f"\nsekarang menggubah list di a menjadi terurut dari abjad belakang")
print(f"\nsetelah perubahan list a menjadi : \n{a} ")
print(f"\nsetelah perubahan list b menjadi : \n{b} ")

"""
see
ketika pengen ngubah jadi reversi di bagian list a
list b ikut berubah njir
karena apa, karena ketika b = a, yang ngikut tuh bukan cuman datanya doang
tapi address dari a juga ikut ke b
dalam artian cuman beda nama list doang

gimana cara liat address list a dan b sama?
"""

print(f"\n\naddress list a : {hex(id(a))}")
print(f"address list b : {hex(id(b))}")

"""
can u see that
alamat list a dan b sama sama 0x1ff997cfe80
karena ketika menggunakan syntax b = a itu pass by refrence

sekarang kita pengen nyoba bagaimana copy yang bener2 copy
ibarat copy dari device satu ke device lainya 
atau full duplicate

langsung ke file
"""