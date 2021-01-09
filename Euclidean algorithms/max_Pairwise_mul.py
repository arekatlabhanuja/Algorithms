def max_pairwise_mul(n,arr):
    a=arr[0]
    b=arr[1]
    if(n>2):
        for i in range(0,n):
            for j in range(i+1,n):
                if(arr[i]*arr[j]>a*b):
                    a=arr[i]
                    b=arr[j]
                    c=a*b
    return c
                
            
        
    

if __name__=='__main__':
    c1=int(input())
    arr = list(map(int, input().split()))
    print(max_pairwise_mul(c1,arr))



       
        
        