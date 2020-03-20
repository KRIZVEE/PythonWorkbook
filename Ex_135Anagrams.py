# Exercise 135: Anagrams
# Two words are anagrams if they contain all of the same letters, but in a different order.
# For example, “evil” and “live” are anagrams because each contains one e, one i, one l, and one v.
# Create a program that reads two strings from the user, determines
# whether or not they are anagrams, and reports the result.

# Here we also learn how to compare two dictionary for it's equivalence

import collections
dict_1={}
dict_2={}
user_input_1 = 'evil'
user_input_2 = 'live'
list_one = []
list_two = []


def func_anagram(dict,user_input):
    # print(type(dict))
    for item in user_input:
        # print('item : ',item)
        if item in dict.keys():
            dict[item] += 1
        else:
            dict[item] = 1
    # print(dict)
    return dict

def func_anagram_dict(dict,lis):
    # print(type(dict))
    for k,v in dict.items():
        lis.append(k)
        lis.append(v)
    # print(dict)
    return lis

dict_1 = func_anagram(dict_1,user_input_1)
dict_2 = func_anagram(dict_2,user_input_2)

list_one = func_anagram_dict(dict_1,list_one)
list_two = func_anagram_dict(dict_2,list_two)

# Using collections.Counter()
# Using Counter(), we usually are able to get frequency of each element in list, checking for it, for both the list,
# we can check if two lists are identical or not. But this method also ignores the ordering of the elements in the list
# and only takes into account the frequency of elements.


if collections.Counter(list_one) == collections.Counter(list_two):
    print ("The given strings are anagram")
else :
    print ("The given strings are not anagram")
