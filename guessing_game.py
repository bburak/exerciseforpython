import random

secret_number = random.randint(0,100)
trial_number = 0
done = False

while not(done):
    trial_number += 1
    number_in = (int)(input('Enter your guess (between 0 and 100): '))
    if number_in == secret_number:
        print('Congratulations')
        print('You got it in {} trials.'.format(trial_number))
        done = True
    elif number_in < secret_number:
        print('Try higher...')
    else:
        print('Try lower...')