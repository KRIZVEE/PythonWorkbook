# Exercise 121: Count the Elements
# Python’s standard library includes a method named count that determines how many times a specific value occurs in a list.
# In this exercise, you will create a new function named countRange which determines and returns the number of elements
# within a list that are greater than or equal to some minimum value and less than some maximum value.
# Your function will take three parameters: the list, the minimum value and the maximum value.
# It will return an integer result greater than or equal to 0. Include a main program that demonstrates your
# function for several different lists, minimum values and maximum values. Ensure that your program works correctly
# for both lists of integers and lists of floating point numbers.

# python inbuilt count method syntax:
# string.count(substring, start=..., end=...)


def count_range(user_list, min_num, max_num):
    result_lis = []
    for item in user_list:
        if (item >= min_num and item < max_num):
            result_lis.append(item)
    return len(result_lis)



    pass

new_user_lis = []
while True:
    user_input = input('please enter number for the list (hit 0 to exit)')
    # print('----',type('0'))
    # print('user_input is : ',user_input)
    # print('type(user_input) is :', type(user_input))
    if user_input  == '0':
        break
    elif '.' in user_input :
        new_user_lis.append(float(user_input))
    elif '.' not in user_input :
        new_user_lis.append(int(user_input))
    else:
        continue

print('user entered list is : ',new_user_lis)
user_input_min = int(input('please enter min number for the list'))
user_input_max = int(input('please enter max number for the list'))



# usr_lis = [4,3,6,7,2,9]
# min_val = 2
# max_val = 8
result = count_range(new_user_lis, user_input_min, user_input_max)

print('The final result is : ',result)