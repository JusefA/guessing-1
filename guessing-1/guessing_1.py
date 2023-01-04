secret_word = "anime"
guess = ""
guess_count = 0
print("how many guesses would you like to have?")
guess_max =int(input(""))

while guess != secret_word:

    guess = input("guess the word:")
    guess_count += 1
    if guess_count == guess_max:
        print("You lose!")
        break

if guess == secret_word:
    print("You win!")
