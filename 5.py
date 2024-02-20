from itertools import product
k=0
for p in product('МАТВЕЙ',repeat=6):
    a=''.join(p)
    g=set(a)
    for i in range (0, len(a)):
        if a[0]!='Й' and g.count==6 and a[i]=='А' and a[i+1]!='Е':
            k+=1
print(k)

    
