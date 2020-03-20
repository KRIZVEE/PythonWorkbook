# Extend your solution to Exercise 115 so that it correctly handles uppercase letters and punctuation marks such as
# commas, periods, question marks and exclamation marks. If an English word begins with an uppercase letter then its
# Pig Latin representation should also begin with an uppercase letter and the uppercase letter moved to the end of the
# word should be changed to lowercase. For example, Computer should become Omputercay. If a word ends in a punctuation mark
# then the punctuation mark should remain at the end of the word after the transformation has been performed.
# For example, Science! should become Iencescay!.

# punctuation marks such as commas, periods, question marks and exclamation marks.
#
# , . ? !

final_list = ' '
user_input = input('Please enter the string')

user_list = user_input.split(' ')

print(' user input string in list form is :', user_list)
result_list = []
ay_str = 'ay'
way_str = 'way'
# computer --> omputercay ; office --> officeway
def func_upper_care(text):
    result_list_upper = ''
    first_letter = text[0]
    last_letter = text[-1]
    if first_letter in ['A', 'E', 'I', 'O', 'U']:
        if last_letter in [',', '.', '?', '!']:
            result_list_upper += ' ' + text[:-1] + way_str + last_letter
        else:
            result_list_upper += ' '+ text + way_str
    else:
        if last_letter in [',', '.', '?', '!']: #Computer! --> Omputercay!
            result_list_upper += ' ' + text[1:-1].capitalize() + first_letter.lower() + ay_str + last_letter
        else: #Computer --> Omputercay
            result_list_upper += ' ' + text[1:].capitalize() + first_letter.lower() + ay_str
    return result_list_upper

def func_lower_care(text):
    result_list_lower = ''
    first_letter = text[0]
    last_letter = text[-1]
    if first_letter in ['a', 'e', 'i', 'o', 'u']:
        if last_letter in [',', '.', '?', '!']: #office! --> officeway!
            result_list_lower += ' ' + text[:-1] + way_str + last_letter
        else: #office --> officeway
            result_list_lower += ' '+ text + way_str
    else:
        if last_letter in [',', '.', '?', '!']: #computer! --> omputercay!
            result_list_lower += ' ' + text[1:-1] + first_letter + ay_str + last_letter
        else: #computer --> omputercay | you --> ouyay
            result_list_lower += ' ' + text[1:] + first_letter + ay_str
    return result_list_lower

for item in user_list:
    if item[0].isupper():
        final_list += func_upper_care(item)
    else:
        final_list += func_lower_care(item)

print('final list is :', final_list.strip())













