#Computing the last digit in a faster way with less time
def large_fib(n):
    if(n<=1):
        return n
    prev=0
    curr=1
    for _ in range(n-1):
        prev,curr=curr%10,(prev+curr)%10
    return curr

n1=int(input())
print(large_fib(n1))