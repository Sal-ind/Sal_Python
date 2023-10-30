from guizero import App, PushButton
import random

def move_button():
    new_x = random.randint(0, app.width - button.width)
    new_y = random.randint(0, app.height - button.height)
    button.move(new_x, new_y)

def increase_score():
    global score
    score += 1
    score_text.value = "Score: {}".format(score)
    move_button()

app = App("Click the Button Game", width=400, height=400)

button = PushButton(app, text="Click me!", command=increase_score)
score_text = PushButton(app, text="Score: 0", enabled=False)

score = 0
move_button()

app.display()
