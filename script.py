import random
money = 100

#Write your game of chance functions here
def coin_flip(bet,guess):
  print("Playing coin_flip...")
  num = random.randint(1,2)
  dic = {1:'Heads',2:'Tails'}
  print("Your guess is {0} and the result is {1}".format(guess, dic[num]))
  if guess == dic[num]:
    print("You have won {0}".format(str(bet)))
    return "You currently have {0}\n".format(str(money+bet))
  else:
    print("You have won {0}".format(str(-bet)))
    return "You currently have {0}\n".format(str(money-bet))

def cho_han(bet, guess):
  print("Playing cho_han...")
  dice1 = random.randint(1,6)
  dice2 = random.randint(1,6)
  dic = {0:'Odd',1:'Even'}
  result = (dice1 + dice2) % 2
  print("Your guess is {0} and the result is {1}".format(guess,dic[result]))
  if dic[result] == guess:
    print("You have won {0}".format(str(bet)))
    return "You currently have {0}\n".format(str(money+bet))
  else:
    print("You have won {0}".format(str(-bet)))
    return "You currently have {0}\n".format(str(money-bet))

def pick_card(bet):
  print("Playing picking cards...")
  pool = []
  for i in range(25):
    result = random.randint(1,25)
    pool.append(result)
  my_draw = pool.pop()
  his_draw = pool.pop()
  print("Your draw is {0} and his draw is {1}".format(my_draw,his_draw))
  if my_draw > his_draw:
    print("You have won {0}".format(str(bet)))
    return "You currently have {0}\n".format(str(money+bet))
  elif my_draw < his_draw:
    print("You have won {0}".format(str(-bet)))
    return "You currently have {0}\n".format(str(money-bet))
  elif my_draw == his_draw:
    print("You have won 0")
    return "You currently have {0}\n".format(str(money))

def roulette(bet, guess):
  print("Playing roulette...")
  num = random.randint(0,2)
  dic = {0:'Odd',1:random.randint(1,100),2:'Even'}
  print("Your guess is {0} and the result is {1}".format(guess, dic[num]))
  if guess == dic[2]:
    print("You have won {0}".format(str(guess)))
    return "You currently have {0}\n".format(str(money+guess))
  elif guess == dic[0] or guess == dic[1]:
    print("You have won {0}".format(str(bet)))
    return "You currently have {0}\n".format(str(money+bet))
  else:
    print("You have won {0}".format(str(-bet)))
    return "You currently have {0}\n".format(str(money-bet))
#Call your game of chance functions here

print(coin_flip(10,'Heads'))
print(cho_han(20,'Odd'))
print(pick_card(25)) 
print(roulette(30,46))