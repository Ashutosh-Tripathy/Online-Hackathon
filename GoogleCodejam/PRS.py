
'''
Created on Dec 18, 2016

@author: tripathy
'''
# P R S

with open('A-large-practice (1).in') as f:
    content = f.readlines()

def get_alphbeticaly_correct_sequence(N, R, P, S):
    possible_winner = ["P", "R", "S"]
    for player in possible_winner:
        sequence, temp = player, ""
        for x in range(N):
            # print(sequence)
            for item in sequence:
                temp += player_winner_map[item]

            # print(temp)

            # print(temp)
            sequence = temp
            temp = ""
        # print(sequence)
        if(sequence.count("R") == R and sequence.count("P") == P and sequence.count("S") == S):
            return sequence
    return "IMPOSSIBLE"


player_winner_map = {"P" : "PR", "R" : "RS", "S": "PS"}
number_of_test_cases = int(content.pop(0))
for y in range(number_of_test_cases):
    N, R, P, S = [int(x) for x in content.pop(0).split()]
    x = (R + P - S) / 2
    if (not x.is_integer() or x > min(P, R)):
        print("Case #"+str(y+1)+": " +"IMPOSSIBLE")
    else:
        print("Case #"+str(y+1)+": " + get_alphbeticaly_correct_sequence(N, R, P, S))

# #
# # for x in range(5):
# #     print (x)
# R P S

# r-x p-x rp x
# r-x s-(r-x) rs (r-x)
# p-x = s -r + x
# r+p-s = 2x