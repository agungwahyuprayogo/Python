data_angka = [1,6,4,3,7,5,1,0,9,2,8]
data_string = ["tsamarah","dwi","fenny","dennise","uray"]

"""
oke lanjut ke pelajaran kedua,
kali ini kita pengen cari tau bagaimana cara mengetahui index suatu data pada list
kalo kemarin kan index buat print data sama ubah data
nah kalo kita bingung data itu ada dimana, kita bisa cari make index

misal kita make data string deh
"""

print(f"ada di urutan (index) ke berapa si tsamarah? : {data_string.index('tsamarah')}")

"""
btw itu tulisan di dalem make petik satu ya. kalo make petik dua error
kalo awalannya make petik satu, tulisan didalem index make petik 2
"""

print(f"ada di urutan (index) ke berapa si uray? : {data_string.index('uray')}")
#print(f"ada di urutan (index) ke berapa si Dwi? : {data_string.index('Dwi')}")

"""
dan sekali lagi perlu diingat
python itu sensitive sekali sama perbedaan huruf besar dan kecil
jadi emang kudu jeli sekali sama ketikan kita di program python ini
kalo ga yaaa... bakal error
contohnya pas nyari Dwi diatas ketika make 'D' gede
"""