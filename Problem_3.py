#Problem 3

"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

#THE BRIEF
"""
Create a function that takes a number, finds its primes, and gives the largest one:

Because finding a prime is not a simple boolean expression, let's break the solution down into 2 fcns:
    Fcn 1: takes an integer and... returns TRUE if int is prime, returns FALSE if not
    Fcn 2: takes an integer — preferably a big number — and finds its largest prime
"""


# fcn 'is_prime' determines if an int is prime
#note: we test only up to the sqrt of the integer test_num. WHY is only up to the square root sufficient?
#   math answer: if a >= b and a * b = x, and sqrt(x) * sqrt (x) = x, then a >= sqrt(x) and b <= sqrt(x)
#   in english: if x is divisible by anything up to it's square root, by definition, it can't be prime
#               hence, because b <= a and a * b = x , and b could equal sqrt(x), by the time you test divisibility
#               up to sqrt(x) (b's highest potential value), if nothing is divisible, the number has to be prime
def is_prime(test_num):

    if test_num == 2:
        return True
    elif test_num % 2 == 0:
        return False

    #this var is the square of the test number
    sqr_num = int(test_num**.5)+1

    #this loop tests odds up to the square for divisibility
    for i in range(3, sqr_num, 2):

        #if anything is divisible up to the square, it's not prime
        if test_num % i == 0:
            return False

    return True


#this fcn finds the largest prime factor of a big number
def largest_prime_factor(big_num):

    #EVEN big numbers
    if big_num % 2 == 0:

        half_num = (big_num // 2)

        #only goes up to half the input number because half is the biggest factor an even number can have
        for i in range(2, half_num + 1):

            # if both the index number is divisible by the input and the corresponding factor is prime
            # this determines the largest prime, because the index starts at the smallest possible factor
            if (big_num % i == 0) and is_prime(big_num//i):
                return big_num//i

    #ODD big numbers
    else:

        third_num = (big_num // 3)

        #only goes up to a third of the input number because a third is the biggest factor an odd number can have
        #scaales by 2 because only odd numbers after 2 can be prime
        for i in range(3, third_num+1, 2):

            if (big_num % i == 0) and is_prime(big_num//i):
                return big_num//i

    #if nothing is returned at this point, then we found a large prime number
    return "You have a prime number!!! And it's {}".format(big_num)


def main():
    print(largest_prime_factor(600851475143))

if __name__ == "__main__":
    main()

    
#THE DEBRIEF
"""
Many solutions floating around on the interwebs do not account for testing even numbers and leave out logic from the 
first part of the if statement in the largest_prime_factor fcn

To have the most encompassing, or general, solution, one must account for as many possibilities as are relevant.
"""
