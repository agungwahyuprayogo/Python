"""
menampilkan leading zero
jadi maksudnya mau nampilin beberapa 0 di depan angka
"""
bulet = 1291391873
koma = 190.89012871

# sebelumnya kita belajar kalo mau nampilin 2 atau 3 angka setelah koma bisa make .3f
# sekarang kita coba buat lebih advance
# jadi total angka di variable koma ada 12 (koma termasuk) diitung dari kiri ke kanan
# nah kita coba latihan buat nampilin sebagian aja mmisal 9 angka di depan koma

print(f"{koma:9.3f}")
# maksud diatas, coba tampilin value / nilai dari variable koma,
# tampilin 9 angka setelah 4 karakter (koma dan 3 digit angka setelah koma)
# maka yang tampil adalah "  190.890"
# kok ada spasi?
# karena permintaanya aneh, 9 angka. 
# sedangkan kalo koma dan 3 digit belakang diitun 4
# maka butuh 2 angka lagi (sebelum koma hanya ada 3 digit) (9-4-3 = 2) 
# jadi ada 2 spasi di depan

# masih bingung?
# kita kasih angka 0 biar keliatan

koma1 = 190.1111111
print(f"{koma1:09.3f}")
# masih mirip kek diatas, tolong tampilin 9 angka (termasuk 3 digit setelah koma)
# maka hasilnya adalah "00190.111"
# angkanya kok cuman ada 8? iya komanya juga diitung 
# jadi 9 digit komanya juga ikut diitung jadi nya ada 9