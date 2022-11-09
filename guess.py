from random import randint
import sys
answer = randint(1,10000)



while True:
    try:
        guess = input('Ghiceste numarul intre 1 si 10000 ')
        if 0 <  int(guess) <10001:
            if int(guess) == answer:
                print ('Felicitari, ai ghicit !')
                break
            elif int(guess) > answer:
                print('Incearca unul mai mic')
            elif int(guess) < answer:
                print('Incearca unul mai mare')
        else: print('Incearca sa introduci un numar intre 1 si 10000')
    except ValueError:
        print('Te rog, valoare introdusa sa fie un numar')
        continue