"""
Make a two-player Rock-Paper-Scissors game.
(Hint: Ask for player plays (using input), compare them,
    print out a message of congratulations to the winner, and ask
    if the players want to start a new game)

Remember the rules:

    Rock beats scissors
    Scissors beats paper
    Paper beats rock
"""

wins = 0
while wins == 0:
    p1 = raw_input('Player 1 pick either rock, paper or scissors: ')
    p2 = raw_input('Player 2 pick either rock, paper or scissors: ')

    if (p1 == 'rock' and p2 == 'scissors') or (p1 == 'scissors' and p2 == 'paper') or (p1 == 'paper' and p2 == 'rock'):
            wins += 1
            print('Player 1 wins!')
            break
    elif (p2 == 'rock' and p1 == 'scissors') or (p2 == 'scissors' and p1 == 'paper') or (p2 == 'paper' and p1 == 'rock'):
            wins += 1
            print('Player 1 wins!')
            break
    else:
        print('It\'s a draw! Go again!')

