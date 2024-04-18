"""
kalo ada list trus list, ada contohnya diatas
tapi kalo kita masukin manual lagi, angkanya ga masuk di dalemnya kotak dalam kotak lagi

nah nested list ini kepake banget kalo buat data yang banyak 
misalnya data peserta, kan di data peserta bisa ada data nama. umur,, kelamin, asal, dll
nah kita bisa make fitur nested list biar enak diliatnya
"""

peserta_0 = ["agung", 23, "laki - laki"]
peserta_1 = ["eli", 50, "perempuan"]
peserta_2 = ["widodo", 15, "laki - laki"]

data_peserta = [peserta_0, peserta_1, peserta_2]
print(f"data peserta \n {data_peserta}")
# kalo print normal kan gaenak nih liatnya dempet - dempet gitu
# nah bisa di bikin rapi kek gini

for peserta in data_peserta:
    print(f"nama\t: {peserta[0]}")
    print(f"umur\t: {peserta[1]}")
    print(f"gender\t: {peserta[2]}\n")