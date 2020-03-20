# When writing out a list of items in English, one normally separates the items with commas.
# In addition, the word “and” is normally included before the last item, unless the list only contains one item.
# Consider the following four lists:
# apples
# apples and oranges
# apples, oranges and bananas
# apples, oranges, bananas and lemons
# Write a function that takes a list of strings as its only parameter. Your function should return a
# string that contains all of the items in the list formatted in the manner described previously as its only result.
# While the examples shown previously only include lists containing four elements or less, your function should behave
# correctly for lists of any length. Include a main program that reads several items from the user, formats them by calling
# your function, and then displays the result returned by the function.
#

def func_format(text):
    result_list = []
    if len(text) == 1:
        return ''.join(text)
    if len(text) == 2:
        return ' and '.join(text)
    for item in text[:-1]:
        result_list.append(item)
    # print('result_list :', result_list)

    final_string = ', '.join(result_list)
    # print(' latest final_string : ', final_string)
    new_string = final_string + ' and ' + text[-1]
    # print(' latest new_string : ', new_string)
    return new_string

user_values = []
while True:
    user_input = input('please enter item names (hit 0 to exit)')
    if user_input == '0':
        break
    else:
        user_values.append(user_input)

result = func_format(user_values)
print('user entered list of items are :',result)