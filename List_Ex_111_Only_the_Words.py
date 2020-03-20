# In this exercise you will create a program that identifies all of the words in a string entered by the user.
# Begin by writing a function that takes a string of text as its only parameter. Your function should return a
# list of the words in the string with the punctu- ation marks at the edges of the words removed.
# The punctuation marks that you must remove include commas, periods, question marks, hyphens, apostrophes,
# exclama- tion points, colons, and semicolons. Do not remove punctuation marks that appear in the middle of a words,
# such as the apostrophes used to form a contraction. For exam- ple, if your function is provided with the string
# "Examples of contractions include: don’t, isn’t, and wouldn’t." then your function should return the list
# ["Examples", "of", "contractions", "include", "don’t", "isn’t", "and", "wouldn’t"].
#
# Write a main  program that demonstrates your function.It should read a string from the user and display all
# of the words in the string with the punctuation marks removed.You will need to import your solution to this exercise
# when completing Exercise 158. As a result, you should ensure that your main program only runs when your file has not
# been imported into another program.

punctuation_marks = [',' , '.' , '?' , '-' , "'", '!', ':' , ';']

def func_onlyOneWords(sampleString):
    result_list = []
    list_string = sampleString.split()
    print('list_string: ', list_string)

    for item in list_string:
        print('item : ', item)
        if item[0] in punctuation_marks:
            result_list.append(item[1:])
        elif item[-1] in punctuation_marks:
            result_list.append(item[:-1])
        else:
            result_list.append(item)
    return result_list

# sampleString = "Examples of contractions include: don’t, isn’t, and wouldn’t."

user_input = input('please enter the words ?')
print('original string is :', user_input)
result = func_onlyOneWords(user_input)
print('resultant string after removal of punctuation is :', result)




print('final_list :',result_list)




