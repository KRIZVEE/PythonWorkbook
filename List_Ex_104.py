# Sorted Order

# Write a program that reads integers from the user and stores them in a list. Your program should continue reading values
# until the user enters 0. Then it should display all of the values entered by the user (except for the 0) in order from
# smallest to largest, with one value appearing on each line. Use either the sort method or the sorted
# function to sort the list.

# solution 1
user_list = []
while True:
    user_input = int(input('please enter the numbers for sorting ( hit 0 to exit)'))
    if user_input == 0:
        break
    else:
        user_list.append(user_input)

print("User's entered list is : ", user_list)
user_list.sort() # to avoid changes in original list we make use of sorted function. see solution 2
print(*user_list, sep = "\n")

print("Entered list in sorted form is : ", user_list)
print("User's original Entered list is also get updated in sorted form as : ", user_list)


# solution 2
# user_list = []
# while True:
#     user_input = int(input('please enter the numbers for sorting ( hit 0 to exit)'))
#     if user_input == 0:
#         break
#     else:
#         user_list.append(user_input)
#
# print("User's entered list is : ", user_list)
# orig_list = user_list
# new_list = sorted(orig_list)
# print("Entered list in orignal form is : ", orig_list)
# print("Entered list in sorted form is : ", new_list)