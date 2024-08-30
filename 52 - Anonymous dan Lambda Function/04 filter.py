angka = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]

# buat make def atau fungsi 
def kurang_dr_lm(angka):
    return angka < 5

data_list = list(filter(kurang_dr_lm,angka))
print(data_list)
# make def aja masih bingung karena belum biasa filter dari list

"""sekarang kita buat filter data kurang dari 6"""
# buat make lambda
# variable = list(filter(lambda (argument:body of argument)))
data_lam = list(filter(lambda nilai:nilai<6, angka)) # nama argument bisa yg lain ga harus nilai, dan buat bedain disini kita make <6
print(data_lam)


"""sekarang kita buat filter data angka genap"""
# variable = list(filter(lambda (argument:body of argument)))
data_genap = list(filter(lambda genap:(genap%2==0), angka)) # angka yg dibagi 2 hasilnya 0
print(data_genap)

"""sekarang kita buat filter data angka ganjil"""
# variable = list(filter(lambda (argument:body of argument)))
data_ganjil = list(filter(lambda g:(g%2!=0), angka)) # angka yg dibagi 2 hasilnya tidak 0
print(data_ganjil)

"""sekarang kita buat filter data angka kelipatan 3"""
# variable = list(filter(lambda (argument:body of argument)))
klptn_3 = list(filter(lambda g:(g % 3 == 0), angka))
print(klptn_3)


