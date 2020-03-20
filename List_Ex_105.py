# Reverse Order

# Write a program that reads integers from the user and stores them in a list.
# Use 0 as a sentinel value to mark the end of the input. Once all of the values have been read your program
# should display them (except for the 0) in reverse order, with one value
# appearing on each line.

result_list = []

while True:
    user_input = int(input('please enter the numbers ( hit 0 to exit)'))
    if user_input == 0:
        break
    else:
        result_list.append(user_input)

print("User's entered list is : ",result_list)
result_list.reverse()
print("User's entered list in reverse order is : ")
print(*result_list, sep = "\n")

