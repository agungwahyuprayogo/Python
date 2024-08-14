teman_teman = {
    "Agung" : "Agung Wahyu Prayogo",
    "Edo" : "Edo Subastian",
    "Deni" : "Deni Kurniawan",
    "Uray" : "Uray Clarisa Dina Aulia",
    "Dennise" : "Natasya Dennise Geraldin",
    "Tsamarah" : "Tsamarah Nabilah",
    "Bintang" : "Bintang Wahyu Sanjoyo",
    "Heni" : "Heni Septi Rahayu"
}

print(f"ini dict teman2 : {teman_teman}\n\n")

"""
nah masukin nama yang banyak kita gunain disini
misal kita pengen buat dict baru namanya circle_ciwi
dan kita pengen ngilangin dari dict teman_teman

kita make .pop("keys") buat ngilangin nama cewe di dict teman2
lalu pindah ke 
"""

# hapus Uray dari temen2, masuk ke circle cewe
circle_cewe = teman_teman.pop("Uray","Dennise")
# kelemahanya cuman bisa uray doang, denise ga masuk :( 

print(f"ini dict teman2 ketika uray di hapus : \n{teman_teman}\n\n")
print(f"ini dict circle cewe {circle_cewe}")

# bisa juga ya make .popitem()
# bedanya kalo .popitem yang diambil data yang paling terakhir

circle_cewe = teman_teman.popitem()
print(f"ini dict tearkhir {circle_cewe}")
# dan ternyata ga nambah, tapi uray kehapus dan jadi heni doang

# kita cek lagi sisa dict temen2
print(f"\n\nsisa orang di dict temen2 = {teman_teman}")

# well