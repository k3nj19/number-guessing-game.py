import random
chosen_number = random.randint(1,100)

def number_guessing_game():
    print("Welcome to the number guessing game!")
    print("I'm thinking of a number from 1 to 100.")
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard'. ").lower()

    if difficulty == 'easy':
        attempts = 10
    elif difficulty == 'hard':
        attempts = 7
    game_ends = False
    print(f"Attempts remaining: {attempts}")
    while not game_ends:
        user_guess = int(input("Make a guess: "))
        if user_guess != chosen_number:
            attempts -= 1
            if user_guess < chosen_number:
                print("Too low.")
            elif user_guess > chosen_number:
                print("Too high.")
            print("Guess again.")
            print(f"Attempts remaining: {attempts}")
        elif user_guess == chosen_number:
            print(f"You got it! The answer was {chosen_number}.")
            game_ends = True
        elif attempts == 0:
            print(f"You ran out of attempts. The answer was {chosen_number}.")
            game_ends = True
    play_again = input("Do you want to play another game? Type 'y' or 'n'. ").lower()
    if play_again == 'y':
        number_guessing_game()
    else:
        print('Goodbye.')
number_guessing_game()
