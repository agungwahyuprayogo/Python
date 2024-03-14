# jadi di sini bisa cek akhiran
# make endswith()

# endswith("masukin apa yg pen dicek di dalem kurung ini")
while True:

    cek_ends = "agung wahyu prayogo"
    print(f"apakah {cek_ends} diakhiri dengan kata ogo? {cek_ends.endswith('ogo')}")

    print(f"apakah {cek_ends} diakhiri dengan kata Agung? {cek_ends.endswith('Prayogo')}")

    # karena case sensitive, mau beda satu huruf dah jadi salah

    masnaleng = input("Masukan nama depan anda : ")
    ceknambek = input("masukan lagi nama belakang anda untuk mengecek sebelumnya sudah betul atau belum :  ")
    print(f"nama anda adalah '{masnaleng}' dan cek nama belakang '{ceknambek}' apakah sudah betul? {masnaleng.endswith(ceknambek)}")

    ulangi = input("Pengen ngulang kodingan ini? (y/n)").lower()

    if ulangi != 'y':
        break