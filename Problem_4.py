#Problem 4

"""
A palindromic number reads the same both ways. The largest palindrome made from the product
of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

#THE BRIEF
"""
What is consistent in the example and question? What is the question asking for?
    Consistent: TWO n-digit numbers (2-digit in the example, 3-digit in the question)
    What P4 wants: to find the largest product of two N-DIGIT NUMBERS that makes a palindrome

Need two functions:
    fcn 1: returns TRUE if a number is a palindrome, FALSE if not
    fcn 2: multiplies two n-digit numbers and finds the largest palindrome between the two
    
fcn 2 will have 2 loops, where each index multiplies by each other, while the palindrome function tests whether the 
product is a palindrome or not
hint: because we want a largest value, to save time, it might be smart to work backwards
"""


#this function takes a number and determines if it is a palindrome
def is_palindrome(a_number):

    #converts an int to a str so we can divide the length (# of digits) by 2
    str_num = str(a_number)

    #make two empty lists to be compared for equality later
    list_1 = []
    list_2= []

    #we want to add each digit to a list and compare the list for equality
    #no need to check if the number has odd or even number of digits because integer division makes it meaningless
    for i in range(len(str_num)//2):

        #append string value numbers to both lists (digits from front of string to list_1, digits from back to list_2)
        list_1.append(str_num[i])
        list_2.append(str_num[-1-i])

    #if both lists are equal, return TRUE, else FALSE
    if list_1 == list_2:
        return True
    else:
        return False


#this function finds the largest palindrome made from the product of a dig_1-digit number and a dig_2-digit number
def largest_palindrome(dig_1, dig_2):

    #multiply str(9) by both digits, convert to int, use in for loops
    dig_1_max = int(dig_1 * "9")
    dig_2_max = int(dig_2 * "9")

    #this could have been done like above with str(9), and dig_1 - 1, and dig_2 - 1, but here's another way to get min
    dig_1_min = int("1{}".format("0"*(dig_1-1))) - 1
    dig_2_min = int("1{}".format("0"*(dig_2-1))) - 1

    #make an empty list, will append palindrome numbers to it, eventually will return the max of this list
    pal_list = []

    #loop from top digit to lowest n or m-digit, nest another loop in it but with the second input digit
    for i in range(dig_1_max,dig_1_min,-1):
        for j in range(dig_2_max,dig_2_min,-1):

            #if we have a palindrome from the products, we append to the list
            if is_palindrome(i*j):
                pal_list.append(i*j)

    #return max of pal_list
    return (max(pal_list))


def main():
    print(largest_palindrome(3,3))

if __name__ == "__main__":
    main()


#THE DEBRIEF
"""
My solution is inefficient and probably cannot handle numbers larger than 3-digits
Given that Euler tends to ask for absurd numbers to use in problems, 
there is probably a limited set of possible, somewhat efficient solutions to the problem, hence, why it only asked
for the largest palindrome of 3-DIGIT products versus a product of 25-DIGIT numbers.

It's also possible that with my novice level of computer science, I am too ignorant to find a more optimized solution

Also, I just realized I did not need to work backwards given my solution stores all palindromes in a list. Someone can
optimize what I did to instantly stop when finding the biggest possible palindrome, altho I imagine that's not too easy
to determine, whether you actually found the largest palindrome based on factor sizes — I was stumped by that.
(I tried a solution that did that and failed a lot and settled with the possibly inefficient solution above.)
"""
