def word(alphabets):
    result = ""
    for letter in alphabets:
        if letter in "AEIOUaeiou":
            result = result + "**"
        else:
            result = result + letter
    return result


print(word(input("Enter a word: ")))


