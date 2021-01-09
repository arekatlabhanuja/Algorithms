#Computing the last digit of the fibonacci no
def large_fib(n):
    if(n<=1):
        return n
    prev=0
    curr=1
    for _ in range(n-1):
        prev,curr=curr,prev+curr
    curr=curr%10
    curr1=curr
    return curr1

n1=int(input())
print(large_fib(n1))