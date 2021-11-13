#Problem 6
"""
The sum of the squares of the first ten natural numbers is, 385

The square of the sum of the first ten natural numbers is, 3025

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is
3025 - 385 = 2640

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""

#THE BRIEF
"""
Really only need one fcn, but would be nicer to have two specific ones:
    fcn 1 finds the sum of the squares of the first 'n'' natural numbers
    fcn 2 finds the square of the sum of the first 'n' natural numbers
Then we could throw the subtraction in the main() fcn
These two fcns could be written almost identically, so I'm going to show you two different ways to write them:
    fcn 1 will use arrays: list comprehension
    fcn 2 will be written with a standard for loop
"""


#finds sum of the squares of the first 'n' natural numbers
def sum_sqr_nat_nums(top_num):

    sum_sqr_list = [x**2 for x in range(1, top_num + 1)]

    sum_sqr = sum(sum_sqr_list)

    return sum_sqr


#finds the square of the sum of the first 'n' natural numbers
def sqr_sum_nat_nums(top_num):

    sum_sqr = 0

    for i in range(1,top_num+1):
        sum_sqr += i

    return (sum_sqr**2)


def main():
    print("{} – {} = {}".format(sqr_sum_nat_nums(100), sum_sqr_nat_nums(100),(sqr_sum_nat_nums(100) - sum_sqr_nat_nums(100))))

if __name__ == "__main__":
    main()


#THE DEBRIEF
"""
This is may be the easiest problem to solve up to this point, which is why there are many types of solutions
"""
