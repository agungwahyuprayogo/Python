# belum belajar list tapi disini diliatin bagaimana cara gabungin list
# jadi satu string

list = ['agung', 'wahyu', 'prayogo']
# jadi di sini awalnya ada list, dimana list itu .. belum belajar list sih sebenernya
# intinya list itu diawali dan diakhiri dengan buka tutup kurung
# tiap elemen ada tanda petik dan dipisahkan dengan koma
# nah dari list diatas kita pengen gabung jadi satu

gabung = " ".join(list)
# didalem tanda kutip sengaja kosong (sebenernya ada spasi)
# buat misahin element yang ada di list tadi
# nah karena udah di .join(variable list) 
# jadi lah agung wahyu prayogo ga kepisah lagi sama koma dan tanda kutip diatasnya

print(f"sebelum di pisah {list} \nsesudah gabung {gabung}")


univ = ['Universitas', 'Bhayangkara', 'Jakarta', 'Raya', 'II']

gabung_univ = "_".join(univ)
# kalo diatas dipisah dengan tanda spasi, kalo disini kita make underscore
# maka nanti dibawah hasilnya jadi Universitas_Bhayangkara.. dan seterusnya 
# karena diatas buat misahin make _
print(f"\nsebelum dipisah {univ}, \n\nsesudah digabung {gabung_univ}")

kampung = ['Jawa Tengah', 'Sukoharjo', 'Tawangsari', 'Watubonang']

gabung_kampung = "-".join(kampung)
print(f"sebelum dipisah : {kampung}, sesudah dipisah {gabung_kampung}")