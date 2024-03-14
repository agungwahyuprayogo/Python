"""
kalo ini simple aja 
kita pengen tau seberapa banyak list yang ada di dalam suatu variable
kita pake aja yg nama2 pemain barca dulu
"""

data = ["gerad pique", "eric abidal", "lionel messi", "ronaldinho"]

bnyk_data = len(data)
print(f"berapa banyak nama pemain disitu? : {bnyk_data}")

data_range = [i for i in range(0,100,5) if i %5 == 0]
# tolong buatkan i dari 0 sampai 100 dengan step 5, 
# dimana angka tersebut jika dibagi 5 hasilnya 0
print(f"angka berapa saja yang ada di data range? : \n{data_range}")
print(f"berapa banyak total angka dalam list tersebut? {len(data_range)}")