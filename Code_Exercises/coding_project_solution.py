import random

# Project
# Generate a list of numbers
# Pick 6 numbers randomly from 1-70
# Pick 1 number randomly from 1-15

pool_one = list(range(1,71))
pool_two = list(range(1,26))

numbers_selected = []
num_selected = 0

numbers_string_output = ""
comma_string_connector = ", "
five_num_label = "Numbers from 1-70: "
one_num_label = "Numbers from 1-25: "

def getPoolNumbers():
    counter = 0
    while counter < 5:
        selected_number = random.choice(pool_one)
        numbers_selected.append(selected_number)
        pool_one.remove(selected_number)
        counter = counter + 1

def getPoolNumber():
    selected_number = random.choice(pool_two)
    return selected_number

getPoolNumbers()
num_selected = getPoolNumber()

for item in numbers_selected:
    numbers_string_output = numbers_string_output + str(item) + comma_string_connector

print("!----     Potential Mega Millions Winning Lottery     ----!")
print(five_num_label + numbers_string_output.rstrip(comma_string_connector))
print(one_num_label + str(num_selected))