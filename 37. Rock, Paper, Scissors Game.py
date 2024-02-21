import random

while True:
    choice = ["rock","paper","scissors"]

    computer = random.choice(choice)                            # Wir sagen dem Computer, dass er zu Zufälliges aus der Liste "choice" entnehmen soll
    player = None 

    while player not in choice:                                 # Falls was anderes als "Rock, Paper, Scissors" geschrieben wird
        player = input("rock, paper, or scissors?: ").lower()   # Damit Klein- und Großbuchstaben erkannt werden

    if player == computer:                                                              # Gleichstand                
        print("Computer: ",computer)
        print("Player: ",player)
        print("Tie!")
    elif player == "rock":              
        if computer == "paper":                                                         # Player hat Stein, Computer hat Papier
            print("Computer: ",computer)
            print("Player: ",player)
            print("You lose!") 
        if computer == "scissors":                                                      # Player hat Stein, Computer hat Schere
            print("Computer: ",computer)
            print("Player: ",player)
            print("You win!")
    elif player == "scissors":          
        if computer == "rock":                                                          # Player hat Schere, Computer hat Stein
            print("Computer: ",computer)
            print("Player: ",player)
            print("You lose!") 
        if computer == "paper":                                                         # Player hat Schere, Computer hat Papier
            print("Computer: ",computer)
            print("Player: ",player)
            print("You win!")
    elif player == "paper":          
        if computer == "scissors":                                                      # Player hat Papier, Computer hat Schere
            print("Computer: ",computer)
            print("Player: ",player)
            print("You lose!") 
        if computer == "rock":                                                          # Player hat Papier, Computer hat Stein
            print("Computer: ",computer)
            print("Player: ",player)
            print("You win!")

    play_again = input("Play again (yes/no): ").lower()

    if play_again != "yes":
        break

print("Okay, Bye!")