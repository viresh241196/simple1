arr=[-1,-2,0,1,2]
found=0
for i in range(3):
    a=arr[i]
    print(a)
    for j in range(i+1,4):
        b=arr[j]
        print(b)
        for k in range(j+1,5):
            c=arr[k]
            print(c)
            
            result=a+b+c
            if result==0:
                print(a,b,c)
                