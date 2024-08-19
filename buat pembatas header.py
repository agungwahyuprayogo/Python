"""
sama kek di word, ada rata kiri, rata kanan, rata tengah
 rjust ljust sama center gitu juga
"""

rt_tgh = "tengah".center(20) # jumlah karakter
# jadi rt_tgh punya variale string "tengah"
# dikasih syntax .center(20)
# maksdunya masukin variable "tengah" dintara 20 karakter (lainya spasi)
print(f"'{rt_tgh}'") 

rt_tgh1 = "tengah".center(10) # jumlah karakter
print(f"'{rt_tgh1}'") 
# mirip2 diatas, tapi kali ini masukin value dari variable diantara 10 karakter ke tengah2

# biar keliatan keren, bisa di tambah parameter

rt_tgh3 = "tengah".center(20,"-") # jumlah karakter
print(f"'{rt_tgh3}'") 
# sekarang dikasih 20 karakter, tapi diperjelas make strip (-)
# disini keliatan kalo jumlah - ada 14 (7 kanan 7 kiri)
# huruf tengah ada 6 karakter, 
# jadi pas ada 20 karakter, dimana sisi yg lain -
# dan python buat itu otomatis, kita cukup masukin perintah doang

rt_tgh4 = "tengah".center(20,">") # jumlah karakter, ">" karakter selain spasi
print(f"'{rt_tgh4}'") 

masbutteng = input("Masukan kata untuk berada di tengah2 : ")
print(f"{masbutteng.center(20,"-")}")