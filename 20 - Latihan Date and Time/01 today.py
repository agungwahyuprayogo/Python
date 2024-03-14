import datetime as dt
# kita import package datetime(waktu gitu deh gampangnya) as dt (sebagai dt)
# as nya ga harus dt, bisa detaim atau apa bebas

hari_ini = dt.date.today()
# 'dt' itu dari alias datetime diatas (liat baris 1 yang import) -> dt
# karena kalo ngetik datetime kelamaan, kita persingkat jadi dt
# 'date' tipe data nya
# 'today' syntax buat nampilin hari ini

# coba iseng2 ganti today ^ jadi tomorrow atau yesterday awkaok
# hari_esok = dt.date.yesterday() wkwk ga ada atribute yesterday
# hari_esok = dt.date.tomorrow() aokaowk ga ada juga

# nah gimana buat nampilin hari pada tanggal yg dimasukin?
# make atribut :%A
print(f"sekarang tanggal {hari_ini}, tepat hari {hari_ini:%A}") 
# :%A untuk menampilkan hari pada tanggal tersebut 
# tahun, bulan, hari

