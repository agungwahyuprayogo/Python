"""
kali ini kita bakal nambah, apus, dan ubah data
kenapa ga dipisah aja filenya?
ya karena biar keliatan bedanya

oke kali ini kita bakal latihan nambah item pada list
"""

print("Menambah item pada list".center(35,"-"))
data = ["gerad pique", "eric abidal", "lionel messi", "ronaldinho"]

print(f"data sebelum ditambah : \n{data}")

# kali ini misal kita pen nambah neymar da silva di posisi kedua (1, krn awal itu 0)
# data.insert(posisi,item)

data.insert(1,"Neymar da silva")
print(f"\nsetelah insert : \n{data}") # harusnya abis gerad pique ada neymar

"""
nambah make nomer itu opsional kadang 
kadang make kadang ga, tapi kalo misalkan pengan nambah di posisi akhir gpp
kita bisa make append, jadi append ini bakal nambah item ke posisi paling belakang
"""
data.append("David Villa") # nambah item di posisi paling akhir
print(f"\ndata setlah append adalah : \n{data}")

"""
oke bisa ga nambah list dengan list?
gw baru tau bisa juga si
oke kita buat list baru dulu
"""
data_madrid = ["Cristiano Ronaldo", "Sergio Ramos", "Pepe", "Karim Benzema"]
# data.exterd(nama list lain yg pen digabung)
data.extend(data_madrid)
print(f"\nlist terbaru barca dan madrid adalah : \n{data}")