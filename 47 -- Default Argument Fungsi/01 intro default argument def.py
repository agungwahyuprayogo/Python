"""
keh, jadi kita kemarin udah belajar apa itu def,
lalu mengatur body of def gimana, cara manggilnya gmn
cara masukin value ke def gmn
nah sekarang kita bisa masukin default argument di dalam def

jadi kalo kemarin kan kita perlu input nih kalo ada variable di argument
sekarang kita bisa atur defaulnya gimana kalo ga di isi
"""

# misal, one default argument
def salam(nama = "kakakk"):
    print(f"haloo {nama}, selamat datang di kampus kamii")

# lalu kita coba dulu input nama sebagai agung
salam("agung") # nah kalo ini di run, hasilnya haloo 'agung' sesuai inputan argument

# trus gmn kalo default
salam() # ketika di run hasilnya, haloo 'kakakk' ... .., sesuai defult
