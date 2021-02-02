for _ in range(int(input())):
    num =int(input())
    q = num//6
    if q%2 == 0:
        if num%6 ==0:
            ans = (str(num-11)+' ' +"WS")
        elif num%6 ==1:
            ans = (str(num+11)+' ' +"WS")
        elif num%6 ==2:
            ans = (str(num+9)+' ' +"MS")
        elif num%6 ==3:
            ans = (str(num+7)+' ' +"AS")
        elif num%6 ==4:
            ans = (str(num+5)+' ' +"AS")
        elif num%6 ==5:
            ans = (str(num+3)+' ' +"MS")
    if q%2!=0:
        if num%6==0:
            ans = (str(num+1)+' '+ 'WS')
        elif num%6==1:
            ans = (str(num-1)+' '+ 'WS')
        elif num%6==2:
            ans = (str(num-3)+' '+ 'MS')
        elif num%6==3:
            ans = (str(num-5)+' '+ 'AS')
        elif num%6==4:
            ans = (str(num-7)+' '+ 'AS')
        elif num%6==5:
            ans = (str(num-9)+' '+ 'MS')
    print(ans)

