"""
kali ini kita bakal belajar args 

jadi gini, args ini fungsinya kepake kalo input kebanyakan 
dan kita males gitu buat argument di def kebanyakan juga
nah disini kita make args

kita buat contohnya dulu deh kalo cara lama yg argument & inputanya banyak
"""

def biodata(nama, umur, kelamin):
    print(f"halo saya {nama}, umur saya {umur} tahun, kelamin saya adalah {kelamin}")
    return

biodata("agung", 24, "laki-laki")

"""
atau kita buat list deh make list kaya gini
"""

def bio(data_list):
    data = data_list.copy()
    nama = data[0]
    tinggi = data[1]
    berat = data[2]
    print(f"halo dia {nama} tingginya {tinggi} dan beratnya {berat}")

bio(["indra", 165, 75]) # dan ribet juga lagi kita masukinnya kudu list biar bisa masuk list juga

"""
nah untuk mengindari keribetan itu, terciptalah *args
jadi args ini yang buat lebih singkat dalam memasukan input di argument

"""