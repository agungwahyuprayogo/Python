"""
nah untuk mengindari keribetan itu, terciptalah *args
jadi args ini yang buat lebih singkat dalam memasukan input di argument

kita bisa buat list lagi tapi ga harus ribet kaya sebelumnya
"""

def tes(*coba):
    print(f"halo saya {coba} umur {coba}") # jadi nya jelek njir wkwk

tes("agung", 24) # ga jelas malahan, skip aja langsung ke bawah gausah peduliin yg syntax paling atas ini

def bio(*args): # nama ga harus args juga ya, bisa bebas, ini contoh aja
    nama = args[0]
    umur = args[1]
    kelamin = args[2]
    print(f"halo nama saya {nama}, umur saya {umur} tahun, dan kelamin saya {kelamin}")

# nah kalo udah buat kaya diatas, kita ga perlu buat list lagi make [] di argumentnya
bio("agung", 24, "laki - laki")

"""
atau kita buat looping, tapi di def cukup dikit aja 
misal hitung baris
"""

def sebut_nama(*nama): 
    for i in nama:
        print(f"hi saya {i}")

sebut_nama("agung", "sulastri", "sumingten", "gugung")

"""
atau kita pengen ngitung rata - rata nilai anak suatu kelas
pasti kan ada banyak ya anaknya, ga mungkin kita buat argument 10 lebih
nah kita bisa buat make args (tapi make nama nilai ya)
"""

def rata(*nilai):
    total_nilai = sum(nilai) # 90 + 100 + 40 + ...
    banyak_nilai = len(nilai) # banyaknya data, misal 10 buah atau 15 buah
    rata_rata = total_nilai / banyak_nilai
    print(f"jadi yg masuk nilanya tuh ada yang {nilai}, nah rata2nya adalah {rata_rata}")
    return rata_rata

rata(90,100,40,70,80,50,80,77,79)


"""
jadi ya intinya make args kalo datanya ada banyak, 
kalo ga terlalu banyak mah ga make args gpp

jadi kesimpulan lainya adalah kalo datanya banyak yg mau make def
disaranin buat ngolah atau di body of def-nya buat looping atau buat itung2an kaya diatas
soalnya kalo cuman data 1, 2, 3 bakal akward gitu,
bisa sih tapi kudu kaya gini dulu :

def fungsi(*args): 
    variable = args[0]
    another = args[1]
    value = args[2]

lalu yg lainya bisa make for atau itung2an kaya diatas
"""