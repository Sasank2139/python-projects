import random
while True:
    computer_number = random.randint(1, 100)
    guess = 0
    lives = 5
    while guess != computer_number and lives > 0 and p_again:
        try:
            guess = int(input("Guess a number between 1 and 100: "))
        except ValueError:
            print("Please enter a valid number.")
            continue    
        if guess < computer_number:
            print("Too low! Try again.")
            lives -= 1
            print("Lives remaining:", lives)
        elif guess > computer_number:
            print("Too high! Try again.")
            lives -= 1
            print("Lives remaining:", lives)
        else:
            print("Congratulations! You've guessed the number!")
        if lives == 0:
            print("You've run out of lives!")
        print("The correct number was:", computer_number)
        print("Lives remaining: ", lives)
        play_again = input("Do you want to play again? (y/n): ").lower()
        if play_again != "y":
            break
    print("Thanks for playing!")    
