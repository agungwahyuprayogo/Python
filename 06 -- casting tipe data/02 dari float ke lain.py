print("=====FLOAT=====")

float = 0.0
print(float, type(float))

print("")
intrgr = int(float)
string = str(float)
boolean = bool(float)

print(f"dari float {float} dengan tipe data ", type(float),"\n") 
print(f"ke int menjadi {intrgr}", type(intrgr)) # type buat ngecek tipe data di intergr apa
print(f"ke string menjadi {string}", type(string)) # type buat ngecek tipe data di string apa
print(f"ke boolean menjadi {boolean}", type(boolean)) # type buat ngecek tipe data di boolean apa

"""
kalo ke int jadi dibulat ke bawah angka nya ketika di casting
kalo ke string jadi sama, bedanya 9.9 string
kalo ke boolean, diluar angka 0.0 True 
"""
print("====FLOAT====")
flt = 1.9
print("flt memiliki nilai",flt,"dengan tipe data",type(flt)) # type buat ngecek tipe data di flt apa

itg = int(flt)
string = str(flt)
boolean = bool(flt)

print("itg memiliki nilai",itg,"dengan tipe data",type(itg)) # type buat ngecek tipe data di itg apa
print("string memiliki nilai",string,"dengan tipe data",type(string))
print("boolean memiliki nilai",boolean,"dengan tipe data",type(boolean))