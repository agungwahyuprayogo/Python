"""
mengecek apakah suatu huruf ada dalam suatu kalimat

misal
apakah "w" ada di "agung wahyu prayogo" ?
True, hasil jawaban dalam bentuk boolean
"""
cek = "W"
nama = "agung wahyu prayogo"

print(f"apakah {cek} ada di {nama} ? {cek in nama}")

"""
kenapa hasilnya False?
karena value cek hurufnya 'W' gede
sedangkan w yang ada di nama w kecil
jadi salah
"""

cek = "W"
nama = "agung wahyu prayogo"

print(f"apakah {cek} tidak ada di {nama} ? {cek not in nama}")

"""
apakah W tidak ada di nama yg hurufnya kecil semua?
True dong
"""

mashur = input("Masukan nama anda\n: ")
cekhur = input("Masukan huruf yang ingin anda cek di dalam nama : ")

print(f"'{cekhur}' ada di {mashur}? {cekhur in mashur}")