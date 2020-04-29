print("we will learn the if conditions in four possible combinations.")
print("1+2= true", "1+2= false", "1 true + 2 false", "1 false + 2 true")
print("")
print("odering food for my friend")
print("==============================================================")
is_vegetarian = False
is_nonveg = True
if is_vegetarian and is_nonveg:
    print("Can I order vege burger and fish pie for my friend.")
elif is_vegetarian and not is_nonveg:
    print("Can I order vege burger FOR MY friend.")
elif not is_vegetarian and is_nonveg:
    print("Can I order fish pie for my friend.")
else:
    print("Can we have two cokes with ice.")

