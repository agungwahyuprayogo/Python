"""
ada berapa huruf "a" di dalam "agung wahyu prayogo" ?
"""
cek = "a"
nama = "agung wahyu prayogo"
print(f"ada berapa {cek} dalam {nama}", nama.count(cek))

masnam = input("Masukan nama anda\n :")
cekhur = input("huruf yang perlu dicek jumlahnya dalam nama\n :")
print(f"\nnama anda adalah '{masnam}' dengan total huruf di dalam nama tersebut adalah {len(masnam)} huruf, dan huruf '{cekhur}' yg ada di {masnam} ada sebanyak {masnam.count(cekhur)}" )

maspus = input("Masukan nama kampus anda : ")
cekhurpus = input("huruf yang akan diperiksa adalah : ")
print(f"nama kampus anda adalah '{maspus}', dan huruf yang akan anda cek adalah '{cekhurpus}', dicek menggunakan python ada sebanyak {maspus.count(cekhurpus)} huruf")