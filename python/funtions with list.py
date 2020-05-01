lucky_numbers = [4, 8, 15, 16, 23, 42]
FAMILY = ["KOVI", "VRISHINA", "SAHARSH", "SABRINA", "RAVEENA", "KOVI"]
print("This command will add to the list")
FAMILY.extend(lucky_numbers)
print(FAMILY)

print("==================================================================================================")

print("This command will append the list and the ammend will always be at the end of the list.")
FAMILY.append("LOKESH")
print(FAMILY)

print("==================================================================================================")

print("This command will add to the specific place an everything will push to the right")
FAMILY.insert(1, "RIANA")
print(FAMILY)

print("==================================================================================================")

print("This will remove the element from the list.")
FAMILY.remove("LOKESH")
print(FAMILY)

print("==================================================================================================")

print("this will remove only the last element from the list.")
FAMILY.pop()
print(FAMILY)

print("==================================================================================================")

print("This will tell you where is the person in the list")
print(FAMILY.index("SAHARSH"))
print(FAMILY)

print("==================================================================================================")
print("==================================================================================================")

print("This will tell you how many same type of values are in the list.")
print(FAMILY.count("KOVI"))

print("==================================================================================================")
print("==================================================================================================")

print("this will sort an alphabet or numbers in order.")
lucky_numbers.sort()
print(lucky_numbers)

print("==================================================================================================")
print("==================================================================================================")

print(" delete the whole list.")
FAMILY.clear()
print(FAMILY)
