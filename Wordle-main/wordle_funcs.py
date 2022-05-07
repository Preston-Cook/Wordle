from colorama import Style,Fore,init
from random import choice
from playsound import playsound

init(autoreset=True)

def play_wordle(word_lst):

    guess_history = []
    
    wordle_store = choice(word_lst)

    attempt = 0

    while attempt < 5:

        display_lst = ['','','','','']

        user_store = list(input(Fore.GREEN+Style.BRIGHT+'\nEnter a guess: ').upper())
        playsound('Assets/navigation.wav',False)

        while len(user_store) != 5 or ''.join(user_store) not in word_lst:
            print(Fore.LIGHTBLACK_EX+Style.BRIGHT+'Error: Invalid Input')
            user_store = list(input(Fore.GREEN+Style.BRIGHT+'Enter a guess: ').upper())
            playsound('Assets/navigation.wav',False)
        
        attempt += 1

        if ''.join(user_store) == ''.join(wordle_store):
            break

        for count,(char0,char1) in enumerate(zip(user_store,wordle_store)):
            if char0 == char1:
                display_lst[count] = Fore.GREEN + char0
        
        for count,char0 in enumerate(user_store):
            if display_lst[count] == Fore.GREEN + char0:
                continue
            elif char0 in wordle_store and (display_lst.count(Fore.GREEN+char0) + display_lst.count(Fore.YELLOW+char0)) < wordle_store.count(char0):
                display_lst[count] = Fore.YELLOW + char0 
            else:
                display_lst[count] = Fore.LIGHTBLACK_EX + char0
        
        guess_history.append(''.join(display_lst))

        for guess in guess_history:
            print(Style.RESET_ALL+guess+'\n')
    
    if attempt < 5:
        print(Fore.GREEN+Style.BRIGHT+'CONGRATULATIONS! YOU WIN')
        playsound('Assets/win.wav',True)
    else:
        print(Fore.GREEN+Style.BRIGHT+f"YOU LOSE! THE CORRECT WORD WAS {''.join(wordle_store)}")
        playsound('Assets/lose.wav',True)