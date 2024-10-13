# Write a code to remove duplicate element from array

n = int(input())
arr = []


arr = input().split(" ")
for i in range(n):
    arr[i] = int(arr[i])

print(arr)

def find_duplicates1(arr):
    duplicate = set()
    seen = set()
    
    for i in arr:
        if i in seen:
            duplicate.add(i)
        else:
            seen.add(i)

    return duplicate


dup = find_duplicates1(arr)
print(dup)