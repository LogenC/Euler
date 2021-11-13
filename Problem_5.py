#Problem 5
"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

#THE BRIEF
"""
Need to find the 1st number divisible by a range of two numbers 
    (scale by the larger one, and start loop from the larger)
How? Using a while loop, I will make a condition that restarts the logic if a number from 1 to 20 does not divide the
number we are testing.
"""


#fcn finds the smallest number divisible by all the ints in a range of num_1 to num_2
def smallest_div_num(num_1, num_2):

    #starting number
    start_num = num_2
    divis_counter = 0

    #Need a nested for loop in the while; i'll break the while loop once we are divisible by num_2+1 - num_1 numbers
    while divis_counter != (num_2+1-num_1):
        for i in range(num_1,num_2+1):
            if start_num % i != 0:
                start_num+=num_2
                divis_counter = 0
                break

            else:
                divis_counter+=1

    return start_num


def main():
    print(smallest_div_num(1,20))

if __name__ == "__main__":
    main()


#THE DEBRIEF
"""
Like problem 4, it's possible there could be a more efficient solution, but the problem did not ask to test an
absurd number range. IT gave 1 to 10 as an example and 1 to 20 to solve (not something like 1 to 27000).

So, again, there's probably a limit to how efficient this problem can be solved. (It's normal if the code takes time)
"""
