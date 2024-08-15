def penyambutan(orang_orang):
    data_orang = orang_orang.copy()
    for orang in data_orang:
        print(f"selamat datang {orang} di Indonesia")

# kita buat deh contohnya boyband twice
twice = ["sana minatozaki", "tzuyu", "jihyo"]

# trus kita panggil deh fungsinya
penyambutan(twice)

"""
alurnya tuh pertama kita kan manggil def
di dalam def ada variable list (twice = sana ...)

nah si twice ini masuk ke argument atau input orang_orang
dari orang_orang di copy ke data_orang
kenapa make .copy()
biar kalo twice dirubah, di def penyambutan ga berubah

nah terus di looping di for
gitu
"""