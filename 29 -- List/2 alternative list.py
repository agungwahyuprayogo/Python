"""
oke di file "1 intro list.py" dah dijelasin list itu apa dan cara buatnya gimana
tapi kali ini kita akan latihan buat list dengan singkat menggunakan range
range? ya yang bentukanya tuh kek gini
"""
range1 = range(1,10) # buat data dimulai dari 1 sampe sbelum 10
"""
kalo range1 langsung di print ga langung dalam bentuk list, 
kudu di convert lagi make variable baru
"""
list_range = list(range1) # jangan lupa make list didepanya 
print(f"ini adalah list range : {list_range}")

"""
jangan lupa sebelum convert, masukin syntax list
lalu masukin variable range tadi dalam kurung

dan ketika di run yang tampil adalah 1 - 9 (sebelum 10)

lalu kita buat lagi dengan step
step? ya jadi langkah setiap angka
"""

range2 = range(1,10,2) # start from 1, until before 10, step 2 numbers
list_range2 = list(range2)
print(f"ini adalah list range kedua : {list_range2}") 

"""
dah dikasih komen diatas
jadi dimulai dari 1, berhenti sebelum 10, lalu langkah setiap angka 2
maka yang tampil adalah 1, 3, 5, 7, 9
"""