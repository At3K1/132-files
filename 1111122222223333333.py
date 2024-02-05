v=0
for n in range(1, 10000000):
    s=bin(n)[2:]
    k=str(n)
    c=0
    m=0
    for x in k:
        if int(x)%2==0:
            c+=1
    else:
        m+=1
    if c>m:
        s+=1
    if m>c:
        s+=1
    if ((c==m) and (n%2==0)):
        s+=0
    else:
        s+=1
    i=int(s, 2)
    h=bin(i)[2:]
    t=str(i)
    q=0
    w=0
    for p in t:
        if int(p)%2==0:
            q+=1
    else:
        w+=1
    if q>w:
        h+=1
    if w>q:
        h+=1
    if ((q==w) and (i%2==0)):
        h+=0
    else:
        h+=1
    z=int(h, 2)
    o=bin(z)[2:]
    l=str(z)
    d=0
    a=0
    for g in l:
        if int(g)%2==0:
            d+=1
    else:
        a+=1
    if d>a:
        o+=1
    if a>d:
        o+=1
    if ((d==a) and (z%2==0)):
        o+=0
    else:
        o+=1
    b=int(o, 2)
    if (b>876544) and (b<1234567899):
        v+=1
    print(v)
    
    
