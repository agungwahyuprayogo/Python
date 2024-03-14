"""
hampir mirip if else sebelumnya
hanysa saja di bagian if bisa di tambah
else

kasusnya sama input nama kampus
"""

while True:
    
    kampus = input("dari kampus mane banh? : ")

    if kampus == "ugm":
        print("selamat datang anak UGM ^^ silahkan klik tautan berikut")
    elif kampus.startswith("u"):
        print("untuk kampus anda, tunggu informasi selanjutnya")
    elif kampus.startswith("i"):
        print("untuk kampus anda, tunggu lagi dalam seminggu")
    else:
        print("lah kampus mane itu? kluar anda!")
    # kalo semua kondisi ga 

    print("program berakhir ")

    ulang = input("apakah anda ingin mengulang program ini? : (y/n)")

    if ulang != 'y':
        break