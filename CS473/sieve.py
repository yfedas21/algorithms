from math import sqrt, floor
MAX = 500

# will output an array of primes
A = []; L = []
# add #'s from 2 to max
for i in range(2, MAX + 1):
  A.append(i)
#print(A)

# loop through 2 - floor of the sqrt of MAX
for i in range(2, int(floor(sqrt(int(MAX)))) + 1):
  if A[i - 2] != 0:
    j = i * i
    while (j <= MAX):
      A[j - 2] = 0
      j = j + i

for p in range(0, len(A)):
  if (A[p] != 0):
    L.append(A[p])

print(L)

# The sieve of Eratosthenes is a clever way to find the prime numbers less
# than n. The way the algorithm works is it starts with an array initialized
# will all consecutive integers from 2 (the first prime) to n (in our case,
# n was 500). The algorithm then takes the first number in the array, squares
# it, and replaces that value with 0. Then the algorithm adds the first number
# the square of the first number, and replaces that value with a 0, and so on.
# So, for example, it takes 2, squares it (2 * 2 = 4), replaces the 4 in the array
# with a 0, adds 2, replaces 6 with 0, adds 2, replaces 8 with 0, etc.

# Once the max value is reached, the next number that exists in the list is taken
# (in our example above, this number would be 3. Three is squared, 9 is replaced 
# with 0, then 9 + 3 is set to 0, and so on.

# Since the next number after three, namely, 4 was already replaced with a zero,
# the actual next number would be 5, which is squared and then added to the square
# iteratively.

# Once all of the numbers that aren't 0 and that are less than the floor of the
# square root of our MAX value are replaced in the list, along with their multiples,
# the list should be filled with a bunch of zeros in the position where the composite
# numbers were removed out of.

# The last step would be to create a new array and add to that array values that
# are in the original list of numbers from 2 to n that aren't 0. This second array
# will then contain our prime numbers that we sought.

#################################### OUTPUT ######################################
# [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73,
#  79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163,
#  167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251,
#  257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349,
#  353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443,
#  449, 457, 461, 463, 467, 479, 487, 491, 499]
