# Exercise 134: Unique Characters
# Create a program that determines and displays the number of unique characters in a string entered by the user.
# For example, Hello, World! has 10 unique characters while zzz has only one unique character. Use a dictionary or
# set to solve this problem.
#
#

dict_uniq_char = {}

user_input = 'Hello, World!'
# user_input = 'zzz'

for item in user_input:
    if item in dict_uniq_char.keys():
        dict_uniq_char[item] += 1
    else:
        dict_uniq_char[item] = 1
num_uniq_chars = []
for key in dict_uniq_char.keys():
    num_uniq_chars.append(key)

print('Number of unique chars is given string "{}" is : {}'.format(user_input,len(num_uniq_chars)))

# solution 2:
user_input_2 = 'zzz'

result = set(user_input_2)
print('Number of unique chars is given string "{}" is : {}'.format(user_input_2,len(result)))
