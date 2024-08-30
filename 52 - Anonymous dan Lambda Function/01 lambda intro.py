"""
keh lanjut lagi
kali ini kita belajar lambda, 
mirip def tapi lebih singkat

gampang def sih nangkepnya 
tapi kalo dah biasa, aman kok pastinya
"""

# misal fungsi kuadrat make def
def kuadrat_def(angka):
    print(f"{angka} jika dikuadratkan maka menjadi : {angka**2}")

kuadrat_def(2)

"""
kalo make lambda cukup sebaris aja
rumusnya :

lambda_name = lambda argument:lambda body
"""
kuadrat_lam = lambda angka:angka**2
# tinggal panggil deh 

print(f"{kuadrat_lam(5)}") # angka yg di kuadratkan yg di dalem kurung
print(f"hasil lambda kuadrat = {kuadrat_lam(4)}") # angka yg di kuadratkan yg di dalem kurung

