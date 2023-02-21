def f17():
   with open('17.txt') as f:
    nums=[int(x) for x in f]
    c=list(map(abs,nums))
    a=[]
    for i in range(len(c)-1):
        if c[i]%10==3:
            a.append(c[i])
    m=max(a)
    count=0
    summ=[]
    #for i in range(len(nums)-1):
       #if((nums[i]%10==3 and nums[i+1]%10!=3) or (nums[i]%10!=3 and nums[i+1]%10==3)):
    for i in range(len(c)-1):
        if((c[i]%10==3 and c[i+1]%10!=3) or (c[i]%10!=3 and c[i+1]%10==3)):
            if nums[i]**2+nums[i+1]**2>=m**2:
                count+=1
                summ.append(nums[i]**2+nums[i+1]**2)
    print(count)
    print(max(summ))
