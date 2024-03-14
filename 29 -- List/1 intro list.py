"""
Ok kali ini kita akan membahas list
mm apa itu list?

list itu sekumpulan data
misal ada banyak data kan

data1 = a
data2 = b 
data3 = c

dst, kalo ada ribuan kan repot. nah bagaimana biar ringkas
ada yg namanya list
list = [1,2,3]

bentukanya seperti itu, ciri-cirinya ada variable diikuti kotak kurung siku dan didalamnya terdapat koma
kalo di bahasa pemograman lain namanya array
di python juga ada array tapi beda jenis, suatu saat nanti akan kita pelajari
"""

list1 = [1,2,3] 
print(f"ini adalah list yang pertama : {list1}")

"""
contoh list yang pertama, diawali nama variable. 
lalu value dari variable tersebut dipisahkan dengan koma

apakah data didalam list harus selalu urut atau boleh acak?
tentu saja boleh
"""
list2 = [2,5,1,3]
print(f"ini adalah list yang kedua : {list2}")

"""
dari contoh diatas terlihat kalo list itu ga harus urut dan bisa acak dari berapa aja
nah apa list cuman bisa buat angka aja?
ga dongg.. di python kan ada string, numbers (contoh diatas) dan boolean (true false)
"""

list_string = ["agung", "Wahyu", "prayogo"]
print(f"ini adalah list string : {list_string}")

list_boolean = [True, False, False, True]
print(f"ini adalah list boolean : {list_boolean}")

"""
oke dari dua list diatas terlihat untuk list string ketika di run 
tanda petik yang muncul hanya satu padahal kita menggunakan kutip 2
haha gapapa
lalu untuk boolean ketika di run tidak tanpil dalam bentuk 0 atau 1
tapi langsung dalam bentuk True dan False

nah apakah list cuman bisa cuman buat satu tipe data?
ga bisa dicampur campur
dalam artian dalam value list bisa ada numbers, strings, dan boolean dalam bersamaan
"""

list_campur = [1, "Satu", False, 0, "nol", True]
print(f"ini adalah list campuran : {list_campur}")