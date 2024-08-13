data_dict = {
    "gung" : "agung wahyu prayogo", # key dan value ke 1
    "subs" : "edo subastian"        # key dan value ke 2
}
print(f"\ndata dictionary = {data_dict}")

# panjang dictionary
print(f"\npanjang dari dict nya adalah : {len(data_dict)}")

# cek key
print(f"\napakah key gung ada di dictionary? {"gung" in data_dict}")

# mengakses value (read)
print(f"\napa value dari gung? {data_dict["gung"]} ")
# print(f"apakah ada value dari key 'muah'? {data_dict("muah")}") # kalo key ga ada di dict, suka error

print(f"\napakah ada value dari key 'muah' ? {data_dict.get("muah")}") 
# make .get biar ga error

# bisa juga make message
print(f"\napakah ada key 'kiis'? {data_dict.get("kiss","key tidak ditemukan")}")

# meng update data dictionary
data_dict["gung"] = "Agoenk Wahjoe Prajogo"
print(f"\ndata terbaru setelah berubah : {data_dict}")

# ada cara lain buat update
data_dict.update({"subs" : "Edo Subastian"})
print(f"\nData terbaru setelah edo diubah : {data_dict}")

# kalo key belum ada di dictionary, nanti otomatis ke add
data_dict.update({"mega" : "Megawati Soekarno Poetri"})
print(f"\nData terbaru setelah ditambah banteng : {data_dict}")
# di atas mega ga ada, tapi pas kita update otomatis nambah

# hapus key dan value dari dictionary
# misal apus agung
del data_dict["gung"]
print(f"\nData terbaru setelah agung ga dihapus : {data_dict}")
