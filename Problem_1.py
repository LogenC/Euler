#Problem 1

"""
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9
# The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.
"""

#THE BRIEF
"""
We need a function (fcn) that lists natural numbers below a certain number that are multiples of two different numbers
We could use another fcn to find the sum.
(Altho the second fcn is unnecessary in this situation, as a good principle, let's keep creating fcns for
    each sub-problem)
"""

#this fcn lists all of the natural numbers that are below a number and that are multiples of 2 other numbers
#from the problem: below_num = 10, mult1 = 3, mult2 =5
def nat_num_list (below_num, mult1, mult2):

    #creating an empty list to eventually append the nat. numbers that meet the conditions
    num_list = []

    #for loop lets us go thru all the natural numbers from 1 to the top number (minus 1, bc we want numbers below it)
    for i in range(1,below_num):

        #if statement checks if each number, i, is a multiple, if so the number is added to the list
        if (i % mult1 == 0) or (i % mult2 == 0):
            num_list.append(i)

    #returns a list of all the multiples of mult1 and mult2 below the below_num
    return num_list


#fcn that finds sum of a list — not necessary, but maintaining the principle is important
#returns the answer
def sum_list(alist):
    return(sum(alist))


#main fcn to call the other fcns — good standard to use
def main():
    print(sum_list(nat_num_list(1000, 3, 5)))

if __name__ == "__main__":
    main()


#THE DEBRIEF
"""
The reason fcns are used is because you can change the parameters (params). Instead of going into all the spots
    in the code and finding where you used the specific numbers from the problem, you can change the params just once.
I do this to test my function and make sure it works with the problem example, if it does, that's a pretty good
    indication it will also work with params it wants us to find the sum of.
So the process: break down our problem into manageable sizes that make sense, put our sub-solutions together.
"""
