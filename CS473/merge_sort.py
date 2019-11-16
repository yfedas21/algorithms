# A program that takes an unsorted array 
# and sorts it using merge sort
# 
# Engineer: Yuriy Fedas
#
# Organization: Self
#
# Technique: divide and conquer

# the crux of the program; 
# @input list (array) to sort
def merge_sort(A):
    # when/if |A| = 2
    if len(A) <= 2:
        # check whether the two elements are ordered
        if A[0] <= A[1]:
            pass
        else:
            temp = A[0]
            A[0] = A[1]
            A[1] = temp
    else:
        # get midway point for array
        ln = len(A) // 2
        # initialize B, C with first half, second half of A
        B, C = A[:ln], A[ln:]
        # recursive calls on each half, the quarter, etc
        merge_sort(B)
        merge_sort(C)
        
        # counter variables for index positions
        # of B, C and A
        i, j, k = 0, 0, 0

        # check the current position of comparison
        while i < len(B) and j < len(C):
            if B[i] <= C[j]:
                A[k] = B[i];
                i += 1
            else:
                A[k] = C[j];
                j += 1
            k += 1
        # case when all elements in B are merged into A
        if i == len(B):
            A[k:] = C[j:]
        else:
            A[k:] = B[i:]
    # output the array at each step 
    print("The sorted list is: ", A)

def main():
    # sample input provided on sheet
    merge_sort([3, 1, 7, 5, 4, 2, 8, 6, 11, 10, 12, 14, 16, 15, 13, 9])
    merge_sort([3, 5, 7, 9, 8, 6, 4, 2])

# points to main() as the driver
if __name__ == "__main__":
    main()