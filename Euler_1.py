#Problem 1

# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9
# The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

#function that lists all of the natural numbers below a number that are multiples of 2 other numbers
def nat_num_list (below_num, mult1, mult2):
    num_list = []
    for i in range(1,below_num):
        if (i % mult1 == 0) or (i % mult2 == 0):
            num_list.append(i)
    return num_list

#function that finds sum of a list
def sum_list(alist):
    return(sum(alist))

#"""
def main():
    main_list = nat_num_list(1000, 3, 5)
    print(sum_list(main_list))

if __name__ == "__main__":
    main()
#"""