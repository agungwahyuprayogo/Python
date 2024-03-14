"""
jadi kalo di percabangan sebelumnya kan kita udah belajar kalo if cuman 1
trus belajar kalo misalkan ada 2 percabangan make if dan else
tapi gmn kalo misakan percabanganya ada 3 atau lebih?
apakah make if if else else atau bagaimana?

oke jadi ada yang namanya elif
-> elif = else if

jadi misalkan kemarin contohnya masukin nama kampus
kalo ugm lanjut
kalo selain ugm ga bisa 
lalu stop

kalo make elif
kita buat kalo ugm lanjut
kalo bukan ugm disuruh nunggu tanggal sekian
selain kampus yang depanya "u" ga bisa lajut
baru yang terakhir ucapan terimakasih

jadi kurang lebih if elif tuh kek gini

if kondisi :
    program
elif kondisi :
    program
elif sekian ...
    program sekian ...
else :
    program
stop
"""
while True:
    
    kampus = input("dari kampus mane banh? : ")

    if kampus == "ugm":
        print("selamat datang anak UGM ^^ silahkan klik tautan berikut")
    elif kampus.startswith("u"):
        print("untuk kampus anda, tunggu informasi selanjutnya")
    elif kampus.startswith("i"):
        print("untuk kampus anda, tunggu lagi dalam seminggu")
    # kalo semua kondisi ga 

    print("program berakhir ")

    ulang = input("apakah anda ingin mengulang program ini? : (y/n)")

    if ulang != 'y':
        break