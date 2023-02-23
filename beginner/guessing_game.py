#Guessing Game
import random

number = random.randrange(1,100)
print(number)
user=0
while number!=user:
    user = int(input('Number: '))
    if number<user:
        print('This number is bigger than random number, type it again')
    elif number>user:
        print('This number is smaller than random number, type it again')
    else:
        print('Congratulations! You hit it!')
