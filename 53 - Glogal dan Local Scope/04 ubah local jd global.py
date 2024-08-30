"""
nah kalo sebelumnya kita bisa akalin naro 
variable global sebelum function dipanggil

kali ini kita bisa ubah yang harusnya ga bisa di taro di dalem function jadi bisa lagi
misal kita punya variable nama dan angka
"""

nama = "Agoenk"
angka = 24

def ubah(nilai_baru):
    angka = nilai_baru # disini kita ngidenya pengen copy data 24 di angka ke nilai_baru trus di print
                        # masalahnya kalo di run error

print(f"sebelum diubah {angka}")
ubah(10)
print(f"sesudah diubah {angka}") # disini kita ngarepnya angka berubah jadi 10
# tapi ga berubah karena angka didalem function ubah itu variable lokal
# trus gimana biar bisa berubah
# kita buat def baru ya

def angka_berubah(nilai_baruu_bre):
    global angka # kita buat global gini dulu, baru enter, kalo ga error
    angka = nilai_baruu_bre
print("\n\nsetelah make global")
print(f"sebelum diubah {angka}")
angka_berubah(10)
print(f"sesudah diubah {angka}") # disini kita ngarepnya angka berubah jadi 10

def nama_berubah(nama_baru_bre):
    global nama
    nama = nama_baru_bre

print(f"\n\nnama sebelum berubah {nama}")
nama_berubah("Wahyuni")
print(f"nama setelah berubah {nama}")
