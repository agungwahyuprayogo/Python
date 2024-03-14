"""
oke cepet banget rasanya
kali ini kita bakal ngurutin data di dalam list menjadi lebih urut
ntah itu urut dari terkecil 
atau pengen dari terbesar juga boleh
"""
data_angka = [1,6,4,3,7,5,1,0,9,2,8]
data_string = ["tsamarah","dwi","fenny","dennise","uray"]

print(f"data angka sebelum di urutkan : \n{data_angka}")
print(f"data string sebelum di urutkan : \n{data_string}")

data_angka.sort()
data_string.sort()

print(f"stelah diurutkan menjadi : {data_angka}")
print(f"stelah diurutkan menjadi : {data_string}")

"""
oke sebelumnya masih acak, setlah make syntax sort jadi terurut
dan untuk data string mungkin ada yg nanya kenapa dennise dulu baru dwi?
karena dennise lebih special dari dwi yang cuman mainin hati :D

ga ga bercanda
tapi lebih karena dennise terdiri dari huruf lebih awal dari pada dwi
kalo kita lihat setlah d adalah e didalam kata dennise
sedangkan dalam kata dwi, setalah d adalah w

yang dapat disimpulkan e dan w, lebih dulu yang e
gitu..

oke lanjut, lalu bagaimana cara agar membuat urutan data dari terbesar?
pertama yang paling penting adalah sort terlebih dahulu seperti diatas
karena apa? kita ketik syntax dulu
"""

data_string.reverse()
data_angka.reverse()

print(f"data setelah reverse: \n{data_angka} lalu \n{data_string}")