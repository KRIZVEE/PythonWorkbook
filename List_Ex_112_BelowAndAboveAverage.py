# Write a program that reads numbers from the user until a blank line is entered.
# Your program should display the average of all of the values entered by the user.
# Then the program should display all of the below average values, followed by all of the average values (if any),
# followed by all of the above average values. An appropriate label should be displayed before each list of values.

# skeleton structure
# blank line user_input
# cal of avg
# below avg - avg value if present within the list - abv avg values


def func_avg(num_list):
    result_list = []
    below_avg = []
    above_avg = []
    avg_val = sum(num_list) / len(num_list)
    print('average value is :', avg_val)
    for item in num_list:
        if item < avg_val:
            below_avg.append(item)
        elif item > avg_val:
            above_avg.append(item)
        elif item == avg_val:
            above_avg.insert(0, item)

    print('below avg list of values : ', below_avg)
    print('above avg list of values : ', above_avg)

    result_list = below_avg + above_avg

    return result_list


user_value = []
while True:
    user_input = input('please enter the numbers (hti blank to exit)')
    if len(user_input.strip()) == 0:
        break
    else:
        user_value.append(int(user_input))

print('user input values are : ',user_value)
result = func_avg(user_value)
print(result)
