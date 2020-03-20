# A proper divisor of a positive integer, n, is a positive integer less than n which divides evenly into n.
# Write a function that computes all of the proper divisors of a positive integer. The integer will be passed
# to the function as its only parameter. The function will return a list containing all of the proper divisors
# as its only result. Complete this exercise by writing a main program that demonstrates the function by reading
# a value from the user and displaying the list of its proper divisors. Ensure that your main program only runs
# when your solution has not been imported into another file.

result_list =[]
def func_proper_div(num):
    print('num is : ',num)
    for i in range(1,num):
        if num%i == 0:
            print('i is : ',i)
            result_list.append(i)
    return result_list

n = 28 #int(input('hey user please input the number'))
result = func_proper_div(n)
print('the proper division list is : ', result)