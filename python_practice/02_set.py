
## curly brackets create a set
fruits = {"a","b","a"}
print(fruits)

## round brackets create tuple
a = [1,2,3,4,5,5]
a.reverse()
print(a)
set_a = set(a)
print(set_a)

fruits = {"apple", "banana", "cherry"}

print("banana" in fruits)  # Output: True
print("date" in fruits) 

set1 = {1, 2, 3}
set2 = {3, 4, 5}

union_set = set1 | set2
union_set_1 = set1.union(set2)
print(union_set)
print(union_set_1)

intersection_set = set1 & set2
intersection_set_1 = set1.intersection(set2)
print(intersection_set)
print(intersection_set_1)

diff_set = set1-set2
diff_set_1 = set1.difference(set2)
print(diff_set)
print(diff_set_1)

set1 = {1, 2, 3}
set2 = {3, 4, 5}

sym_diff_set = set1 ^ set2
print(sym_diff_set)  # Output: {1, 2, 4, 5}

# Using .symmetric_difference()

sym_diff_set = set1^set2
sym_diff_set1 = set1.symmetric_difference(set2)
print(sym_diff_set)  # Output: {1, 2, 4, 5}














