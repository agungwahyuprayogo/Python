"""
oke kali ini kita bakal belajar mengenai hints pada def
jadi kalo biasanya kita buat def kan gini doang :

def fungsi(argument):

nah sebenernya kalo di bahasa pemograman lain tuh, 
udah di tentuin di awal, def / fungsi ini mau make tipe data apa gitu
misal int ya int, ga bisa di masukin string gitu

begitu juga kalo kita atur suatu fungsi make string, 
ya cuman bisa make string, error kalo kita masukin interger

nah disini kita bakal belajar buat hint dalam def, 
biar nanti tuh ngasih tau di awal kalo tipe data yg bisa dipake cuman tertentu doang
"""

def biasanya(gini):
    print("oh gini too")

biasanya("agung") # coba arahain kursor ke tulisan 'biasanya' di kiri, tulisanya :Any kan? berarti itu bisa dimasukin apapun, ntah itu string, int
