def remove_dupli(arr):
    if not arr:
        return 0
    
    i=0

    for j in range(1,len(arr)):
        if arr[j]!=arr[i]:
            i+=1
            arr[i]=arr[j]
    return i+1

dupli=[5,8,9,8,7,5,6,4]
dupli.sort()
print(remove_dupli(dupli))