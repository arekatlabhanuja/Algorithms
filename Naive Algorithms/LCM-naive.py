def LCM (a,b):

    for i in range(1,a*b):
        if(i%a==0 and i%b==0):
            return i 
    
       
    

c,d=map(int,input().split())
print(LCM(c,d))
