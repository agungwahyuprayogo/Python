# jadi biasanya kita kan kalo mau buat string biasa make ".."
# kita juga bisa make single quote

from tokenize import single_quoted


singleQuote = 'ini single Quote'
doubleQuote = "ini double Qoute"

print(f"{singleQuote} {type(single_quoted)} \n{doubleQuote} {type(doubleQuote)} ")

# ga ada bedanya kan? antara single quote dan double quote? harusnya ga

# anehnya pas coba ditampilin tipe data dari single quote dan double quote malah beda
# yang single quote malah class 'set', yang double quote malah class 'str'
# harusnya tuh 22nya class 'str'