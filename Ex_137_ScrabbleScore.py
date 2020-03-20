# Exercise 137: ScrabbleTM Score
#
# In the game of ScrabbleTM, each letter has points associated with it.
# The total score of a word is the sum of the scores of its letters. More common letters are worth fewer points while
# less common letters are worth more points. The points associated with each letter are shown below:
#
# Write a program that computes and displays the ScrabbleTM score for a word. Create a dictionary that maps from
# letters to point values. Then use the dictionary to compute the score.
#

dict_scrabble = {1 : ['A', 'E', 'I', 'L', 'N', 'O', 'R', 'S', 'T', 'U'],
                 2 : ['D', 'G'],
                 3 : ['B', 'C', 'M', 'P'],
                 4 : ['F', 'H', 'V', 'W', 'Y'],
                 5 : ['K'],
                 8 : ['J', 'X'],
                 10 : ['Q', 'Z']
                 }

user_input = 'Hello'.upper()
score_list = []
for item in user_input:
    for k,v in dict_scrabble.items():
        if item in v:
            score_list.append(int(k))
print('final score is  : ',sum(score_list))




