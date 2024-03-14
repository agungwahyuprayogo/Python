print("===Input Data User====")
print("========String========")

nadep = input("masukan nama depan anda : ")
nateng = input("masukan nama tengah anda : ")
nabek = input("masukan nama belakang anda : ")

print(f"nama lengkap anda adalah {nadep} {nateng} {nabek}")

"""
input default dari python adalah string
jadi mau kita masukin angka, boolean, type datanya tetep string
"""


print("\n\n\nMahasiswa baru")

nama = input("Masukan Nama Anda : ")
nik = input("Masukan Nomer NIK Anda : ")
alamat = input("Masukan Alamat Anda (Jalan & kota) : ")

print(f"Mohon cek kembali data berikut : \nNama anda adalah '{nama}' \nNIK anda adalah '{nik}'\nalamat anda adalah '{alamat}'\napakah sudah benar?")