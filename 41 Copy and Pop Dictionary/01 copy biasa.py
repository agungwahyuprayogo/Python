"""
kita ga make dictionary agung dan ubj lagi,
kita kali ini latihan buat copy dari satu dictionary ke dictionary lain
ada banyak cara, dan bisa aneh juga haha
"""
# kita buat key dan values yang banyak dulu
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

# kita liat dulu dictionary diatas
print(f"dict teman_teman : {teman_teman}\n\n")

# kita coba copy biasa dulu
friends = teman_teman
print(f"dict friends : {friends}\n\n")

"""
nah kalo copy nya gitu doang, cuman make =
nanti kalo ada yg kehapus dan keubah di dict teman_teman, keubah juga di dict friends

misal ya kita ubah di Agung, valuenya jadi Agoenk
"""

teman_teman["Agung"] = "Agoenk Wahjoe Prajogo"
# kita liat lagi, berubah ga yg di dict Friends

print(f"setelah agung diubah, dict teman2 menjadi :\n{teman_teman}\n\n")
print(f"setelah agung diubah, dict friends menjadi :\n {friends}\n\n")
# ternyata di dict Friends juga ikut berubah, coba deh kalo hapus

del teman_teman["Agung"]
print(f"setelah agung dihapus, dict teman2 menjadi :\n{teman_teman}\n\n")
print(f"setelah agung dihapus, dict friends menjadi :\n {friends}\n\n")

"""
ternyata ikut kehapus juga, 
lalu bagaimana caranya biar ga ikut berubah juga?
make .copy

baca di 02 ya thx
"""