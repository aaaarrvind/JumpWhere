# First and last index in sorted array

def first_and_last(arr, target):
    # first=0
    if target not in arr:
        return [-1,-1]
    
    first , last = 1,1
    for i in range(len(arr)):
        if arr[i]==target:
            if first==-1:
                first=i
            last=i
            
    return [first,last]
    
