import random
import word_list
import ui
import registr

def reg():
    word = registr()
def play_game():
    word = word_list.get_random_word()
    jumbled_word = "".join(random.sample(word, len(word)))

    ui.display_jumbled_word(jumbled_word)

    while True:
        guess = ui.get_player_guess()

        if guess == word:
            ui.display_result(f"Правильное слово было {word}")
            break
        else:
            ui.display_result("неправильное слово попровуй сново")

play_game()