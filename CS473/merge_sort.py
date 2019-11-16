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

# @input two array elements
# @return input in nondecreasing order
def swap(a, b):
    if (a <= b): 
        return([a, b])
    else: 
        return([b, a])

# merge two already sorted sub-arrays
# @input sorted sub-arrays to merge
# @return the merged sorted array 
#         of length |A| = |B| + |C| 
def merge(B, C, A): 
    print("DEBUG: merge() reachable")
    # initialize i, j, k to 0
    i, j, k = (0 for _ in range(3))

    # conditional while for merging
    while i < len(B) and j < len(C):
        # check if the value in B is 
        # less than the current value in C;
        # if so, copy to same location in A
        if B[i] <= C[j]:
            print("merging ",str(A[k])," and ",str(B[i]),"...")
            A[k] = B[i]; i+=1
            print("A is now: ",A,"\n\n")
        else: 
            print("merging ",str(A[k])," and ",str(C[j]),"...")
            A[k] = C[j]; j+=1
            print("A is now: ",A,"\n\n")
        # increment the index for A[]
        k+=1
    # all elements in list B merged into A, 
    # copy the rest of sorted list C into A
    if i == len(B):
        # copy C[j..q −1]to A[k..p+q −1]
        A[k:] = C[j:]
    else: 
        # copy B[i..p−1]to A[k..p+q −1]
        A[k:] = B[i:]

    print("The final ordering of A is ", A)

# the crux of the program
# @input the array to sort
# @return the sorted array
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
        B = A[:ln]
        C = A[ln:]

        print("B is ", B, ", C is ", C)

        # call mergesort recursively
        while len(B) > 1:
            merge_sort(B)
            merge(B, C, A)
        while len(C) > 1: 
            merge_sort(C)
            merge(B, C, A)

    # len(A) = 2
    else: 
        # swap the elements
        print("swap : ",swap(A[0],A[1]))
        #return(swap(A[0],A[1]))
        

# driver for the program
def main(): 
    in_1 = [3, 5, 7, 9, 8, 6, 4, 2]
    in_test = [3, 7, 9, 5, 8, 6, 4, 2]
    in_2 = [3, 1, 7, 5, 4, 2, 8, 6, 11, 10, 12, 14, 16, 15, 13, 9]

    # sample
    merge_sort(in_test)
    #merge_sort(in_2)
    #merge([1,3,4,9],[2,4,6,9],[0, 0, 0, 0,0,0,0,0])
    # D, E, F = [1, 2, 3, 4], [5, 6, 7, 8], [0, 0, 0, 0, 0, 0, 0, 0]
    # print("D: ",D)
    # print("E: ",E)
    # print("F: ",F)

    # F[:len(D)] = D[:]
    # F[len(E):] = E[:]

    # print("F: ",F)
# code driver, tells the interpreter
# starting point for execution
if __name__ == "__main__": 
    main()