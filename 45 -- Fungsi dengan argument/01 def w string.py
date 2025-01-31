# misal kita buat fungsi yang nyebut nama sesuai yang kita input
def pakabs(nama):   # jadi yang di dalem kurung ini input / argument (tapi kebanyakan argument)
    print(f"hello whatsapp {nama}, gimana orang tua? sehat kan?")
    # nah argument ini semacam variable di dalam fungsi atau def

# misal deh
pakabs("agung")

"""
yang keluar setelah di run adalah "hello whatsapp agung, gimana orang tua? sehat kan?"
nah si "agung" ini masuk ke argument nama (yang dalem kurung dalam def / function) pakabs
nah ketika "agung" ini udah masuk ke argument pakabs
masuk lah "agung" ini ke body of function

function yang kita buat kan hello .. {nama} gimana ...
nah si "agung" ini masuk ke argument nama 
gituu
"""

def undangan(nama):
    print(f"haii {nama}.. makasih ya duah dateng ke nikahan kitaa..")

undangan("agoenk")

input_name = input("Masukan nama Anda : ")

def kondangan(input_name):
    print(f"Selamat Datang {input_name}. Anda masuk daftar List tamu VIP, silahkan belok kanan.")

kondangan(input_name)
