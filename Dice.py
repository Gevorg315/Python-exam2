import random

dice1 = random.randint(1, 6)
dice2 = random.randint(1, 6)
total = dice1 + dice2
result = f"The sum of dice is {dice1} + {dice2} = {total}"

if total in (7, 11):
    print(result)
    print("You won")
elif total in (2, 3, 12):
    print(result)
    print("You lose")
else:
    goal = total
    print(result)
    print(f"Now your goal number is {goal}")
    while True:
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        total = dice1 + dice2
        result = f"The sum of dice is {dice1} + {dice2} = {total}"
        if total == 7:
            print(result)
            print("You lose")
            break
        elif total == goal:
            print(result)
            print("You won")
            break
        else:
            print(result)