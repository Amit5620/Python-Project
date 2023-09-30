while True:
    
    import random

   
    lower_limit = int(input("Enter the lower limit: "))
    upper_limit = int(input("Enter upper limit: "))

    random_number = random.randint(lower_limit, upper_limit)
    print("You will have to choose a number between ", upper_limit, " and ", lower_limit)

    chances = 0
    while chances < 8:
        chances += 1
        guess = int(input("Enter your guess: "))
        if random_number == guess:
            print("Congratulations, you did it. The number was ", random_number)
            break
        elif guess < random_number:
            print("You guessed a small number.")
        elif guess > random_number:
            print("You guessed a large number.")
        if chances == 7:
            print("\n You've run out of chances")
            print("\n The number was ", random_number)
            print("Better luck next time")
            break
    print("\n")
    break
