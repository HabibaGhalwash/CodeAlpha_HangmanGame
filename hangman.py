import random

def hangman():
    word_list = ["apple", "banana", "grape", "orange", "lemon"]
    selected_word = random.choice(word_list)
    guessed_word = ["_"] * len(selected_word)
    guessed_letters = []
    attempts_left = 6

    print("Welcome to Hangman!")
    print("Guess the word:", " ".join(guessed_word))

    while attempts_left > 0 and "_" in guessed_word:
        guess = input("Enter a letter: ").lower()

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in selected_word:
            for i in range(len(selected_word)):
                if selected_word[i] == guess:
                    guessed_word[i] = guess
            print("Good job:", " ".join(guessed_word))
        else:
            attempts_left -= 1
            print(f"Wrong guess. Attempts left: {attempts_left}")
            print("Current word:", " ".join(guessed_word))

    if "_" not in guessed_word:
        print("🎉 Congratulations! You won!")
    else:
        print(f"😢 You lost! The word was: {selected_word}")

hangman()