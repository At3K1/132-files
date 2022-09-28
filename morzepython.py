Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a = "abwgdevijklmnoprstufhcqx"
abc = list(a)
print(abc)
b = ".- -... .-- --. -.. . ...- --.. .. .--- -.- .-.. -- -. --- .--. .-. ... - ..- ..-. .... -.-. --.- -..-"
abcm=b.split()
print(abcm)
abcm=b.split()
text=input("Введите текст на английском: ")
indm=""
for i in range (len(text)):
    ind = abc.index(text[i])
    indm=indm + abcm[ind] 
print(f"{indm}")
