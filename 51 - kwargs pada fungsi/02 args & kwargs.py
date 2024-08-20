"""
nah dah tau kan cara kerja args dan kwargs
kali ini kita bakal kombinasiin args dan kwarg
untuk contoh kita saat ini sementara masih itung2an 

misal ni ya kita buat def yg bisa milih operasinya itu pernjumlahan atau perkalian
"""

def math(*args, **kwargs):
    output = 0
    if kwargs["option"] == "penjumlahan":
        for angka in args:
            output += angka
    elif kwargs["option"] == "perkalian":
        output = 1 # diubah jadi 1 karena kalo 0, hasil perkalian 0 terus
        for angka in args:
            output *= angka
    else:
        print("tidak ada operasi")

    return output

a = math(1,2,3,4,5, option = "penjumlahan")
print(a) # hasilnya 15, (1)+(2)=3+(3)=6+(4)=10+(5)

b = math(1,2,3,4,5, option = "perkalian")
print(b) # hasilnya 15, output = 1x(1)=1x(2)=2x(3)=6x(4)=24x(5)=120
