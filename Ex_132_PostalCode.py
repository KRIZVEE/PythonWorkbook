# Exercise 132: Postal Codes
# In a Canadian postal code, the first, third and fifth characters are letters while the second, fourth and sixth characters
# are numbers. The province can be determined from the first character of a postal code, as shown in the following table.
# No valid postal codes currently begin with D, F, I, O, Q, U, W, or Z.

dict_postal_code = {'Newfoundland' : ['A'],
                    'Nova Scotia' : ['B'],
                    'Prince Edward Island' : ['C'],
                    'New Brunswick' : ['E'],
                    'Quebec' : ['G', 'H', 'J'],
                    'Ontario' : ['K','L','M','N','P'],
                    'Manitoba' : ['R'],
                    'Saskatchewan' : ['S'],
                    'Alberta' : ['T'],
                    'British Columbia' : ['V'],
                    'Nunavat' : ['X'],
                    'Northwest Territories' : ['X'],
                    'Yukan' : ['Y'] }
# eg H2X 2C6  ===> urban address in Quebec
# 1st position signifies Province, 2nd position signifies rural [zero] / urban [non-zero]

# user_input = 'H2X 2C6'
# user_input = 'M4H 1L5'
user_input = 'H0X 2C6'

first_letter = user_input[0]
second_letter = int(user_input[1])
province_name = ''
urbal_or_rural = 'urban'
if second_letter == 0:
    urbal_or_rural = 'rural'
for k,v in dict_postal_code.items():
    if first_letter in v:
        # print('inside of if loop')
        province_name = k
        # break

print('given postal code is for {} address in {} province'.format(urbal_or_rural,province_name) )
