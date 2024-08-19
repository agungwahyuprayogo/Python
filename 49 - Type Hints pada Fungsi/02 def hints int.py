
# nah kalo mau buat hints tipe data kek gini
def kuadrat(angka:int):
    hasil = angka**2
    return hasil

a = kuadrat(2) # coba deh kursor nya diarahin ke tulisan kuadrat di kiri, nanti muncul tipe data apa yang bisa dimasukin, int 
print(a)



def kubik(angka:int) -> int:
    hasil = angka**3
    return hasil

b = kubik(3)
print(b)

"""
nah 2 itu kan harusnya make int kan
tapi anehnya tuh kalo python kita masukinnya string kaga merah njir syntaxnya alwkaok
tapi kalo kita run error

misal ya kubik kita masukin string
"""

c = kubik("agung") # tuh kan coba, padahal kita masukinnya string, tapi ga merah tulisanya
# pas dijalanin error sat wkwk

"""
yoweslah intinya hints itu buat ngasih tau kalo tipe data yang dimasukin itu,... nyesuain apa yg kita atur
jadi kedepan juga kalo liat def python yg ada :int) -> int: gausah bingung lagi yak
itu cuman sebagai hint aja kalo kursor kita arahin ke def
"""