def binarySearch(self,arr,key):
    lo=0
    hi=len(arr)-1
    mid=0
    index = -1
    while lo<=hi:
        mid = (lo+hi)//2
        if arr[mid] == key:
            index = mid
            return index
        elif key<arr[mid]:
            hi = mid - 1
        elif key > arr[mid]:
            low = mid + 1
    
    return index