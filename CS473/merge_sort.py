# merge_sort algorithm, implementation based 
# off of psuedocode in Levitin, 3rd Edition
#
# Engineer: Yuriy Fedas
# 
# Organization: Whitworth University
#
# Purpose: To sort an array in theta(n logn) 
#          instead of theta(n^2)
# 
# Technique: Divide and Conquer

def merge_sort(A): 
    # stores the length of the input array
    # for easy reuse (assumes len(A) is power of 2)
    ########## fix later for any size A ###########
    ln = len(A) // 2
    
    # 2 sub arrays to hold halves of A
    B,C = [], []

    # check if len(A) is greater than 2
    if len(A) > 2: 
        # copy first half of A into B
        # and second half into C
        for i in range(ln):
            B.append(A[i])
            C.append(A[i + ln])

        # call mergesort recursively
        while len(B) > 1:
            sub_B = merge_sort(B)
        while len(C) > 1: 
            sub_C = merge_sort(C)

    # len(A) is < 2
    else: 
        # swap the elements
        if A[0] > A[1]: 
            temp = A[0]; A[0] = A[1]; A[1] = temp
        # already in order
        return A
    
    merge(B, C, A)

# merge two already sorted sub-arrays
def merge(B, C, A): 
    print("DEBUG: merge() reachable")
    i, j, k = (0 for _ in range(3))
    while i < len(B) and j < len(C):
        if B[i] <= C[j]:
            A[k] = B[i]; i+=1
        else: 
            A[k] = C[j]; j+=1
        k+=1
    if i == len(B):
        # copy C[j..q −1]to A[k..p+q −1]
        pass
    else: 
        # copy B[i..p−1]to A[k..p+q −1]
        pass

# driver for the program
def main(): 
    in_1 = [3, 5, 7, 9, 8, 6, 4, 2]
    in_2 = [3, 1, 7, 5, 4, 2, 8, 6, 11, 10, 12, 14, 16, 15, 13, 9]

    # sample
    #merge_sort(in_1)
    #merge_sort(in_2)
    merge(3, 2, 1)

# code driver, tells the interpreter
# starting point for execution
if __name__ == "__main__": 
    main()