"""
didalam looping atau perulangan ada 3 kompenen yang biasa digunakan :
continue, pass, dan break

kali ini kita bakal belajar pass dulu
sebenernya pass ini lebih ke dummy sih, 
maksudnya tuh programnya ada tapi ga ngejalanin apa2

pass -> dummy, tidak akan dieksekusi

biar gampang nangkepnya, kita buat contoh satu dulu variable angka_1
"""

angka_1 = 1 # misal disini kita ada variable yang punya nilai value tuh 1

while angka_1 < 5: # lalu di dalam while kita buat syarat kalo angka kurang dari 5 maka ...
    angka_1 += 1 # angka_1 ditambah 1

    print(f"sekarang angka ke {angka_1}") 

    if angka_1 == 4: # kalo setiap looping dah sampe angka 4
        print(f"weh dah {angka_1} aje nih ^^") # maka ada tulisan kek disamping

print("Program 1 selesai\n")

"""
nah contoh diatas buat ngasih liat dibagian if kalo = 4
lalu bagaimana caranya ngasih liat fungsi pass
"""
angka_2 = 1 # misal disini kita ada variable yang punya nilai value tuh 1 lagi

while angka_2 < 5: # lalu di dalam while kita buat syarat kalo angka kurang dari 5 maka ...
    angka_2 += 1 # angka_2 ditambah 1

    print(f"sekarang angka ke {angka_2}") 

    if angka_2 == 4: # kalo setiap looping dah sampe angka 4
        pass # nah disini keliatan bedanya, 
    # kalo di program 1 kan keliatan tuh kalo dah sampe 4 ngapain
    # nah disini (pass) ga bakal eksekusi apa2, jadi ya dilewatin aja udeh
    # bahkan ketika di print beda kek program satu kalo sampe 4 bakal ngapain, yg pass ga ada apa2

print("Program 2 selesai\n")

"""
soal pass nanti digunainya banget pas kapan nanti pas udah belajar def atau fungsi
ini hanya perkenalan aja
"""