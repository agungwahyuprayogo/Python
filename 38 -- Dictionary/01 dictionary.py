"""
jadi kemarin kita udah belajar mengenai list
sampe advance gitu nambah buku dan penulisnya

nah sekarang kita mau belajar mengenai dictionary
berbeda dari list, dictionary itu make key dan value

kalo list kan gini nih
"""

cnth_list = ["ini", "list", "ya?"]
print(f"ini contoh list : {cnth_list}")
print(f"list dengan index 1 adalah {cnth_list[1]}") # yang keluar 'list'

"""
kalo list kan akses value make index yak
nah kalo dictionary tuh beda

dia aksesnya tuh make key, langsung contoh aja ya
"""
cnth_dict = { # make kurung kurawal
    "nama" : "agung",
    "umur" : 24,                # bisa naro angka juga
    "sudah menikah?" : False    # boolean juga bisa
}

"""
dan aksesnya ga make index, tapi key
contoh key ada nama, umur, sudah menikah? 

kita kasih liat contoh dulu deh ya, bentuk dictionary kaya apa
dan akses melalui key nya kaya gmn.
"""

print(f"ini contoh dictionary : {cnth_dict}, {type(cnth_dict)}")

print(f"berapa umurnya? : {cnth_dict['umur']}") # dictionary[key]

