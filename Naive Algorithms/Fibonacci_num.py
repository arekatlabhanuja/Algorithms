def Fibonacci(n):
    if n<=1: 
        return n
    prev=0
    curr=1
    for i in range(n-1):
        prev,curr=curr,prev+curr
    return curr

    
if __name__=='__main__':
    n1=int(input());
    print(Fibonacci(n1))
