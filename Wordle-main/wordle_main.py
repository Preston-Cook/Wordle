from wordle_funcs import play_wordle
from colorama import Fore,Style,init
from playsound import playsound

init(autoreset=True)

GRAY = Fore.LIGHTBLACK_EX+Style.BRIGHT
GREEN = Fore.GREEN+Style.BRIGHT

word_lst = []

with open('Assets/valid-wordle-words.txt') as fh:
        for word in fh.read().splitlines():
            word_lst.append(word.upper())

playsound('Assets/theme.wav',False)

while True:

    print(GREEN+'''
 - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
|  ░██╗░░░░░░░██╗░█████╗░██████╗░██████╗░██╗░░░░░███████╗ |
|  ░██║░░██╗░░██║██╔══██╗██╔══██╗██╔══██╗██║░░░░░██╔════╝ |
|  ░╚██╗████╗██╔╝██║░░██║██████╔╝██║░░██║██║░░░░░█████╗░░ |
|  ░░████╔═████║░██║░░██║██╔══██╗██║░░██║██║░░░░░██╔══╝░░ |
|  ░░╚██╔╝░╚██╔╝░╚█████╔╝██║░░██║██████╔╝███████╗███████╗ |
|  ░░░╚═╝░░░╚═╝░░░╚════╝░╚═╝░░╚═╝╚═════╝░╚══════╝╚══════╝ |
 - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
                    
                    By Preston Cook
'''+GRAY+'''
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

To Play: Enter 1
To View Rules: Enter 2
To Quit: Enter 3

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
''')
    user_selection = input(GREEN+'Enter a Selection: ')
    playsound('Assets/navigation.wav',False)
    print(GRAY+'\n - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ')

    while user_selection not in ['1','2','3']:
        print(GRAY+'Error: Invalid Input')
        user_selection = input(GREEN+'Enter a Selection: ')
        playsound('Assets/navigation.wav',False)

    if user_selection == '3': 
        print(GREEN+'QUITTING PROGRAM'.center(len(' - - - - - - - - - - - - - - - - - - - - - - - - - - - - - '),'-'))
        print(GRAY+' - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ')
        quit()

    elif user_selection == '2':
        print(GREEN+'THE RULES'.center(len(' - - - - - - - - - - - - - - - - - - - - - - - - - - - - - '),'-'))
        print(GREEN+'''
1) When you begin, the computer will randomly select a 5-letter word
2) You will have 5 attempts to guess the word
3) If a letter is green, it is in the word and in the correct location
4) If a letter is yellow, it is in the word but located in the wrong position
5) If a letter is gray, it is not in the word''')
        print(GRAY+' - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ')

    elif user_selection == '1':
        play_wordle(word_lst)
        print('\n'+GRAY+' - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ')