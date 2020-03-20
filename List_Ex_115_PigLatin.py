# Exercise 115: Pig Latin
# Pig Latin is a language constructed by transforming English words. While the ori- gins of the language are unknown,
# it is mentioned in at least two documents from the nineteenth century, suggesting that it has existed for more than 100 years. The
# following rules are used to translate English into Pig Latin:
# • Ifthewordbeginswithaconsonant(includingy),thenalllettersatthebeginningof the word, up to the first vowel (excluding y),
# are removed and then added to the end of the word, followed by ay. For example, computer becomes omputercay and think becomes inkthay.
# • If the word begins with a vowel (not including y), then way is added to the end of the word. For example, algorithm becomes
# algorithmway and office becomes officeway.
# Write a program that reads a line of text from the user. Then your program should translate the line into
# Pig Latin and display the result. You may assume that the string entered by the user only contains lowercase letters and spaces.
#

user_input = input('Please enter the string')

user_list = user_input.split(' ')

print(' user input string in list form is :', user_list)
result_list = []
final_list = ' '
ay_str = 'ay'
way_str = 'way'
for item in user_list:
    first_letter = item[0]
    if first_letter in ['a', 'e', 'i', 'o', 'u']:
        final_list += ' '+ item + way_str
    else:
        final_list += ' ' + item[1:] + first_letter + ay_str

print('final list is :', final_list.strip())

# ay_list=['ay']
# way_list = ['way']
# for item in user_list:
#     # print('item',item)
#     first_letter = [item[0]]
#     # print('===', first_letter)
#
#     if first_letter in ['a', 'e', 'i', 'o', 'u']:
#         result_list.append([item]+ way_list)
#     else:
#         result_list.append([item[1:]] + [first_letter] + ay_list)
#
# print('result_list : ',result_list)
