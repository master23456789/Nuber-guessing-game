import random
print("Number Guessing Game")
number = random.randint(1,9)
chances = 0
print("Guess a number (between 1 and 9):")
while chances < 5:
   guess = int(input('Enter the guess:-'))
    
   if guess == chances:
     print("CONGRAGULATIONS YOU WON!")
     break
   elif guess < number:
     print('Your guess was too high, guess a lower number',guess)
   else:
     print('Your guess was too low, guess a lower number',guess)
     
     
     chances +=1
     
if not chances < 5:
   print('You Loose!, The number is',number)
