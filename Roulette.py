'''
Roulette Game

Need to work out what is red and black
'''

import random,time

def spinWheel():
    print ("Lets spin the wheel")
    time.sleep(1)
    print ("Spinning",end = "")
    time.sleep(1)
    for i in range (0,8):
        print (".",end = "")
        time.sleep(0.5)
    roulette_number = random.randint(0,36)
    time.sleep(1)
    if roulette_number in red_list:
        print ("RED {0}".format(roulette_number))
    elif roulette_number in black_list:
        print ("BLACK {0}".format (roulette_number))
    else:
        print ("GREEN 0")
    time.sleep(2)
    return roulette_number
    
def placeBet(balance):
    
    
    
    while True:
        try:
            bet_amount = int(input("Please enter your amount to bet: "))
            
        except ValueError:
            print ("That is not a valid amount")
            continue
        if bet_amount > balance:
            print ("That is too high a bet")
        else:
            break
        
            
    print ("You can place bets on:")
    print ("A single number")
    print ("ODD or EVEN")
    print ("RED or BLACK")
    print ("1-12 // 13-24 // 25-36")
    print ("Good Luck")
    while balance > 0 and bet_amount <= balance:
        
        
        bet = input("Please enter your bet or press enter to spin the wheel!: ")
        if bet.isdigit() and int(bet) > 0 and int(bet) < 37:
            bet_list.append (bet)
            balance -= bet_amount
        elif bet.upper() == "EVEN":
            bet_list.append ("EVEN")
            balance -= bet_amount
        elif bet.upper() == "ODD":
            bet_list.append ("ODD")
            balance -= bet_amount
        elif bet.upper() == "RED":
            bet_list.append ("RED")
            balance -= bet_amount
        elif bet.upper() == "BLACK":
            bet_list.append ("BLACK")
            balance -= bet_amount
        elif bet == "1-12":
            bet_list.append ("1-12")
            balance -= bet_amount
        elif bet == "13-24":
            bet_list.append ("13-24")
            balance -= bet_amount
        elif bet == "25-36":
            bet_list.append ("25-36")
            balance -= bet_amount
        elif bet == "" and len(bet_list) > 0:
            
            break
        else:
            print ("Please enter a valid bet")
        
    print ("All bets placed")
        
    print ("You have placed bets on: ")
    
    for item in bet_list:
        print (item)
        
    time.sleep(1)
    return bet_amount
    


def checkResult(bet_amount):
    total_winnings = 0
    winnings = 0
    for bet in bet_list:
        print ("Checking bets.....")
        time.sleep (1)
        
        if bet == str(roulette_number):
            print ("{0} is a winning number".format(roulette_number))
            winnings = bet_amount * 35
            total_winnings += winnings
            print ("You won £{0} with a bet of {1}".format (winnings,bet_amount))
        elif str(bet) == "ODD" and roulette_number % 2 == 1:
            print ("{0} is a winning ODD number".format(roulette_number))
            winnings = bet_amount * 2
            total_winnings += winnings
            print ("You won £{0} with a bet of {1}".format (winnings,bet_amount))
        elif str(bet) == "EVEN" and roulette_number % 2 == 0:
            print ("{0} is a winning EVEN number".format(roulette_number))
            winnings = bet_amount * 2
            total_winnings += winnings
            print ("You won £{0} with a bet of {1}".format (winnings,bet_amount))
        elif str(bet) == "RED" and roulette_number in red_list:
            print ("{0} is a winning RED number".format(roulette_number))
            winnings = bet_amount * 2
            total_winnings += winnings
            print ("You won £{0} with a bet of {1}".format (winnings,bet_amount))
        elif str(bet) == "BLACK" and roulette_number in black_list:
            print ("{0} is a winning BLACK number".format(roulette_number))
            winnings = bet_amount * 2
            total_winnings += winnings
            print ("You won £{0} with a bet of {1}".format (winnings,bet_amount))
        elif str(bet) == "1-12" and roulette_number > 0 and roulette_number < 13:
            print ("{0} is a winning 1-12 number".format(roulette_number))
            winnings = bet_amount * 3
            total_winnings += winnings
            print ("You won £{0} with a bet of {1}".format (winnings,bet_amount))
        elif str(bet) == "13-24" and roulette_number > 12 and roulette_number < 25:
            print ("{0} is a winning 13-24 number".format(roulette_number))
            winnings = bet_amount * 3
            total_winnings += winnings
            print ("You won £{0} with a bet of {1}".format (winnings,bet_amount))
        elif str(bet) == "25-36" and roulette_number > 24 and roulette_number <= 36 :
            print ("{0} is a winning 25-36 number".format(roulette_number))
            winnings = bet_amount * 3
            total_winnings += winnings
            print ("You won £{0} with a bet of {1}".format (winnings,bet_amount))
    return total_winnings


play = True
balance = 100
while play:
    red_list = [1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36]
    black_list = [2,4,6,8,10,11,13,15,17,20,22,24,26,28,29,31,33,35]
    bet_list = []
    print ("Money: £{0}".format(balance))
    #To cheat uncomment the line below
    #roulette_number = spinWheel() 
    bet_amount = placeBet(balance)
    for item in bet_list:
        balance -= bet_amount
    print ("Your remaining balance is £{0}".format(balance))
    time.sleep(1)
    #To cheat comment the line below
    roulette_number = spinWheel()
    total_winnings = checkResult(bet_amount)
    time.sleep(1)
    print ("Your total winnings is £{0}".format (total_winnings))
    time.sleep(1)
    balance += total_winnings
    time.sleep(1)
    print ("You now have a balance of £{0}".format(balance))
    if balance == 0:
        print ("You have run out of money")
        time.sleep(1)
        print ("Better luck next time")
        break
    
    choice = input ("Would you like to play again? [Y//N]")
    if choice.upper() == "N":
        print ("Ok Goodbye")
        break
    else:
        play = True
        
            
            
      



            
   