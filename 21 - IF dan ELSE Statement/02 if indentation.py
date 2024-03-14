"""
di if else python itu ada indentation
jadi maksud dari indentantion adalah 
ada jarak setelah if

 misal di sebelumnya kita masukin if langsung di sebelah printahnya
 if nama == "agung": print(f"kyaa {nama} kunn >>>//<<<")

 nah kalo indentation, abis titik 2 kita enter, nanti program rada maju
 misal 
 if nama == "agung": 
    print(f"kyaa {nama} kunn >>>//<<<")
    ^ jadi kaya ada semacam spasi, sebelum pri
"""

name = input("Masukan nama anda : ")

if name == "agung":
    # beda huruf gede kecil berpengaruh karena case sensitive
    print("Shhh dingin bangett!!") 
    print("ciee dah lulus skripsi awoakwaok") 
    # print disini masih masuk program if
    # indentasi, jadi kaya di tab sekali biar ga error
    # ^ jika kondisi tidak terpenuhi, 
    # langsung skip ke program selanjutnya (program di bawah)
print(f"Ok makasih {name} silahkan masuk")