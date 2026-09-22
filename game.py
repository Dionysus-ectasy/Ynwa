import random

choices = ["rock", "paper", "scissors"]
wins = {"rock": "scissors", "paper": "rock", "scissors": "paper"}
Emojis = {"rock": "🪨", "paper": "📄", "scissors": "✂️"}
player_score = 0
computer_score = 0

print("Rock, Paper, Scissors! Type 'quit' to stop. ")

while True:
    player = input("Your move: ").lower().strip()
    
    if player == "quit":
        break
    if player not in choices:
        print("choose rock, paper, or scissors.")
        continue
    
    computer = random.choice(choices)
    print(f"You {Emojis[player]}  vs Computer {Emojis[computer]}")
    
    if player == computer:
        print("It's a tie")
    elif wins[player] == computer:
        print("You win this round!")
        player_score += 1
    else:
        print("Computer wins this round.")
        computer_score += 1
    print(f"Score: You {player_score} - {computer_score} Computer")
print("Thanks for playing")