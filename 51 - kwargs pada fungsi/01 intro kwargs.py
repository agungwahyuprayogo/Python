"""
kali ini kita mau belajar kwargs
mirip args di materi sebelumnya hanya saja, di kwargs ini make 'key words'
makanya namanya kwargs, kw nya itu key word

kita langsung buat 3 perbandingan deh ya,
yg satu fungsi biasa, yg satu fungsi make args, yg satu fungsi make kwargs
"""

# def biasa
def fungsi_biasa(nama, umur, kelamin):
    print(f"halo nama saya {nama}, umur saya {umur} tahun, dan jenis kelamin saya {kelamin}")

fungsi_biasa("Agung", 24, "laki-laki")

# def args
def fungsi_args(*args): # bintangnya satu aja, tuple
    nama = args[0]
    umur = args[1]
    kelamin = args[2]
    print(f"halo, nama aku {nama}, umur aku teh {umur} yak, dan kelamin saya {kelamin}")

fungsi_args("Agoenk", 25, "laki - laki")

# def kwargs
def fungsi_kwargs(**kwargs): # bintangnya 2, dictionary
    jeneng = kwargs["nama"]
    umure = kwargs["umur"]
    kelamine = kwargs["kelamin"]
    print(f"halo jenengku {jeneng}, umurku saiki {umure} taun, karo kelamin ku saiki {kelamine}")

# nah bedanya di kwargs itu, kita perlu naro 'key'
fungsi_kwargs(nama = "agung", umur = 26, kelamin = "Lanang")