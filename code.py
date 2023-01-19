import os
import random
import time

os.system("clear")

print(
"""

███████╗░██████╗░█████╗░░█████╗░██████╗░███████╗  ██████╗░░█████╗░░█████╗░███╗░░░███╗██╗██╗
██╔════╝██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔════╝  ██╔══██╗██╔══██╗██╔══██╗████╗░████║██║██║
█████╗░░╚█████╗░██║░░╚═╝███████║██████╔╝█████╗░░  ██████╔╝██║░░██║██║░░██║██╔████╔██║██║██║
██╔══╝░░░╚═══██╗██║░░██╗██╔══██║██╔═══╝░██╔══╝░░  ██╔══██╗██║░░██║██║░░██║██║╚██╔╝██║╚═╝╚═╝
███████╗██████╔╝╚█████╔╝██║░░██║██║░░░░░███████╗  ██║░░██║╚█████╔╝╚█████╔╝██║░╚═╝░██║██╗██╗
╚══════╝╚═════╝░░╚════╝░╚═╝░░╚═╝╚═╝░░░░░╚══════╝  ╚═╝░░╚═╝░╚════╝░░╚════╝░╚═╝░░░░░╚═╝╚═╝╚═╝
"""
)

print("By Sazid Rahman\n")

charecter_status = {
  "mood": "neutral",
  "key_status": False
}

list_of_books = ["1918", "The Meth Head", "The Lord Regent's Lore", "The Depths is calling", "Reverse 990"]

def menu():
    print("Start (s)")
    print("Quit (q)\n")

menu()

menu_ans = input("You sure you accept this challenge?:")

def rsp():
    # simple game of rock paper scissors
    os.system("clear")
    print("""

░█████╗░██╗░░░░░░█████╗░░██████╗░██████╗██╗░█████╗░
██╔══██╗██║░░░░░██╔══██╗██╔════╝██╔════╝██║██╔══██╗
██║░░╚═╝██║░░░░░███████║╚█████╗░╚█████╗░██║██║░░╚═╝
██║░░██╗██║░░░░░██╔══██║░╚═══██╗░╚═══██╗██║██║░░██╗
╚█████╔╝███████╗██║░░██║██████╔╝██████╔╝██║╚█████╔╝
░╚════╝░╚══════╝╚═╝░░╚═╝╚═════╝░╚═════╝░╚═╝░╚════╝░
                           """)
    print("You choose to play a game of rock paper scissors.\n")
    print("You see a rock, a paper and a scissor on the table.\n")
    print("You can choose to pick any of them.\n")
    print("You can also choose to not play the game.\n")
    print("You can also choose to leave the room.\n")
    print("What do you choose?\n")
    print("Rock (r)")
    print("Paper (p)")
    print("Scissor (s)")
    print("Leave (l)")
    cpu = random.choice(["rock", "paper", "sicssor"])
    game_ans = input("Your choice:")
    if game_ans == 'r':
        if cpu == "rock":
            print("You chose rock and the computer chose rock. It's a tie.\n")
            input("Press enter to continue...")
            game_menu()
        elif cpu == "paper":
            print("You chose rock and the computer chose paper. You lose.\n")
            input("Press enter to continue...")
            game_menu()
        elif cpu == "scissor":
            print("You chose rock and the computer chose scissor. You win.\n")
            print("The man tells you a secert something that can be helpful towards your escape")
            input("Press enter to continue...")
            game_menu()
        
def hangman():
    os.system("clear")

# List of words to choose from
    words = ["python", "programming", "language", "computer", "science"]

# Choose a random word from the list
    answer = random.choice(words)

# Create a list of underscores the same length as the chosen word
    display = ["_"] * len(answer)

# Keep track of the number of incorrect guesses
    incorrect_guesses = 0

# Keep track of the letters that have been guessed
    guessed_letters = []

# Loop until user guesses the word or runs out of guesses
    while "_" in display and incorrect_guesses < 6:
    # Ask user to guess a letter
        guess = input("Guess a letter: ").lower()

    # Check if the letter has already been guessed
        if guess in guessed_letters:
            print("You already guessed that letter. Try again.")
    # Check if the letter is in the word
        elif guess in answer:
        # Update the display list with the correctly guessed letter
            for i in range(len(answer)):
                if answer[i] == guess:
                    display[i] = guess
            print(" ".join(display))
        else:
        # Increment the number of incorrect guesses
            incorrect_guesses += 1
            print("Incorrect. You have", 6 - incorrect_guesses, "guesses left.")
        guessed_letters.append(guess)
        
# Check if the user won or lost
    if "_" not in display:
        print("Congratulations! You guessed the word.")
    else:
        print("Sorry, you ran out of guesses. The word was", answer + ".")

def door():
    os.system("clear")
    print(
    """
███████╗██╗░░██╗██╗████████╗
██╔════╝╚██╗██╔╝██║╚══██╔══╝
█████╗░░░╚███╔╝░██║░░░██║░░░
██╔══╝░░░██╔██╗░██║░░░██║░░░
███████╗██╔╝╚██╗██║░░░██║░░░
╚══════╝╚═╝░░╚═╝╚═╝░░░╚═╝░░░                
    """)
    print("You choose to search the door:\n")
    print("You look at the door's handel and see a lock which can be opened using a key.")
    open_door = input("Would you want to open it? (y/n)\n")
    if open_door == 'y':
        # Check if charecter_status key_status is true
        if charecter_status["key_status"] is True:
            print("You have the key. You open the door and escape the room.\n")
            krnl()
        else:
            print("You don't have a key. You can't open the door.\n")
            input("Press enter to continue...")
            game_menu()
    elif open_door == 'n':
        os.system("clear")
        print("You decide not to open the door.\n")
        input("Press enter to continue...")
        game_menu()
    else:
        print("Invalid input. Try again.\n")
        input("Press enter to continue...")
        door()

def krnl():
    os.system("clear")
    code_right = input("But before opening the door you must use the code that was given previously: ")
    if code_right == '4896':
        print("You have opened the door. You are now free")
        good_end()
    else: 
        caught()
        
def caught():
        os.system("clear")
        print("""
            
░█████╗░░█████╗░██╗░░░██╗░██████╗░██╗░░██╗████████╗
██╔══██╗██╔══██╗██║░░░██║██╔════╝░██║░░██║╚══██╔══╝
██║░░╚═╝███████║██║░░░██║██║░░██╗░███████║░░░██║░░░
██║░░██╗██╔══██║██║░░░██║██║░░╚██╗██╔══██║░░░██║░░░
╚█████╔╝██║░░██║╚██████╔╝╚██████╔╝██║░░██║░░░██║░░░
░╚════╝░╚═╝░░╚═╝░╚═════╝░░╚═════╝░╚═╝░░╚═╝░░░╚═╝░░░
            """)
        print("the code you provided is incorrect\n")
        print("The guard catch up to you and caught you....")
        input("Press enter to continue...")
        bad_end()
    
def scramble():
    os.system("clear")
    print("""
    
░██████╗░█████╗░██████╗░░█████╗░███╗░░░███╗██████╗░██╗░░░░░███████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗████╗░████║██╔══██╗██║░░░░░██╔════╝
╚█████╗░██║░░╚═╝██████╔╝███████║██╔████╔██║██████╦╝██║░░░░░█████╗░░
░╚═══██╗██║░░██╗██╔══██╗██╔══██║██║╚██╔╝██║██╔══██╗██║░░░░░██╔══╝░░
██████╔╝╚█████╔╝██║░░██║██║░░██║██║░╚═╝░██║██████╦╝███████╗███████╗
╚═════╝░░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░░░░╚═╝╚═════╝░╚══════╝╚══════╝
        """)
# List of words to choose from
    words = ["paper", "bookshelf", "dangerous", "deadzone", "key"]
    answer = random.choice(words)
    scrambled = ''.join(random.sample(answer, len(answer)))
    guess = input("Unscramble the word: " + scrambled + " ")
    guesses = 1

# Loop until user guesses correctly
    while guess != answer:
        print("Incorrect. Try again.")
        guess = input("Unscramble the word: " + scrambled + " ")
        guesses += 1

# Print message when user guesses correctly
    print("Congratulations! You unscrambled the word in", guesses, "tries.")
    print("As you unscramble a word you see the following word is a hint to escaping this room.")
    input("Press enter to continue...")
    game_menu()
        

    
def window():
    os.system("clear")
    print(
        """

░██╗░░░░░░░██╗██╗███╗░░██╗██████╗░░█████╗░░██╗░░░░░░░██╗
░██║░░██╗░░██║██║████╗░██║██╔══██╗██╔══██╗░██║░░██╗░░██║
░╚██╗████╗██╔╝██║██╔██╗██║██║░░██║██║░░██║░╚██╗████╗██╔╝
░░████╔═████║░██║██║╚████║██║░░██║██║░░██║░░████╔═████║░
░░╚██╔╝░╚██╔╝░██║██║░╚███║██████╔╝╚█████╔╝░░╚██╔╝░╚██╔╝░
░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚══╝╚═════╝░░╚════╝░░░░╚═╝░░░╚═╝░░
        """)
    print("You choose to search the window:")
    print("You look out the window and see a dead field of grass and decaying trees trying to hold themselves.")
    print("You try to open the window but realize that the window is welded on.")
    print("This lowers your motivation, and puts you into a bad mood. Back to search the room further.\n")
    charecter_status["mood"] = "bad"
    input("Press enter to continue...")
    game_menu()
    
def notebook():
    os.system("clear")
    print("""
    
███████╗░██████╗░██╗░░░██╗░█████╗░████████╗██╗░█████╗░███╗░░██╗
██╔════╝██╔═══██╗██║░░░██║██╔══██╗╚══██╔══╝██║██╔══██╗████╗░██║
█████╗░░██║██╗██║██║░░░██║███████║░░░██║░░░██║██║░░██║██╔██╗██║
██╔══╝░░╚██████╔╝██║░░░██║██╔══██║░░░██║░░░██║██║░░██║██║╚████║
███████╗░╚═██╔═╝░╚██████╔╝██║░░██║░░░██║░░░██║╚█████╔╝██║░╚███║
╚══════╝░░░╚═╝░░░░╚═════╝░╚═╝░░╚═╝░░░╚═╝░░░╚═╝░╚════╝░╚═╝░░╚══╝
    """)
    print("You chose to pick up the notebook and read it\nupon reading it you see a text pop up.")
    input("Press enter to continue...")
    x = random.randint(1, 10)
    y = random.randint(1, 10)
    operators = ["+", "-", "*", "/"]
    operator = random.choice(operators)
    equation = str(x) + " " + operator + " " + str(y)
    answer = input("Solve the equation: " + equation + " = ")
    attempts = 1
    while eval(equation) != int(answer):
        print("Incorrect. Try again.")
        answer = input("Solve the equation: " + equation + " = ")
        attempts += 1
    print("Congratulations! You solved the equation in", attempts, "attempts.")
    print(" As you solve the question you see the answer is the exact number as the detective who questioned you.")
    print("Strange isn't it.......There must be something behind this.")
    input("Press enter to continue...")
    game_menu()
    
def tablet():
    os.system("clear")

    print(
        """

████████╗░█████╗░██████╗░██╗░░░░░███████╗████████╗
╚══██╔══╝██╔══██╗██╔══██╗██║░░░░░██╔════╝╚══██╔══╝
░░░██║░░░███████║██████╦╝██║░░░░░█████╗░░░░░██║░░░
░░░██║░░░██╔══██║██╔══██╗██║░░░░░██╔══╝░░░░░██║░░░
░░░██║░░░██║░░██║██████╦╝███████╗███████╗░░░██║░░░
░░░╚═╝░░░╚═╝░░╚═╝╚═════╝░╚══════╝╚══════╝░░░╚═╝░░░     
                                                            
        """
    )

    if charecter_status["mood"] == "bad" or charecter_status["mood"] == "neutral":
        print("You're in a bad mood. You don't want to search the tablet.")
        print("Maybe a good book from the bookshelf might help?")
        input("Press enter to continue...")
        game_menu()
    else:
        print("You choose to search the tablet:")
        print("You find a tablet on the table. You turn it on and see that it is locked with a password")
        password = input("Enter the 4-number password:")
        if password == '4896':
            print("You have unlocked the laptop.")
            print("You're faced with a firewall")
            print("It's asking you to play a game")
            game_key = input("Do you want to play the game? (y/n)")
            if game_key == 'y':
                num = random.randint(1,10)
                os.system("clear")
                print("""

░██████╗░██╗░░░██╗███████╗░██████╗░██████╗██╗███╗░░██╗░██████╗░
██╔════╝░██║░░░██║██╔════╝██╔════╝██╔════╝██║████╗░██║██╔════╝░
██║░░██╗░██║░░░██║█████╗░░╚█████╗░╚█████╗░██║██╔██╗██║██║░░██╗░
██║░░╚██╗██║░░░██║██╔══╝░░░╚═══██╗░╚═══██╗██║██║╚████║██║░░╚██╗
╚██████╔╝╚██████╔╝███████╗██████╔╝██████╔╝██║██║░╚███║╚██████╔╝
░╚═════╝░░╚═════╝░╚══════╝╚═════╝░╚═════╝░╚═╝╚═╝░░╚══╝░╚═════╝░               
\n""")
                print("You started the game")
                print("It's a game of guess the number:")
                print("You have 5 chances to guess the number")
                print("The number is between 1 and 10")
                for i in range(5):
                    guess = int(input("Guess the number:"))
                    if guess == num:
                        print("You guessed the number correctly")
                        print("The screen goes black and says: 'Are you hungry?'")
                        print("Maybe it means something?")
                        input("Press enter to continue...")
                        game_menu()
                    elif guess > num:
                        print("Your guess is too high")
                    elif guess < num:
                        print("Your guess is too low")
            else:
                print("You choose not to play the game")
                print("The laptop shuts down")
                input("Press enter to continue...")
                game_menu()
        else:
            print("You have entered the wrong password")
            print("The laptop shuts down")
            input("Press enter to continue...")
            game_menu()
    input("Press enter to continue...")
            

def bookshelf():
    os.system("clear")
    print(
        """

██████╗░░█████╗░░█████╗░██╗░░██╗░██████╗██╗░░██╗███████╗██╗░░░░░███████╗
██╔══██╗██╔══██╗██╔══██╗██║░██╔╝██╔════╝██║░░██║██╔════╝██║░░░░░██╔════╝
██████╦╝██║░░██║██║░░██║█████═╝░╚█████╗░███████║█████╗░░██║░░░░░█████╗░░
██╔══██╗██║░░██║██║░░██║██╔═██╗░░╚═══██╗██╔══██║██╔══╝░░██║░░░░░██╔══╝░░
██████╦╝╚█████╔╝╚█████╔╝██║░╚██╗██████╔╝██║░░██║███████╗███████╗██║░░░░░
╚═════╝░░╚════╝░░╚════╝░╚═╝░░╚═╝╚═════╝░╚═╝░░╚═╝╚══════╝╚══════╝╚═╝░░░░░        
        """
    )                                                                 
    print("You choose to search the bookshelf:")
    print("You find a book on the bookshelf. You see a ton of books on the bookshelf.")
    print("Here are some of the books:")
    # Print the list of books
    for i in list_of_books:
        print(i)
    book = input("Which book do you want to read?:")
    if book == '1918':
        os.system("clear")
        print(
        """
   __     ______     __     ______  
 _/  |   /      \  _/  |   /      \ 
/ $$ |  /$$$$$$  |/ $$ |  /$$$$$$  |
$$$$ |  $$ \__$$ |$$$$ |  $$ \__$$ |
  $$ |  $$    $$ |  $$ |  $$    $$< 
  $$ |   $$$$$$$ |  $$ |   $$$$$$  |
 _$$ |_ /  \__$$ | _$$ |_ $$ \__$$ |
/ $$   |$$    $$/ / $$   |$$    $$/ 
$$$$$$/  $$$$$$/  $$$$$$/  $$$$$$/  

        """)
        print("You read the book. Its a pretty good book.")
        print("Your mood gets better.")
        charecter_status["mood"] = "good"
        print("However, you realize that the number 4896 is written on the last page of the book.")
        print("Maybe it means something?")
        input("Press enter to continue...")
        game_menu()
    elif book != '1984':
        print("YOu look into the book but you see nothing but blank pages....")
        print("could that be something strange??")
        input("\nPress enter to continue...")
        print("\nThe guards caught you......")
        game_menu()

def powerhouse():
    os.system("clear")
    print(
        """

██████╗░░█████╗░░██╗░░░░░░░██╗███████╗██████╗░  ██╗░░██╗░█████╗░██╗░░░██╗░██████╗███████╗
██╔══██╗██╔══██╗░██║░░██╗░░██║██╔════╝██╔══██╗  ██║░░██║██╔══██╗██║░░░██║██╔════╝██╔════╝
██████╔╝██║░░██║░╚██╗████╗██╔╝█████╗░░██████╔╝  ███████║██║░░██║██║░░░██║╚█████╗░█████╗░░
██╔═══╝░██║░░██║░░████╔═████║░██╔══╝░░██╔══██╗  ██╔══██║██║░░██║██║░░░██║░╚═══██╗██╔══╝░░
██║░░░░░╚█████╔╝░░╚██╔╝░╚██╔╝░███████╗██║░░██║  ██║░░██║╚█████╔╝╚██████╔╝██████╔╝███████╗
╚═╝░░░░░░╚════╝░░░░╚═╝░░░╚═╝░░╚══════╝╚═╝░░╚═╝  ╚═╝░░╚═╝░╚════╝░░╚═════╝░╚═════╝░╚══════╝                                   ░                                      
        """
    )
    print("You choose to search the power generator:")
    # Create a small puzzle
    print("You see a power generator. You walk towards it and see a small quarter on the front of the generator.")
    print("Despite that you know that if you disable the power generator it'll be a much more easier escape, you decide to take the quarter and play a game of chance.\n")
    print("You know that your fate lies on these 3 tries wheather you make it out or not.")
    print("You have 3 tries.")
    print("You have to flip a coin 3 times.")
    print("If you get 2 tails or tails, you win.\n")
    print("Or else...\n")
    print("YOU DIE\n")
    print("""
           
     ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⣀⣀⣀⣀⡀⢀⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⣷⡀⢿⣿⣷⡀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⡿⠿⠿⠿⠿⢿⣿⣧⠈⢿⣿⣿⡄⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⣤⣤⣤⣤⣤⣼⣿⣿⣧⠈⢿⣿⣿⡄⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣦⣤⣤⣤⣤⣼⣿⣿⣿⡇⢈⣉⣉⣉⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⢸⣿⣿⡏⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠀⣿⣿⣿⠃⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⢰⣿⣿⡟⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⣼⣿⣿⠇⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⢀⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⢸⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⣿⣿⣿⣿⣿⣿⠃⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⡿⠀⣿⣿⡏⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⡇⢸⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠛⠛⠛⠛⠛⠛⠀⠘⠛⠛⠀⠀⠀⠀⠀⠀⠀⠀⠀
    """)
    puzzle = input("Would you like to play?(y/n)")
    if puzzle == 'y':
        os.system("clear")
        # Create a list of the possible outcomes
        possible_outcomes = ['heads', 'tails']
        # Create a list of the outcomes
        outcomes = []
        # Create a list of the outcomes and print them slowly
        for i in range(3):
            outcomes.append(random.choice(possible_outcomes))
            print(outcomes)
            time.sleep(1)
        # Print the outcomes
        print(outcomes)
        # Check if the user got the answer right
        if outcomes.count('tails') == 2:
            os.system("clear")
            print("Luck is on your side!")
            print("You get a key.")
            print("You look around and you find...")
            input("Press enter to continue...")
            os.system("clear")
            print("nothing. . .\n")
            input("Press enter to continue...")
        else:
            print("Luck was not on your side.")
            print("You died to an explosion while playing with your quarter.")
            print("You die....")
            bad_end()
    elif puzzle == 'n':
        os.system("clear")
        print("You decide not to play the game of chance.")
        print("You decide to leave the powerhouse alone.")
        input("Press enter to continue...")
        game_menu()
    else:
        os.system("clear")
        print("Please enter a valid input.")
        input("Press enter to continue...")
        powerhouse()


def piecepaper():
    os.system("clear")
    print(
        """ 

██████╗░░█████╗░██████╗░███████╗██████╗░
██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗
██████╔╝███████║██████╔╝█████╗░░██████╔╝
██╔═══╝░██╔══██║██╔═══╝░██╔══╝░░██╔══██╗
██║░░░░░██║░░██║██║░░░░░███████╗██║░░██║
╚═╝░░░░░╚═╝░░╚═╝╚═╝░░░░░╚══════╝╚═╝░░╚═╝
                                                """
    )
    print("You choose to search the piece of paper on the floor that the detective left:")
    print("YOu quickly read whats on the paper on the floor. As you continue reading you find in that letter it was your coworkers telling you the passcode which is 9980 and they key attached to that letter.")
    print("You feel a bit better.")
    print("You find a key inside the paper. You take the key.")
    charecter_status["key_status"] = True
    charecter_status["mood"] = "neutral"
    
    input("Press enter to continue...")
    game_menu()

def picture():
    os.system("clear")
    print(
        """
     
███████╗░█████╗░███╗░░░███╗██╗██╗░░░░░██╗░░░██╗  ██████╗░██╗░█████╗░████████╗██╗░░░██╗██████╗░███████╗
██╔════╝██╔══██╗████╗░████║██║██║░░░░░╚██╗░██╔╝  ██╔══██╗██║██╔══██╗╚══██╔══╝██║░░░██║██╔══██╗██╔════╝
█████╗░░███████║██╔████╔██║██║██║░░░░░░╚████╔╝░  ██████╔╝██║██║░░╚═╝░░░██║░░░██║░░░██║██████╔╝█████╗░░
██╔══╝░░██╔══██║██║╚██╔╝██║██║██║░░░░░░░╚██╔╝░░  ██╔═══╝░██║██║░░██╗░░░██║░░░██║░░░██║██╔══██╗██╔══╝░░
██║░░░░░██║░░██║██║░╚═╝░██║██║███████╗░░░██║░░░  ██║░░░░░██║╚█████╔╝░░░██║░░░╚██████╔╝██║░░██║███████╗
╚═╝░░░░░╚═╝░░╚═╝╚═╝░░░░░╚═╝╚═╝╚══════╝░░░╚═╝░░░  ╚═╝░░░░░╚═╝░╚════╝░░░░╚═╝░░░░╚═════╝░╚═╝░░╚═╝╚══════╝                                         
        """
    )
    print("You choose to search the picture:")
    print("You find a family picture on the wall.")
    print("It seems like the picture looks like the someone who looks like the detective.")
    print("You see a date on the picture. You take a closer look and see that the date is 1918")
    print("Maybe it means something?")
    input("Press enter to continue...")
    game_menu()

def puzzle():
    os.system("clear")
    print("""
 
███╗░░░███╗██╗░░░██╗░██████╗████████╗███████╗██████╗░██╗░░░██╗
████╗░████║╚██╗░██╔╝██╔════╝╚══██╔══╝██╔════╝██╔══██╗╚██╗░██╔╝
██╔████╔██║░╚████╔╝░╚█████╗░░░░██║░░░█████╗░░██████╔╝░╚████╔╝░
██║╚██╔╝██║░░╚██╔╝░░░╚═══██╗░░░██║░░░██╔══╝░░██╔══██╗░░╚██╔╝░░
██║░╚═╝░██║░░░██║░░░██████╔╝░░░██║░░░███████╗██║░░██║░░░██║░░░
╚═╝░░░░░╚═╝░░░╚═╝░░░╚═════╝░░░░╚═╝░░░╚══════╝╚═╝░░╚═╝░░░╚═╝░░░  
    """)
    print("You choose to search the puzzles:")
    print("Here 2 puzzles that you can choose from.")
    puzzle = input("Would you like to play a puzzle? (y/n): ")
    if puzzle == 'y':
        os.system("clear")
        puzzle = input("Which puzzle would you like to play? (1/2: ")
        if puzzle == '1':
            rsp()
        elif puzzle == '2':
            hangman()
        else:
             print("Please enter a valid input.")
             game_menu()


def bad_end():
    os.system("clear")
    print(
        """
        
██████╗░███████╗░█████╗░██████╗░
██╔══██╗██╔════╝██╔══██╗██╔══██╗
██║░░██║█████╗░░███████║██║░░██║
██║░░██║██╔══╝░░██╔══██║██║░░██║
██████╔╝███████╗██║░░██║██████╔╝
╚═════╝░╚══════╝╚═╝░░╚═╝╚═════╝░
        """)
    print("Luck was not on your side...")
    print("You have died")
    exit()

def good_end():
    os.system("clear")
    print(
    """
    
██╗░░░██╗░█████╗░██╗░░░██╗  ███████╗░██████╗░█████╗░░█████╗░██████╗░███████╗██████╗░
╚██╗░██╔╝██╔══██╗██║░░░██║  ██╔════╝██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗
░╚████╔╝░██║░░██║██║░░░██║  █████╗░░╚█████╗░██║░░╚═╝███████║██████╔╝█████╗░░██║░░██║
░░╚██╔╝░░██║░░██║██║░░░██║  ██╔══╝░░░╚═══██╗██║░░██╗██╔══██║██╔═══╝░██╔══╝░░██║░░██║
░░░██║░░░╚█████╔╝╚██████╔╝  ███████╗██████╔╝╚█████╔╝██║░░██║██║░░░░░███████╗██████╔╝
░░░╚═╝░░░░╚════╝░░╚═════╝░  ╚══════╝╚═════╝░░╚════╝░╚═╝░░╚═╝╚═╝░░░░░╚══════╝╚═════╝░
    """)
    print("You have completed the game")
    exit()
 

def game_menu():
    os.system("clear")
    print("""

███╗░░░███╗███████╗███╗░░██╗██╗░░░██╗
████╗░████║██╔════╝████╗░██║██║░░░██║
██╔████╔██║█████╗░░██╔██╗██║██║░░░██║
██║╚██╔╝██║██╔══╝░░██║╚████║██║░░░██║
██║░╚═╝░██║███████╗██║░╚███║╚██████╔╝
╚═╝░░░░░╚═╝╚══════╝╚═╝░░╚══╝░╚═════╝░    
                                      
    """)
    print("You find yourself in a dark and creepy room. What are you searching for? :")
    print("""
    Door with and exit sign[d]
    Window[w]
    tablet[t]
    Bookshelf[b]
    power generator[p]
    A small folded piece of paper on the floor [sp]
    Picture on the wall[pic]
    Puzzles[puzzle]
    Scrambler[s]
    notebook[n]
    """)
    ans = input("What do you want to search?:")
    if ans == 'd':
        door()
    elif ans == 'w':
        window()
    elif ans == 't':
        tablet()
    elif ans == 'b':
        bookshelf()
    elif ans == 'p':
        powerhouse()
    elif ans == 'sp':
        piecepaper()
    elif ans == 'pic':
        picture()
    elif ans == 'puzzle':
        puzzle()
    elif ans == 's':
        scramble()
    elif ans == 'n':
        notebook()
    else:
        print("Invalid input")
        game_menu()

if menu_ans == 's':
    os.system("clear")
    game_menu()
elif menu_ans == 'q':
    print("You quit the game")
    exit()
