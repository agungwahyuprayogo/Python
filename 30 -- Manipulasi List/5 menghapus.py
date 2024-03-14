"""
setelah belajar index, panjang atau banyak data pada list, menambah, mengubah,
kali ini kita akan belajar mengenai hapus atau delete 

untuk menghapus ada 2 cara, yakni :
remove (huruf jangan ada perbedaan baik dari besar kecilnya huruf)

"""

data = ["gerad pique", "eric abidal", "lionel messi", "ronaldinho"]
print(f"data sebelum dirubah adalah : \n{data}")

data.remove("gerad pique") # kali ini kita pen ngapus gerad pique karena tersandung kasus perselingkuhan
print(f"\ndata setelah di remove : \n{data}")
# data.remove("Gerad Pique") # error karena ada perbedaan huruf

"""
untuk menggunakan remove, pertama kali yang harus kita perhatikan adalah
jangan sampai ada perbedaan satu karakter pun didalam data list
sebagai contoh diatas, gerad pique didalam list menggunakan huruf kecil
namun jika kita mencoba me-remove menggunakan hruf kapital, akan error 
karena tidak ada data didalam list gerad pique yang menggunakan huruf kapital

selain remove kita bisa menggunakan .pop
.pop ini bila kita ingin menghapus data pada list pada bagian paling akhir
tanpa perduli siapa yang berada di posisi paling akhir tersebut
"""

data.pop() # jangan lupa tanda kurung
print(f"\ndata list setelah pop : \n{data}")

