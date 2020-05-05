secrect_word = "LION"
guess = ""
turn = 0
limit = 3
out = False
print("Enter an animal name who is king of the jungle:")
print("YOU HAVE THREE GUESSES")
print("")
while guess != secrect_word and not (out):
    if turn < limit:
       guess = input(" ENTER YOUR GUESS")
       turn += 1
    else:
        out = True

if out:
    print("")
    print("YOU LOSE.. YOU RAN OUT OF YOUR GUESSES")
else:
    print("")
    print("You got it. Congratulation you won the game")

