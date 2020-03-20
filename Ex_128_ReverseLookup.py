# select category,brand, count(brand) as BrandCount from products group by brand, category order by BrandCount desc;

# path : cd /Users/kashifrizvee/PycharmProjects/PythonWorkbookDictionaries

# Exercise 128: Reverse Lookup
#
# Write a function named reverseLookup that finds all of the keys in a dictionary that map to a specific value.
# The function will take the dictionary and the value to search for as its only parameters. It will return a (possibly empty)
# list of keys from the dictionary that map to the provided value.
# Include a main program that demonstrates the reverseLookup function as part of your solution to this exercise.
# Your program should create a dictionary and then show that the reverseLookup function works correctly when it
# returns multiple keys, a single key, and no keys. Ensure that your main program only runs when the file containing
# your solution to this exercise has not been imported into another program.

def reverseLookup(dict,val):
    return_val = 0
    for key in dict_rvlkp.keys():
        if val == key:
            return_val = 1
            break

    return bool(return_val)

dict_rvlkp = {'a' : 1,
              'b' : 2,
              'c' : 3}

result = reverseLookup(dict_rvlkp, 'd')
print('requested key is present within the dict ? :', result)

