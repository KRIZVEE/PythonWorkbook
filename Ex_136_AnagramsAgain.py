# Exercise 136: Anagrams Again
# The notion of anagrams can be extended to multiple words. For example, “William Shakespeare” and “I am a weakish speller”
# are anagrams when capitalization and spacing are ignored.
# Extend your program from Exercise 135 so that it is able to check if two phrases are anagrams.
# Your program should ignore capitalization, punctuation marks and spacing when making the determination.

import collections
dict_1={}
dict_2={}
user_input_1 = 'William Shakespeare'.lower().split(' ')
user_input_2 = 'I am a weakish speller'.lower().split(' ')
res_usr_ip_1=[]
res_usr_ip_2=[]
list_one = []
list_two = []

def letter_storing(user_input,res_usr_ip):
    for item in user_input:
        for i in range(len(item)):
            if item[i].isalpha():
                res_usr_ip.append(item[i])
    return res_usr_ip

res_usr_ip_1 = letter_storing(user_input_1,res_usr_ip_1)
res_usr_ip_2 = letter_storing(user_input_2,res_usr_ip_2)


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

dict_1 = func_anagram(dict_1,res_usr_ip_1)
dict_2 = func_anagram(dict_2,res_usr_ip_2)

list_one = func_anagram_dict(dict_1,list_one)
list_two = func_anagram_dict(dict_2,list_two)

# Using collections.Counter()
# Using Counter(), we usually are able to get frequency of each element in list, checking for it, for both the list,
# we can check if two lists are identical or not. But this method also ignores the ordering of the elements in the list
# and only takes into account the frequency of elements.


if collections.Counter(list_one) == collections.Counter(list_two):
    print ("The given phrases are anagram")
else :
    print ("The given phrases are not anagram")