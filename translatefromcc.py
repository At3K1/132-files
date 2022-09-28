Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> print("p=")
a = int(input())
print("Np=")
b = int(input())
c = 1
d = 0
while b>0:
   d = d +(b%10)*c
   c = c*a
   b = b//10
print("N10=",d)