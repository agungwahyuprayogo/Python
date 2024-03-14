"""
sama kek di word, ada rata kiri, rata kanan, rata tengah
 rjust ljust sama center gitu juga
"""

rt_knn = "kanan".rjust(20) # jumlah karakter
print(f"'{rt_knn}'") 

rt_knn1 = "kanan".rjust(10) # jumlah karakter
print(f"'{rt_knn1}'") 

# biar keliatan keren, bisa di tambah parameter

rt_knn3 = "kanan".rjust(20,"-") # jumlah karakter
print(f"'{rt_knn3}'") 

rt_knn4 = "kanan".rjust(20,">") # jumlah karakter, ">" karakter selain spasi
print(f"'{rt_knn4}'") 

# baca komentar di center dan ljust

rata_tengah = "ini rata tengah".center(25,"-")
rata_kiri = "ini rata kiri".ljust(25,"<")
rata_kanan = "ini rata kanan".rjust(25,">")

print(f"\n\n{rata_tengah}\n{rata_kiri}\n{rata_kanan}")

