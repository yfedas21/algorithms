# merge_sort algorithm

def merge_sort(A): 
    # stores the length of the input array
    # for easy reuse
    ln = len(A) // 2
    
    # 2 sub arrays to hold halves of A
    B = []; C = []

    # check if len(A) is greater than 2
    if len(A) > 2: 
        # copy first half of A into B
        # and second half into C
        for i in range(ln):
            B.append(A[i])
            C.append(A[i + ln])
    print("B is ", B)
    print("C is ", C)

def merge(A, B, C): 
    pass

# driver for the program
def main(): 
    in_1 = [3, 5, 7, 9, 8, 6, 4, 2]
    in_2 = [3, 1, 7, 5, 4, 2, 8, 6, 11, 10, 12, 14, 16, 15, 13, 9]

    # sample
    merge_sort(in_1)
    merge_sort(in_2)

# code driver, tells the interpreter
# starting point for execution
if __name__ == "__main__": 
    main()