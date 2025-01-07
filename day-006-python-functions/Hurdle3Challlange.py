'''
https://www.reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%203&url=worlds%2Ftutorial_en%2Fhurdle3.json
'''

#used only as placeholder function
def move():
    pass

#used only as placeholder function
def turn_left():
    pass 

#used only as placeholder function
def wall_in_front():
    pass 

#used only as placeholder function
def at_goal():
    pass 

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
    
while not at_goal():
    if wall_in_front():
        jump()
    else:
        move()
