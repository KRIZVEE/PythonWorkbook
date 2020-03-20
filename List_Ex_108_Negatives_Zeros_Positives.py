# Create a program that reads integers from the user until a blank line is entered.
# Once all of the integers have been read your program should display all of the negative numbers,
# followed by all of the zeros, followed by all of the positive numbers. Within each group the numbers
# should be displayed in the same order that they were entered by the user. For example,
# if the user enters the values 3, -4, 1, 0, -1, 0, and -2 then your program should output the values
# -4, -1, -2, 0, 0, 3, and 1. Your program should display each value on its own line.

num_list = []

while True:
    user_input = (input('please enter the number (hit blank line to quit)'))
    if len(user_input.strip()) == 0:
        break
    else:
        num_list.append(int(user_input))

print('number in the list are : ', num_list)
neg_list = []
zero_list = []
pos_list = []
result = []
for item in num_list:
    if item < 0:
        neg_list.append(item)
    elif item == 0:
        zero_list.append(item)
    else:
        pos_list.append(item)
result = neg_list + zero_list + pos_list
print('final list is : ',result)
