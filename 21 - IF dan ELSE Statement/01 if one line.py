# if and else statement

# jadi sebelumnya kita cuman belajar program yang alurnya tuh satu atau sekali doang
# input > program > selesai/stop
# program diatas cuman linear atau satu alur doang

"""
sedangkan kalo make if statement, bisa jalanin lebih dari 1 program dalam satu file
misal, misal ada input nama agung
trus ada cabang (if)
kalo misal "apkah bener namanya agung?" ternyata bener (True), programnya bakal ngapain
kalo misalkan salah (False), programnya berhenti
"""

"""
if nya kondisi :
aksi
"""

print("If One Line".center(20,"-"))

nama = input("siapa nama anda ? : ")
# if nya
# kondisi nya :
# aksi nya 
if nama == "agung": print(f"kyaa {nama} kunn >>>//<<<")
print(f"terima kasih {nama} sudah menggunakan layanan kami")

"""
jadi kalo pas input nama masukin nama 'agung'
hasilnya ada "kyaa agung kun" gitu gitu
tapi kalo bukan agung langsung ke terima kasih 
"""

kerja = input("Dimana anda berkerja? ")

if kerja == "khong guan":
    print("uwaa.. betah yaa kerja di Khong Guan :)")

print("Terimakasih atas waktunya, anda bisa log out sekarang")