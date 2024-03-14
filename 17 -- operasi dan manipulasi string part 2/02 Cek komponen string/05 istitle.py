## istitle adalah syntax untuk apakah value di dalam variable itu 
# semua kata dimulai dari huruf besar

while True:

    cek1 = "agung wahyu prayogo"

    print(f"apakah {cek1} kapital? {cek1.istitle()}")


    # inget -> .title() ada buka kurung tutup kurung
    # title berkaitan sama judul
    # biasnya judul film, judul buku tiap kata kapital 

    cek2 = "Agung wahyu Prayogo"
    print(f"apakah {cek2} kapital? {cek2.istitle()}")

    # karena case sensitive, mau yg lain kapital di wahyu ga kapital, 
    # bakal dianggep False

    cek3 = "Agung Wahyu Prayogo"
    print(f"apakah {cek3} kapital ? {cek3.istitle()}")

    masnam = input("Masukan nama anda : ")
    print(f"Nama anda adalah '{masnam}'. apakah sudah berbentuk kapital? {masnam.istitle()}")

    ulangi = input("Pengen ngulang kodingan ini? (y/n)").lower()

    if ulangi != 'y':
        break