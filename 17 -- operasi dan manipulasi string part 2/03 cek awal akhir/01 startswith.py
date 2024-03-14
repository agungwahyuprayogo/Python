# jadi di sini bisa cek awall
# make startswith()

# startwith("masukin apa yg pen dicek di dalem kurung ini")

cek_starts = "agung wahyu prayogo"
print(f"apakah {cek_starts} dimulai dengan kata agung? {cek_starts.startswith('agung')}")

print(f"apakah {cek_starts} dimulai dengan kata Agung? {cek_starts.startswith('Agung')}") # a huruf gede

# karena case sensitive, mau beda satu huruf dah jadi salah

masnaleng = input("Masukan nama lengkap anda : ")
ceknasdem = input("masukan lagi nama depan anda untuk mengecek apakah sudah betul atau belum :  ")
print(f"nama anda adalah '{masnaleng}' dan cek nama depan '{ceknasdem}' apakah sudah betul? {masnaleng.startswith(ceknasdem)}")