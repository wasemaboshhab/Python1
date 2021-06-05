# input String and convert to int + change to pounds or kilos
"""
user_weight = int(input('weight: '))
unit = input('(L)bs or (K)g : ')
if unit.upper() == 'L':
    converted = user_weight * 0.45
    print(f"your are {converted} kilos")
elif unit.upper() == 'K':
    converted = user_weight // 0.45
    print(f"your are {converted} pounds")

"""

# while loop guess a number
'''
right_Guess = 9
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    user_guess = int(input('guess:'))
    guess_count += 1
    if user_guess == right_Guess:
        print('right_Guess')
        break
else:  # we can do the same game with out using  else 
    print('Wrong Guess')
'''

#  car game   --- Boolean
'''
command = ""
started = False

while True:
    command = input(">").lower()

    if command == 'start':
        if started:
            print('car is already started')
        else:
            started = True
            print('the car stated.....')

    elif command == 'stop':
        if not started:
            print('the car already stopped')
        else :
            started = False
            print('the car stopped')
    elif command == 'quit':
        break
    elif command == "help":
        print("""
start- to start the car
stop - to stop the car
quit - to exit         
        """)
    else:
        print("i don't understand that.")
'''

# for loop

# for i in 'wasim':
#     print(i)

# for item in ['wasim','siham']:
#     print(item)

# for item in range(10):
#     print(item)

# for item in range(1, 20):
#     print(item)

# for item in range(0, 20, 5):
#     print(item)

# exercise1
"""price = [10, 20, 30]
total = 0
for item in price:
    total += item
print(f"Total: {total}")
"""

# nested loop
"""for x in range(4):
    for y in range(3):
        print(f""
              f"({x},{y})")
"""

# exercise2
"""numbers = [5, 2, 5, 2, 2]
for x_count in numbers:
    output = ''
    for count in range(x_count):
        output += 'x'
    print(output)"""

# list
# find the larger Number  in the lest
"""numbers = [3, 6, 2, 8, 4, 10]
largerNumber = numbers[0]
for number in numbers:
    if number > largerNumber:
        largerNumber = number
print(largerNumber)
"""

# 2D list

"""matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
for row in matrix :
    for item in row:
        print(f"{item} ")"""

#  list methods
# numbers = [5, 2, 1, 5, 7, 4, 20]  # add number to the list
# numbers.append(50) # input number in the last of the list
# numbers.insert(0, 10)  #insert number any where in the list (index,value)
# numbers.remove(5)   #remove number from the list
# numbers.clear()
# numbers.pop()  # remove last item in the list
# print(numbers.index(5))  # check where dose the number exist in the list
# print(50 in numbers)  # another way to check if number exist by using in-(true|false)
# print(numbers.count(5))  # how much number exist in the list
# numbers.sort()  #  sorting
# numbers.reverse()
# numbers2 = numbers.copy()  # cope the original list / any change in the first list in not related to the second


# exercise - remove duplicate
"""numbers = [1, 2, 4, 4, 5, 6, 7, 8, 7]
another_list = []
for number in numbers:
    if number not in another_list:
        another_list.append(number)
print(another_list)
"""

# # Tuples -- its final list - unchanged
# numbers = (1, 2, 3)


# Unpacking
"""coordinates = (1, 2, 3)
x, z, y = coordinates  # -- > another way   / available to do the same with regular list
"""
# Dictionaries
"""customer = {
    "name": "wasim shhab",
    "age": 22,
    "is_verified": True
}
"""
# print(customer)
# print(customer['name'])
# print(customer["birthday"])  # no exist will return error
# print(customer.get("birthday"))  # return None
# print(customer.get("birthday", "jan 30 1999 ")) # not added in the customer
# customer.__setitem__("birthday", 1999) # add to the customer new information
# print(customer["birthday"])

# customer["id"] = 3188  # add information to the  Dictionaries
# print(customer["id"])
""""
we can update information in the customer and it's will change the original customer information   
"""

# dictionaries Exercise - convert phone numbers to words by using dictionary
"""phone = input("phone: ")
digits_mapping = {
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four"
}

temp = ""
for ch in phone:
    temp += digits_mapping.get(ch, "!")+" "
print(temp)
"""

# Emoji Converter
msg = input(">")
words = msg.split(' ')
emojis = {
    ":)": "🙂",
    ":(": '😥',
}
output = ""
for word in words:
    output += emojis.get(word, word) + " "
print(output)

