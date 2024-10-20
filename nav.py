import random
from stats import Statistics
from core import analyze
from coloring import colored_word

def run_game(dict_file):
    ''' Main function used to navigate and run the game'''
    stats = Statistics()
    while True:
        '''Opens the wordle_dictionary txt'''
        wordle_file = open('wordle_dictionary.txt', "r")
        wordle_dict = wordle_file.read()
        word_list = wordle_dict.split()
        secret_word = random.choice(word_list)
        num_guesses = 0
        '''Keeping the guesses under 7'''
        while num_guesses < 7:
            guessed_word = input("Enter your guess: ")
            guessed_word = guessed_word.upper()
            if not guessed_word.isalpha():
                print('Only letters please :)')
                num_guesses = num_guesses

            if len(guessed_word) < 5 or len(guessed_word) > 5:
                print('5 letter words >:(')
                num_guesses = num_guesses

            if guessed_word.isalpha() is False or len(guessed_word) != len(secret_word):
                print("Invalid input.")
                continue
            elif guessed_word not in word_list:
                print('Invalid input.')
            elif guessed_word != secret_word:
                print("Incorrect.")
                analysis_result = analyze(guessed_word, secret_word)
                correct_colors = colored_word(guessed_word, analysis_result)
                print("Letter Analysis:", correct_colors)
                num_guesses += 1
                if num_guesses < 7:
                    print(f'You have guessed {num_guesses} time(s)')
                continue
            else:
                break
        analysis_result = analyze(guessed_word, secret_word)
        correct_colors = colored_word(guessed_word, analysis_result)
        print("Letter Analysis:", correct_colors)
        if guessed_word == secret_word:
            print("Won")
            # print stats
            stats.add_won_game(num_guesses)
            stats.print_stats()
        else:
            print("Lost")
            print("The correct word was", secret_word)
            # print stats
            stats.add_lost_game()
            stats.print_stats()


        play_again = input("Play again? (y/n): ")
        if play_again.lower() != 'y':
            break