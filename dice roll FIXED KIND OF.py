import random
import time
import sys

i = 0
Player1Points = 0
Player2Points = 0
Player1Tiebreaker = 0
Player2Tiebreaker = 0
Winner_Points = 0

logged_in1 = False
logged_in2 = False
while logged_in1 == False:
    username = input('Enter Your Username - ')
    password = input('Enter Your Password -  ')
    if username == 'Username1' or username == 'Username2' or username == 'Username3' or username == 'Username4' or username == 'Username5':
        if password == 'password':
            print('Welcome, ',username,'. ')
            logged_in1 = True
            user1 = username
        else:
            print('Wrong pass. Try again.')  
    else:
        print('Wrong username. Try again.')

while logged_in2 == False:
    username = input('Enter Your Username - ')
    password = input('Enter Your Password - ')
    if username == 'Username1' or username == 'Username2' or username == 'Username3' or username == 'Username4' or username == 'Username5':
        if password == 'password':
            print('Welcome, ',username,'.')
            logged_in2 = True
            user2 = username
        else:
            print('Wrong pass. Try again.')  
    else:
        print('Wrong pass. Try again.')




### Makes the dice roll for the player and works out the total for that roll


def roll():

    points = 0

    die1 = random.randint(1,6)

    die2 = random.randint(1,6)

    dietotal = die1 + die2

    points = points + dietotal

    if dietotal % 2 == 0:
        points = points + 10

    else:
        points = points - 5

    if die1 == die2:
        die3 = random.randint(1,6)
        points = points +die3

    return(points)


### This rolls the dice 5 times for the players, and then adds up the total. (next section of code)

for i in range(1,5):
    Player1Points += roll()
    print('After this round,',user1, 'you now have: ',Player1Points,' Points')
    time.sleep(1)
    Player2Points += roll()
    print('After this round, ',user2, 'you now have: ',Player2Points,' Points')
    time.sleep(1)

if Player1Points == Player2Points:
    while Player1Tiebreaker == Player2Tiebreaker:


        Player1Tiebreaker = random.randint(1,6)
        Player2Tiebreaker = random.randint(1,6)

    if Player1Tiebreaker > Player2Tiebreaker:
        Player2Points = 0
    elif Player2Tiebreaker > Player1Tiebreaker:
        Player1Points = 0



# This checks which score is bigger, adds to leaderboard

if Player1Points>Player2Points:
    Winner_Points = Player1Points
    winner_User = user1
    winner = (Winner_Points, user1)
elif Player2Points>Player1Points:
    Winner_Points = Player2Points
    winner = (Winner_Points, user2)
    winner_User = user2

print('Nice one,', winner_User,' you won with ',Winner_Points,' Points')

#export code, broken currently so its commented out



#winner = (Winner_Points,winner_User)
#f = open('Winner.txt', 'a')
#f.write(''.join(winner))
#f.close()


###### CODE TO LOAD, UPDATE AND SORT LEADERBOARD ######

### This loads the leaderboard into an array, then compares the scores just gotton and replaces it ###

f = open('Leaderboard.txt', 'r')
leaderboard = [line.replace('\n','') for line in f.readlines()]
f.close()


for idx, item in enumerate(leaderboard):
    if item.split(', ')[1] == winner[1] and int(item.split(', ')[0]) < int(winner[0]):
            leaderboard[idx] = '{}, {}'.format(winner[0], winner[1])
    else:
        pass 

### This sorts the leaderboard in reverse, and then rewrites it ###

leaderboard.sort(reverse=True)

with open('Leaderboard.txt', 'w') as f:
    for item in leaderboard:
        f.write("%s\n" % item)
