# Kth largest element
# import heapq
def k_largest_element(arr,k):
    if len(arr)<k:
        return -1
    sorted_arr= sorted(arr)
    i =len(arr)-k
    return sorted_arr[i]

#   return heapq.nlargest(n,arr)[-1] #alternate solution
