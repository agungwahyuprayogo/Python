# mengubah tipe data ke tipe data lain

print("====TIPE DATA INTEGER KE ..====")

data_int    = 0
print("angka INT :", data_int) 
print("")

data_float  = float(data_int)       
# maksud dari fload(name of variable) adalah buat ganti tipe data jadi float
print("diubah ke float menjadi : ", data_float, type(data_float))

data_str    = str(data_int)         # tetep jadi 9, tapi dalam bentuk text
print("diubah ke string menjadi : ", data_str, type(data_str))

data_bool   = bool(data_int)        # bernilai false kalo 0
print("diubah ke boolean menjadi : ", data_bool, type(data_bool))



print("")
print("====TIPE DATA FLOAT KE ..====")

data_float    = 9.9
print("angka FLOAT :", data_float) 
print("")

data_int    = int(data_float)       # angka dibuat jadi ga ada koma, dan dibulatkan kebawah
print("diubah ke int menjadi : ", data_int, type(data_float))

data_str    = str(data_float)       # tetep jadi 9, tapi dalam bentuk text
print("diubah ke string menjadi : ", data_str, type(data_str))

data_bool   = bool(data_float)      # bernilai true selain 0
print("diubah ke boolean menjadi : ", data_bool, type(data_bool))



print("")
print("====TIPE DATA STRING KE ..====")

data_str    = 69        # bakal error di int dan float kalo >> data berupa kata
                        # biar ga error masukin data angka
print(" STRING :", data_str) 
print("")

data_int        = int(data_str)       # bakal error kalo data str berupa text
print("diubah ke float menjadi : ", data_int, type(data_float))

data_float      = float(data_str)     # bakal error kalo data str berupa text
print("diubah ke string menjadi : ", data_float, type(data_str))

data_bool       = bool(data_str)      # bernilai false kalo 0
print("diubah ke boolean menjadi : ", data_bool, type(data_bool))



print("")
print("====TIPE DATA BOOLEAN KE ..====")

data_bool    = True         # kalo data True, output jadi 1
                            # kalo data False, output jadi 0
print(" BOOLEAN :", data_bool) 
print("")

data_int  = int(data_bool)       # angka dibuat jadi ga ada koma, dan dibulatkan kebawah
print("diubah ke int menjadi : ", data_int, type(data_int))

data_float    = float(data_bool)         # tetep jadi 9, tapi dalam bentuk text
print("diubah ke float menjadi : ", data_float, type(data_float))

data_str    = str(data_bool)       # bernilai false kalo 0
print("diubah ke str menjadi : ", data_str, type(data_str))