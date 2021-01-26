# write in python program which will keep adding a stream of number input by the user.
# the adding stop as soon  as user presses q key on the keyboard



sum = 0           # the initial value is zero

while (True):
    userInput = input("Enter the item price or press q to quick :\n")   # the input will be in string there therefore  it uses int to convert in integer
    if userInput != 'q':
        sum = (sum + int(userInput))
        print('your order so far',sum)
    else:
        print("your total bill is ",sum )
        print("Thanks for shopping with us have a great day ")
        break

# print item price  receipt

print("ABC shopping  store ")



