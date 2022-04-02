import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
turt = turtle.Turtle()


def position(x,y):
    turt.hideturtle()
    turt.penup()
    turt.goto(x,y)
    turt.write(arg=answer_state)




states = pd.read_csv("50_states.csv")
state_name = states['state'].to_list()
answer_list = []
flag = True

while flag:
    answer_state= screen.textinput(f"{len(answer_list)}/50 Correct Guesses", prompt = "What's another state's name?").title()
    
    if answer_state in answer_list:
        continue
    elif answer_state in state_name:
        answer_list.append(answer_state)
        state_d = states[states.state== answer_state]              
        position(int(state_d.x),int(state_d.y)) 
    if answer_state == 'Exit' :
        flag = False
    if len(answer_list) ==49:
        flag = False
    
missed_states =[]
for state in state_name:
    if state not in answer_list:
        missed_states.append(state)
        
pd.DataFrame(missed_states).to_csv("States_to_learn.csv")   

