"""
studi kasus yang ketiga ialah, ketika kita ingin sort list
biasanya kan kita tinggal make .sort gitu
nah kita bisa buat make lambda
"""

# contoh make .sort biasa dulu
data_1 = ["Agung", "Wahyu", "Prayogo"]
data_1.sort()
print(data_1) # ketika di run, urutanya jadi agung prayogo wahyu

# ngurut dari yang terpendek ke terpanjang dari jumlah huruf
data_2 = ["Bintang", "Wahyu", "Sanjoyo"]
data_2.sort(key=len) # mengurutkan dari panjang karakter
print(data_2) # ketika di run, hasilnya Wahyu Bintang Sanjoyo 
# Bintang dan Sanjoyo sama2 7 huruf, kalo ada yg sama2 7, diurutin dari abjad

# misal make def buat ngurut
data_3 = ["Slamet", "Sedyo", "Raharjo"]

def panjang_nama(nama):
    return len(nama)

data_3.sort(key=panjang_nama) # ternyata bisa juga make key dari def
print(f"sorted list by def panjang : {data_3}")

"""
kalo make cara konvensional dan def kaya diatas kan lama ya
nah kalo make lambda, caranya gini nih
"""
# bingung make nama sapa njer
data_4 = ["Dedi", "Tri", "Wibowo"]
data_4.sort(key = lambda apakek:len(apakek)) # susah anjer ngapaalinnya demi dah
print(data_4)           # ^ jangan bingung sama nama 'apakek', nama bebas, yang penting tuh lambda nya

