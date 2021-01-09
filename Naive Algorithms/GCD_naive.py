def gcd(a,b):
    max=1
    for i in range(2,min(a,b)+1):
        if a%i==0 and b%i==0:
            if i>max:
                  max=i
    return max


c,d=map(int,input().split())
print(gcd(c,d))
