# Write a function that determines whether or not a list of values is in sorted order (either ascending or descending).
# The function should return True if the list is already sorted. Otherwise it should return False.
# Write a main program that reads a list of numbers from the user and then uses your function to report whether or not
# the list is sorted.

user_values = []

def is_list_sorted(list_nums):
    result_check= True

    for i in range(0,len(list_nums)):
        for j in list_nums[i+1:]:
            if j > list_nums[i]:
                continue
            else:
                result_check = False
                break

    return result_check

while True:
    user_input = int(input('please enter the numbers(hit 0 ot break'))
    if user_input == 0:
        break
    else:
        user_values.append(user_input)


result = is_list_sorted(user_values)
print(' is the list already sorted :', result)

