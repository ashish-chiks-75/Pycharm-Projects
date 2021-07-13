secret_word = "ashish"
guess_count = 0
guess_limit = 3
out_of_guesses = False
guess = ""

print("The word contains only 6 letters")

while guess != secret_word and not(out_of_guesses):
    if guess_count <= guess_limit:
        guess = input("enter your guess = ")
        guess_count+=1
        if guess != secret_word:
            print("try again")
            if not(out_of_guesses):
                print("clue = " +secret_word[:guess_count])
    else: out_of_guesses = True

if out_of_guesses:
    print("you chances are over!!")
else:
    print("you win!!")

