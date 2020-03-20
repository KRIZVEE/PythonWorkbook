# Exercise 129: Two Dice Simulation
# (Solved—42 Lines) In this exercise you will simulate 1,000 rolls of two dice. Begin by writing a func- tion that
# simulates rolling a pair of six-sided dice. Your function will not take any parameters. It will return the total
# that was rolled on two dice as its only result. Write a main program that uses your function to simulate rolling
# two six-sided dice 1,000 times. As your program runs, it should count the number of times that each total occurs.
# Then it should display a table that summarizes this data. Express the frequency for each total as a percentage of
# the total number of rolls. Your program should also display the percentage expected by probability theory for each total.
#
#

import numpy as np
def roling_dice():
    dice_1 = np.random.randint(1,7)
    dice_2 = np.random.randint(1,7)
    return dice_1+dice_2
dict_dice = {}
for item in range(1000):
    result = roling_dice()
    if result in dict_dice.keys():
        dict_dice[result] += 1
    else:
        dict_dice[result]=1
print('total number of kvp in dictionary is : ',dict_dice)
print('-----------')
print('perecentage wise : ')
total = 0
sorted(dict_dice.keys())
for vals in dict_dice.values():
    total += vals
for k,v in dict_dice.items():
    per_val = round(v/total * 100,2)
    print('percentage of {} in dice is : {} %'.format(k,per_val))
