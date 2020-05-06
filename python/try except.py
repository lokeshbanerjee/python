# catching errors in the code

try:
    no = 12 / 0
    number = int(input("enter your number: "))
    print(number)
except ZeroDivisionError:
    print("zero division")
except ValueError:
    print("only numbers are accepted")
"""you can type in both ways one gives official error message which is the bottom one
    except ZeroDivisionError as err:
    print(err)
"""
