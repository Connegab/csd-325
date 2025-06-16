'''Cho-Han, by Al Sweigart al@inventwithpython.com
The traditional Japanese dice game of even-odd.
 Modified by Gabe Conner
 Assignment Number: 3.2'''

import random, sys

JAPANESE_NUMBERS = {1: 'ICHI', 2: 'NI', 3: 'SAN',
                    4: 'SHI', 5: 'GO', 6: 'ROKU'}

print('''Cho-Han, by Al Sweigart al@inventwithpython.com

In this traditional Japanese dice game, two dice are rolled in a bamboo
cup by the dealer sitting on the floor. The player must guess if the
dice total to an even (cho) or odd (han) number.

**Note:** If you roll a 2 or a 7, you get a 10 mon bonus!
''')

purse = 5000
while True:  # Main game loop.
    # Place your bet:
    print('You have', purse, 'mon. How much do you bet? (or QUIT)')
    while True:
        pot = input('GMC: ')  # Updated input prompt with initials
        if pot.upper() == 'QUIT':
            print('Thanks for playing!')
            sys.exit()
        elif not pot.isdecimal():
            print('Please enter a number.')
        elif int(pot) > purse:
            print('You do not have enough to make that bet.')
        else:
            # This is a valid bet.
            pot = int(pot)  # Convert pot to an integer.
            break  # Exit the loop once a valid bet is placed.

    # Roll the dice.
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    diceTotal = dice1 + dice2  # Total of dice roll

    print('The dealer swirls the cup and you hear the rattle of dice.')
    print('The dealer slams the cup on the floor, still covering the')
    print('dice and asks for your bet.')
    print()
    print('    CHO (even) or HAN (odd)?')

    # Let the player bet cho or han:
    while True:
        bet = input('> ').upper()
        if bet != 'CHO' and bet != 'HAN':
            print('Please enter either "CHO" or "HAN".')
            continue
        else:
            break

    # Reveal the dice results:
    print('The dealer lifts the cup to reveal:')
    print('  ', JAPANESE_NUMBERS[dice1], '-', JAPANESE_NUMBERS[dice2])
    print('    ', dice1, '-', dice2)

    # Determine if the player won:
    rollIsEven = (diceTotal % 2 == 0)
    if rollIsEven:
        correctBet = 'CHO'
    else:
        correctBet = 'HAN'

    playerWon = bet == correctBet

    # Display the bet results:
    if playerWon:
        print('You won! You take', pot, 'mon.')
        purse = purse + pot  # Add the pot to player's purse.

        # Updated house fee to 12%
        house_fee = int(pot * 0.12)
        print(f'The house collects a {house_fee} mon fee.')
        purse = purse - house_fee  # Deduct the house fee (12%).
    else:
        purse = purse - pot  # Subtract the pot from player's purse.
        print('You lost!')

    # Check for 10 mon bonus if the dice total is 2 or 7
    if diceTotal == 2 or diceTotal == 7:
        print(f'You rolled a {diceTotal}! You get a 10 mon bonus.')
        purse += 10  # Add 10 mon bonus to the purse.

    # Check if the player has run out of money:
    if purse == 0:
        print('You have run out of money!')
        print('Thanks for playing!')
        sys.exit()
