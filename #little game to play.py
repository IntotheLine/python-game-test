# Spiel des Lebens.py

import math
import random

# needs to defined
# playernames
# playercolours
# amount of playrounds
# houses
# cars
# neutral fields
# house fields
# car fields
# random step generator
# add Salery each step
# define selery by promotion
# the idea is with an random generator to add an dictionary


# Besitz durch ein Dictionary einspeichern

# Starts the game asks for the players, theire colours and some easy checks.
print('welcome to Game of Live')
print('this is a ongoing development project')
print('please enter the number of players, please enter 2 until more players can be added')


players = input()
while not players.isdecimal():
    print('please enter a number between 2 and 4')
    players = input()

if players.isdecimal():
    print('Welcome you ' + players + ' players')

if players <= '1':
    print('this is for at least two players yet')
    print('you have to enter again between 2 and 4 ;-)')
    players = input()

if players == '2':
    print('please enter your name for player 1')
    PlayerOneName = input()
    print('please enter your name for player 2')
    PlayerTwoName = input()


print('Welcome %s and %s to your game' % (PlayerOneName, PlayerTwoName))

PlayerColourSelection = {'1': 'yellow', '2': 'red', '3': 'green', '4': 'blue'}
print('Please choose your colour ' + PlayerOneName)

print('1 for yellow, 2 for red, 3 for green, 4 for blue')
PlayerOneColourInput = input()
if PlayerOneColourInput.isdecimal():
    PlayerOneColour = PlayerColourSelection.get(PlayerOneColourInput)
    if not PlayerOneColourInput.isdecimal():
        print('1 for yellow, 2 for red, 3 for green, 4 for blue')
        PlayerOneColourInput = input()
        print(PlayerOneColour)

print('Please choose your colour ' + PlayerTwoName)
PlayerTwoColourInput = input()
while PlayerTwoColourInput == PlayerOneColourInput:
    print(PlayerTwoName + ' I am sorry, but you can not choose the same colour as Player One')
    PlayerTwoColourInput = input()

if PlayerTwoColourInput.isdecimal():
    PlayerTwoColour = PlayerColourSelection.get(PlayerTwoColourInput)
    print(PlayerTwoColour)

print('%s has the colour %s, %s has the colour %s' % (PlayerOneName, PlayerOneColour, PlayerTwoName, PlayerTwoColour))

# this sections defines the amounts of rounds to play.
print('Please enter the amount of rounds you like to play, enter any letter for random amount of rounds to play')
TotalPlayRounds = input()
if not TotalPlayRounds.isdecimal():
    TotalPlayRounds = random.randint(10, 100)
if TotalPlayRounds == int(0):
    print('----Game Over----')
    print('----Programm will calculate the winner now----')

# need to find a container to store each round, if Player One and Player Two matches, substract 1 from total Rounds played
PlayerOneRoundsPlayed = int(0 / 2)
PlayerTwoRoundsPlayed = int(0 / 2)

# this section ads the yearly income of the players
PlayerOneIncome = int(5000)
PlayerTwoIncome = int(5000)

PlayerOneWallet = int(0)
PlayerTwoWallet = int(0)

PlayerOneHouse = '0'
PlayerTwoHouse = '0'

PlayerOneCar = '0'
PlayerTwoCar = '0'

# playground
Playground = {1: 'blank', 2: 'blank', 3: houseoption(), 4: BuyACar(), 5: 'blank', 6: 'blank', 7: BuyACar(), 8: 'Promotion, increase your salery by 5000', 9: 'Demotion, you loose 1000 of your salery', 10: 'blank'}

# possible houses, connect a function to select and add the values
House = {'1': 'Bungalow', '2': 'House', '3': 'Villa'}
HouseValues = {'1': int(20000), '2': int(100000), '3': int(10000000)}

# cars and theire values, possible option for later, car increases the steps a player makes by 1:+1, 2:+2; 3:+3,
Car = {'1': 'VW T1 Bus', '2': 'Saab900Cabrio', '3': 'PorscheBoxster', '4': 'Nothing to Buy'}
CarValues = {'1': int(10000), '2': int(50000), '3': int(100000)}

StartGenerator = random.randint(1, 2)

if StartGenerator == 1:
    print(PlayerOneName + ' , the force tells you to begin')
elif StartGenerator == 2:
    print(PlayerTwoName + ' , the force tells you to begin')

# functions for the game

while TotalPlayRounds >= (PlayerOneRoundsPlayed + PlayerTwoRoundsPlayed) / 2:
    if StartGenerator == 1:
        print(PlayerOneName + ' time to start, the dice gets thrown now')
        salery(PlayerOneIncome)
        DiceThrow = dice()
        print(playground(DiceThrow))
        PlayerOneRoundsPlayed = PlayerOneRoundsplayed + 1
        RoundMove = Playground.get(DiceThrow)
        print(PlayerOneName + ' you have thrown a ' + DiceThrow + ' you are on field ' + Roundmove)
        print(PlayerOneWallet + 'your available funds')


def dice(RandomDice):
    RandomDice = random.randint(1, 10)
    return RandomDice


def salery(PlayerOneIncome, PlayerTwoIncome):
    PlayerOneIncome = PlayerOneWallet + PlayerOneIncome
    PlayerTwoIncome = PlayerTwoWallet + PlayerTwoIncome
    return PlayerOneIncome
    return PlayerTwoIncome


def car(BuyACar):
    print('please enter the "1" for %s and enter the "2" for %s.' % (PlayerOneName, PlayerTwoName))
    BuyACarPlayerOption = input()
    if BuyACarPlayerOption == 1:
        print(PlayerOneName + 'please select a car to buy' + Car)
        print(Car)
        CarBuy = input()
        if not CarBuy.isdecimal():
            print('please enter a value between 1 and 4')
            if CarBuy == '1' or '2' or '3':
                PlayerOneCar = CarValues.get(Carbuy)
                print('Congratulations you bougt a ' + Car.get(Carbuy))
                if CarBuy == '4':
                    True


def houseoption(BuyAHouse):
    print('please enter the Player 1 or Player 2')
    PlayerHouseOptionInput = input()
    if PlayerHouseOptionInput == 1:
        print('you can choose to buy a house now')
        print('press 1 for a Bungalow, costs 20000 Euro, press 2 for a House for 100.000 Euro or a Villa for 1.000.000 Euro press 3, for nothing press 4.')
        PlayerBuyOption = input()
        while PlayerBuyOption == '4':
            break
            if PlayerBuyoption == '1' or '2' or '3':
                PlayerOneHouse = PlayerOneHouse + Housevalues.get(PlayerBuyOption)


print('Get ready to play!')
print('Player start is choosen random')
