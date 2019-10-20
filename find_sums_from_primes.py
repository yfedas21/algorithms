# Make a list of consecutive primes (exclude 2 because
# and even + an odd # is odd and our inputs are even)
primes = [3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 
        43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

# function that will find the sum
# @list: the list of primes
# @num: the sum we're looking for
def find_sum(num_to_find):
    # variable to keep track of whether the input was found
    found = False

    # variable to keep track of the length of primes[]
    sz = len(primes) - 1

    # establish lower and upper indices to move
    # independent of each other
    lower = 0
    upper = 0

    # algorithm: start with the ends of the list of primes. 
    # If the sum of the first and last element in primes is
    # greater than the number we want, sum the first element
    # with the 2nd to last one. 
    # if the sum of the first and last element is less than
    # the sum we're seeking, sum the second element and the 
    # last element. 
    # This algorithm is theta(n), or linear time (very nice)
    while(not found):
        if ((primes[lower] + primes[sz - upper]) < num_to_find):
            lower += 1
        elif ((primes[lower] + primes[sz - upper]) > num_to_find):
            upper += 1
        else:
            print(str(primes[lower]), " + ", 
            str(primes[sz - upper]), " = ", str(num_to_find))
            found = True

def main():
    # create a list of inputs (70 - 100)
    inputs = [70, 72, 74, 76, 78, 80, 82, 84, 
            86, 88, 90, 92, 94, 96, 98, 100]

    # print all the sums
    for i in inputs:
        find_sum(i)

# define the entry point of our program
if __name__ == "__main__":
    main()