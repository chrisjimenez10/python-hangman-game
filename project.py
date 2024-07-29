import random
import stages
import clear

word_list = [
    "wendy",
    "chris",
    "amway",
    "bww",
    "free"
]

def startHangman():

    wins = 0
    losses = 0

    while True:
        clear.clear_console()
        chosen_word = random.choice(word_list)
        word_length = len(chosen_word)
        # print(chosen_word)

        display = ["-" for letter in chosen_word]
        chances = 6

        print(F"Your word has {word_length} letters and you have {chances} lives to guess the word correctly - Good Luck!")

        while True:

            if chances == 6:
                print(stages.stages[6])
            elif chances == 5:
                print(stages.stages[5])
            elif chances == 4:
                print(stages.stages[4])
            elif chances == 3:
                print(stages.stages[3])
            elif chances == 2:
                print(stages.stages[2])
            elif chances == 1:
                print(stages.stages[1])

            player_guess = input(F"{display}\nGuess a letter:\n").lower()

            for position in range(word_length):
                letter = chosen_word[position]
                if player_guess == letter:
                    display[position] = letter
            
            if player_guess not in chosen_word:
                chances -= 1

            if chances == 0:
                print(F"{stages.stages[0]}\nYou have {chances} guesses left and ran out of lives - Game Over...")
                losses += 1
                break

            if "-" not in display:
                print(F"Congratulations, your word was {chosen_word} - You Win!")
                wins += 1
                break

        reset_status = input("Play again? - Type Y to play again or anything else to exit\n").lower()
        if reset_status != "y":
            print(F"Your record was: {wins} Wins - {losses} Losses\nExiting...")
            return

startHangman()