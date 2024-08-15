"""
terus lah berkembang untuk menjadi kepribadian yang lebih baik
nah kita sampe ke def return. maksudnya gmn tuh?

jadi mirip di matematika yang ada 
y = f(x)
nah si return ini mirip si ya

kalo kemarin kan kita belajar cuman sampe f(x) doang nih
f tuh kaya nama fungsi nya
trus x tuh kaya argumentnya

    f       (x)
penjumlahan (1,2)

nah si y ini return 
misal

def penjumlahan(angka1, angka2)     = sama kaya f(x)
    badan fungsi
    return output                   = sama kaya y

wkwkwk bingung gw jelasinnya kalo by text
liat ini dulu deh    
https://www.youtube.com/watch?v=ADcQu-8R0Ok

mending langsung ke contoh aja kita
"""


# kuadrat coba sebagai contoh
def kuadrat(angka):
    hasil_kuadrat = angka**2
    return hasil_kuadrat

# nah si ye ini gini doang
y = kuadrat(5)  # ga harus y juga ya, bisa bebas
print(y)
# beda nya disitu doang

# coba kita buat lagi tapi ga make return, apakah error kalo kita pake z
def kubik(number):
    hasil_kubik = number**3
    # kalo ga make return, hasil nya none

z = kubik(5)
print(z)
# hasilnya none kalo kita manggil kubik tanpa return terus dimasukin ke z

