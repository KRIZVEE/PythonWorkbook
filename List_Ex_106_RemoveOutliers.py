# When analysing data collected as part of a science experiment it may be desirable to remove the most extreme values
# before performing other calculations. Write a function that takes a list of values and an non-negative integer, n,
# as its parameters. The function should create a new copy of the list with the n largest elements and the n smallest
# elements removed. Then it should return the new copy of the list as the function’s only result. The order of the elements
# in the returned list does not have to match the order of the elements in the original list. Write a main program that
# demonstrates your function. Your function should read a list of numbers from the user and remove the two largest and
# two smallest values from it. Display the list with the outliers removed, followed by the original list. Your program
# should generate an appropriate error message if the user enters less than 4 values.

def func_rm_outliers(value_list, pos_int):
    new_list = sorted(value_list)
    # new_list.sort()
    print('Sorted List is : ', new_list)
    return new_list[2:len(value_list)-2]
    # pass

value_list = [111,2,56,34,78,3,6,7,88,189]
while True:
    user_input = int(input('please enter the numbers ( hit 0 to exit'))
    if user_input == 0:
        break
    else:
        value_list.append(user_input)

n = 2
print('Original List is : ', value_list)
result_list = func_rm_outliers(value_list, n)
print('List after removal of outliers :',result_list)
print('Original List before removal of outliers :',value_list)

# still need modification esp try - catch block




