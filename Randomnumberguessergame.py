import random

x = int(input("Enter the starting range: "))
y = int(input("Enter the ending range: "))

z = random.randint(x, y)


chance = 3

while chance > 0:
    print("Number of tries left:", chance)
    num = int(input("Enter your choice: "))

    chance -= 1

    diff = abs(num - z) # to find the abstract difference of the number guessed and number generated 
                        #   to help the player guess more easily
    if diff == 0:
        print("🎉 Congrats! You have won")
        break
    elif diff <= 2:
        print("🔥 Very close!")
    elif diff <= 5:
        print("🙂 Close")
    else:
        print("❄️ Far away")

else:
    print("❌ You failed! The correct number was:", z)
