teman_teman = {
    "Agung" : "Agung Wahyu Prayogo",
    "Edo" : "Edo Subastian",
    "Deni" : "Deni Kurniawan",
    "Uray" : "Uray Clarisa Dina Aulia",
    "Dennise" : "Natasya Dennise Geraldin",
    "Tsamarah" : "Tsamarah Nabilah",
    "Bintang" : "Bintang Wahyu Sanjoyo",
    "Heni" : "Heni Septi Rahayu"
}

friends = teman_teman.copy()

print(f"dict teman2 sebelum diapa2in :\n{teman_teman}\n\n")
print(f"dict friends sebelum diapa2in :\n {friends}\n\n")

# okeh masih belum keliatan ya
# coba kita ubah

teman_teman["Agung"] = "Agoenk Wahjoe Prajogo"
# kita liat lagi, berubah ga yg di dict Friends

print(f"setelah agung diubah, dict teman2 menjadi :\n{teman_teman}\n\n")
print(f"setelah agung diubah, dict friends menjadi :\n {friends}\n\n")
# karena tadi pas copy kita make .copy(), diFriends gaikut berubah 

del teman_teman["Agung"]
print(f"setelah agung dihapus, dict teman2 menjadi :\n{teman_teman}\n\n")
print(f"setelah agung dihapus, dict friends menjadi :\n {friends}\n\n")

"""
ternyata udah ga kehapus
so its work
"""