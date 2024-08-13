# looping dari list
"""
misal kita punya list, dan kita pengen print
itu ada berbagai cara, ada yang lewat loop,
ada yang lewat while, enumarate dll

untuk kali ini kita latihan make yang dari for loop dulu
"""

list = [4,9,1,5,0,3,9,2]

for i in list:
    print(f"sekarang angka ke {i}")
    # nanti tampil di samping "sekarang angka ke 4", dibawahnya "sekarang angka ke 9", dst


list_peserta = ["agung", "wahyu", "prayogo"]

for nama in list_peserta:
    print(f"sapa aja yang main? ada {nama}")