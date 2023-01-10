import random

print('I am thinking of a number between 1 and 20')
rand = random.randint(1, 20)
count = 0
while True:
    print('Take a guess.')
    num = int(input())
    if num > rand:
        print('Your guess is too high.')
        count += 1
        continue
    elif num < rand:
        print('Your guess is too low')
        count += 1
        continue
    else:
        print('Good job! You guessed my number in ' + str(count) + 'guesses')
        break