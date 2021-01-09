def merging_sort(nlist):
    if len(nlist)>1:
        mid=len(nlist)//2
        lefthalf=nlist[:mid]
        righthalf=nlist[mid:]

        merging_sort(lefthalf)
        merging_sort(righthalf)
        i=j=k=0
        while i<len(lefthalf) and j<len(lefthalf):
            if lefthalf[i] < righthalf[j]:
                nlist[k]=lefthalf[i]
                i=i+1
            else:
                nlist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            nlist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            nlist[k]=righthalf[j]
            j=j+1
            k=k+1
    return nlist
        
    
    

arr=list(map(int,input().split()))
print(merging_sort(arr))