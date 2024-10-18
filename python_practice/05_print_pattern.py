n = int(input())

def print_pattern_1(k):
    for i in range(k):
        for j in range(i+1):
            print("*", end = " ")
        print()
    return


def print_pattern_2(k):
    for i in range(k):
        for j in range(k-i):
            print("*", end = " ")
        print()

def print_pattern_3(k):
    for i in range(k):
        for j in range(k):
            # print("*",end = " ")
            if(i>j):
                print(" ", end = " ")
            else:
                print("*", end = " ")
        print()
    return

def print_pattern_4(k):
    for i in range(k):
        for j in range(k):
            # print("*",end = " ")
            if(i+j>=k-1):
                print("*", end = " ")
            else:
                print(" ", end = " ")
        print()
    return



print_pattern_1(n)
print()
print_pattern_2(n)
print()
print_pattern_3(n)
print()
print_pattern_4(n)