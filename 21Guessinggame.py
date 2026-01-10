print("game played by leg")
the_word = "Football"
guess = ""
guess_count = 0
guess_limit = 5
out_of_guess = False

while guess  != the_word and not(out_of_guess):
    if guess_count < guess_limit:
       guess = input("Enter the word: ")
       guess_count += 1
    else:
        out_of_guess = True

if out_of_guess:
    print("Sorry you lost")
else:
    print("congratulation! you won.")
