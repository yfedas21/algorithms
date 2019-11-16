def swap(_a, _b):
    if _a <= _b:
        return (_a, _b)
    else:
        return (_b, _a)


def merge(*args):
    print("DEBUG: merge() reachable")
    B, C, A = args[0], args[1], args[2]
    i, j, k = 0, 0, 0

    while i < len(B) and j < len(C):
        if B[i] <= C[j]:
            A[k] = B[i];
            i += 1
        else:
            A[k] = C[j];
            j += 1
        k += 1
    if i == len(B):
        A[k:] = C[j:]
    else:
        A[k:] = B[i:]

    #print("A is ", A)
    return(A)

def merge_sort(A):
    if len(A) <= 2:
        if A[0] <= A[1]:
            pass
        else:
            temp = A[0]
            A[0] = A[1]
            A[1] = temp
    else:
        ln = len(A) // 2
        B, C = A[:ln], A[ln:]
        merge_sort(B)
        merge_sort(C)

        #B, C, A = args[0], args[1], args[2]
        i, j, k = 0, 0, 0

        while i < len(B) and j < len(C):
            if B[i] <= C[j]:
                A[k] = B[i];
                i += 1
            else:
                A[k] = C[j];
                j += 1
            k += 1
        if i == len(B):
            A[k:] = C[j:]
        else:
            A[k:] = B[i:]

        # print("A is ", A)
    print("The sorted list is: ", A)

def main():
    # merge([5, 7, 9, 11], [2, 4, 5, 7], [0 for i in range(8)])
    merge_sort([3, 5, 7, 9, 8, 6, 4, 2])


if __name__ == "__main__":
    main()