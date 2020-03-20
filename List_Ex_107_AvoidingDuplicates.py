# In this exercise, you will create a program that reads words from the user until the user enters a blank line.
# After the user enters a blank line your program should dis- play each word entered by the user exactly once.
# The words should be displayed in the same order that they were entered. For example, if the user enters:
# first
# second
# first
# third
# second
# then your program should display:
# first
# second
# third

word_list = []

while True:
    user_input = input("Please enter the word's (hit blank line to quit)")
    if len(user_input.strip()) == 0:
        break
    else:
        word_list.append(user_input)

print('word list entered by the user is : ', word_list)
new_word_list = []
for item in word_list:
    new_word_list.append(item.lower())

print('word list entered by the user in lowercase is : ', new_word_list)
result=[]
for item in new_word_list:
    if item in result:
        continue
    else:
        result.append(item)
print('final list is :')
print(*result, sep = "\n")
# ss = set(new_word_list)
# print(ss)
