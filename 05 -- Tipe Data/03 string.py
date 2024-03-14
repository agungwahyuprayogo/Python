"""
untuk kali ini tipe datanya adalah string
string itu sekumpulan karakter
"""

nama_depan = "Agung"
nama_tengah = "wahyu"
nama_belakang = "prayogo"

nama_lengkap = nama_depan+nama_tengah+nama_belakang
print(nama_lengkap)
print(f"{nama_depan} \n{nama_tengah} \n{nama_belakang}",type(nama_lengkap))

"""
selama value dikasih tanda petik
tipe datanya akan dibaca jadi string
"""
sepuluh = "10"
seratus = "100"

print(f"sepuluh nilanya {sepuluh}", type(sepuluh))
print(f"seratus nilanya {seratus}", type(seratus))

kelompok_1 = """Kelompok 1 : 
1. Agung Wahyu Prayogo 
2. Valent Aderiandra 
3. Fauziya Alya Ramadhana 
4. Putri Windasari 
5. Reno Darin Khalifah Panarung"""

print(kelompok_1)

# entah gimana ceritanya itu gw string bisa lebih dari satu baris tau darimana
# kemungkinan sih dari video kelas terbuka yang laen terus gw praktekin disini juga

data_str = "halo apa kabar"
print("kalimat pada variable data_str adalah", data_str)