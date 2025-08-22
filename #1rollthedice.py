import random
# ask the user
while True:
    answer = input("Do you want to roll the dice, YES or NO?")

if answer.lower()== "yes":
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    print("Your rolled:",dice1, "and",dice2)
    print("Thanks for playing!")
    break
elif answer.lower()=="no":
    print("Okey then, have a nice day!")
    break
else:
    print("Invalid choice! Answer yes or no! Please try again! ")

