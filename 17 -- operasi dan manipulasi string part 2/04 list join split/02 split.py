# kebalikan dari join yang ngemisah list jadi string
# di split mau buat string jadi list

string = "agung wahyu prayogo"
list = string.split(' ')
# penggunaan " " spasi disini sebagai indikator, bagian mana yg mo dipisah
# misal pen misah pas spasi, ya ketika agung, trus ada spasi, si agung dipisah ke list
# begitu juga pas wahyu dan prayogo 

print(f"\nsebelum jadi list {string}\npas jadi list{list}")

s2 = "agungTwahyuTprayogo"
l2 = s2.split('T')

print(f"\nsebelum jadi list {s2}\npas jadi list{l2}")


univ = "Universitas_Bhayangkara_Jakarta_Raya"
# kalo diatas dipisahin sama huruf T, kali ini make underscore
pisah_univ = univ.split("_")
# pas disini kita masukin variable (univ) 
# lalu pas bagian split kita masukin underscore ("_") <- bukan emot 

print(f"\n\nsebelum di pisah {univ} sesudah dipisah {pisah_univ}")

kampuang = "Watubonang, Kecamatan Tawangsari, Kabupaten Sukoharjo, Provinsi Jawa Tengah"
pisah_kampuang = kampuang.split(", ")

print(f"sebelum dipisah {kampuang}, setelah dipisah jadi {pisah_kampuang}")