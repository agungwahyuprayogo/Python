"""
oke pada kali ini kita bakal belajar manipulasi list
untuk pertama tama yang kita pelajari ini adalah index
index dimulai dari 0 sampai terkahir
lalu -1 paling kanan hingga paling depan

mungkin bakal bingung kalo ga di kasih liat secara langsung 
"""

#          0 (-4)          1 (-3)         2 (-2)          3 (-1)
data = ["gerad pique", "eric abidal", "lionel messi", "ronaldinho"]

"""
oke maksudnya apa 0 lalu ada -1 -2
didalam python yang berada di awal itu indexnya 0, lalu diikuti sehingga seterusnya kebelkang
kalo -1 itu anggep lah kita punya list yang panjang banget, tapi kita pengen ambil yang paling belakang
"""

data_pertama = data[0] # 0 itu mengindikasikan list paling awal
print(f"data pertama adalah : {data_pertama}")

data_terakhir = data[-1] # -1 itu mengindikasikan list paling terakhir
print(f"data list paling terakhir adalah : {data_terakhir}")

"""
ke untuk sekarang sesuai kan, data awal itu gerad pique make 0
dan untuk data paling terakhir itu ronaldino pake -1
gimana kalo -3? ya karena ini data listnya dikit jadi gampang keliatanya
tapi harusnya berhubung -1 ada di ronaldino, -3 ada di eric abidal
"""

data_minus_tiga = data[-3]
print(f"data ke -3 adalah : {data_minus_tiga}")

# dah sesuai kan?