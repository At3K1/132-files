Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> p = int(input("vvedite p (2<p<=10):"))
x,y = int(1),int(1)

for x in range (1,p):
   a=[]
   for y in range (1,p):
      z = (x*y//p)*10 + (x*y)% p
      a.append(z)
   print(a)
