# In order to win the top prize in a particular lottery, one must match all 6 numbers on his or her ticket to the 6 numbers
# between 1 and 49 that are drawn by the lottery organizer. Write a program that generates a random selection of 6 numbers for a
# lottery ticket.Ensure that the 6 numbers selected do not contain any duplicates.Display the numbers in ascending order.

# to display a six numbers randomly generated within the range of 1-49
import random

result_list=[]
while True:
    num = random.randrange(1,50,1)
    if num not in result_list:
        result_list.append(num)
    if len(result_list) == 6:
        break
print('original random list',result_list)
result_list.sort()
print('original random list on sort',result_list)
final_lotery_number = ''.join(str(x) for x in result_list)
# final_lotery_number = ' ,'.join(str(x) for x in result_list)
print('final_lotery_number :', final_lotery_number)