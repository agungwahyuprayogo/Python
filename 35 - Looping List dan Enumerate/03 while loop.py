# kali ini kita mau looping make while loop.
# mirip for loop yang make range tapi kita nambahin variable baru

list = [1,9,2,8,3,7,4,6,5]

panjang = len(list)
i = 0

while i < panjang:
    print(f"sekarang angka ke {list[i]}")
    i += 1


"""
jadi gini

kita ada list = [1,9,2 ....]

nah karena kita make while, kita butuh inisiasi buat masuk ke list
caranya gimana, buat len(lenght/panjang)

nah hasil variable panjang ini = 9 atau (0,8)

kita masukin deh while i < panjang, print ...
nah itu ide i = 0 biar ada kerjaan gitu si while

kalo i masih 0 < 9,
makan print "sekarang angka ke {list[index i]}

jika index i = 0, maka list juga nampilin index 0, maka list[0] = 1
list index 1 = 9,

begitu terus sampe index selalu nambah 1 (i += 1)
nah kalo i udah sampe 9 atau 8 di python
maka print list juga berhenti, diharapkan mengerti wkwk

"""