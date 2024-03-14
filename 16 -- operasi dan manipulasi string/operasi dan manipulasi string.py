# operasi menyambung string

nama_depan = "agung"
nama_tengah = "wahyu"
nama_belakang = "prayogo"

nama_lengkap = nama_depan + " " + nama_tengah + " " + nama_belakang
print(nama_lengkap)

# menghitung panjang string
print("banyak karakter dalam nama lengkap :", len(nama_lengkap))

# ngecek huruf / karakter di sting
print("apakah ada huruf 'a' di nama lengkap? :", "a" in nama_lengkap)

print("apakah ada tidak ada huruf 'x' di nama lengkap? :", "x" not in nama_lengkap)

# mengulang string
print("hai halo " * 10)

# indexing 
print("index ke 3 nama lengkap :" + nama_lengkap[3])
print("index ke 0 nama lengkap :" + nama_lengkap[0])
print("index ke -1 nama lengkap :" + nama_lengkap[-1])    # ke paling kanan kalo minus
print("index ke -2 nama lengkap :" + nama_lengkap[-2])    # ke paling kanan lanjut kiri
print("index 0 - 5 :" + nama_lengkap[0:5])      # dari 0 sampe sebelum 5
print("index 5 - 11 :" + nama_lengkap[5:11])    # dari 5 sampe sebelum 11
print("print dari 0 - 11 lompat 2 :" + nama_lengkap[0:11:2])

# item paling kecil
print("item paling kecil di agung :" + min(nama_depan))
print("item paling gede di agung :" + max(nama_depan))

# menghitung jumlah huruf pada string
jumlah_a = nama_lengkap.count("a")
print("jumlah a dalam nama lengkap : " + str(jumlah_a))