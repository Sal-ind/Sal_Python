Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def play(player_choice):
...     computer_choice = random.choice(choices)
...     result = determine_winner(player_choice, computer_choice)
...     result_text.value = f"Computer chose {computer_choice}\n{result}"
... 
... def determine_winner(player_choice, computer_choice):
...     if player_choice == computer_choice:
...         return "It's a tie!"
...     elif (player_choice == "Rock" and computer_choice == "Scissors") or \
...          (player_choice == "Paper" and computer_choice == "Rock") or \
...          (player_choice == "Scissors" and computer_choice == "Paper"):
...         return "You win!"
...     else:
...         return "Computer wins!"
... 
... app = App("Rock, Paper, Scissors", width=300, height=200)
... 
... choices = ["Rock", "Paper", "Scissors"]
... 
... instruction_text = Text(app, text="Select your choice:")
... result_text = Text(app, text="")
... button_box = Box(app, layout="grid")
... 
... for i, choice in enumerate(choices):
...     button = PushButton(button_box, command=play, args=[choice], text=choice, grid=[i, 0])
... 
... app.display()
