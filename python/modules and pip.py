# it import files from external libraries/ lib or from any of th file you made.
# you can also install third part python from pip by going in command prompt.
# anything install from pip it goes in site packages.


with open("test open file.txt") as fp:
    lines = fp.readlines()
    print(lines[3])




