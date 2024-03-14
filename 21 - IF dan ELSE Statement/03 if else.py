# IF Else

"""
jadi kalo sebelumnya belajar if cuman kalo kondisi terpenuhi
 langsung ke program terakhir
disini kita latihan if else
if else itu jika 1 kondisi tidak terpenuhi, bakal melakukan apa 

misal ada input nama kampus
yg true itu ugm misalnya, nanti kalo true jadi "selamat datang"
kalo salah misal jadi "maaf hanya mahasiswa ugm yang bisa menggunakan ini"
trus baru ke program terakhir "terimakasih telah menggunakan layanan ini"
"""
print("If Else".center(20,"-"))

kampus = input("Dari kampus mane banh? : ")

if kampus=="ugm":
    print("Selamat datang mahasiswa UGM ^^ Silahkan untuk klik link berikut")
    # kalo pas input masukin "ugm", bakal nampilin tulisan diatas^
else:
    # tapi kalo yang dimasukin selain ugm, mau ubj mau apakek
    print("Maaf banh, yang bisa akses layanan ini cuman mahasiswa UGM")
    # yang di print tulisan ini ^

print("Terima kasih sudah mengunjungi xxx ")
# akhir program

kantor = input("Dimana tempat anda berkerja? ")

if kantor == "Khong Guan Group":
    print("Semoga betah kerja disini yaa :)")
    print("Semoga rezeki perusahaan Khong Guan dan anak perusahaannya naik terus")
else:
    print("maaf layanan mudik gratis ini hanya untuk karyawan Khong Guan Group")
print("Terimakasih sudah menggunakan layanan ini")

