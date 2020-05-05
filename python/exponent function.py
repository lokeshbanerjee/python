def raise_power(base, pow):
    return base * pow
print(raise_power(2, 2))
print("")
print("==============================================================")

#this is an exmaple how for loop will work in index and range

def calculation_of_numbers(no, power):
    answer = 1
    for index in range(power):
        answer = answer * no
    return answer
print(calculation_of_numbers(2,3))





