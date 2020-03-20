# Perfect Numbers
#
# An integer, n, is said to be perfect when the sum of all of the proper divisors of n is equal to n.
# For example, 28 is a perfect number because its proper divisors are 1, 2, 4, 7 and 14, and 1 + 2 + 4 + 7 + 14 = 28.
# Write a function that determines whether or not a positive integer is perfect. Your function will take one parameter.
# If that parameter is a perfect number then your func- tion will return true. Otherwise it will return false.
# In addition, write a main program that uses your function to identify and display all of the perfect numbers between 1 and 10,000.
# Import your solution to Exercise 109 when completing this task.

def func_perfect_num(num):
    result_list = []
    for i in range(1,num):
        if num%i == 0:
            result_list.append(i)

    if sum(result_list) == num:
        return True
    else:
        return False

# n = 28 #int(input('hey user please input the number'))

for n in range(1,10001):
    result = func_perfect_num(n)
    if result:
        print('Whether the number {} is a perfect square ? : {}'.format(n, result))
