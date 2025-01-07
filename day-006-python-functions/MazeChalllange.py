'''
https://www.reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json
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
def wall_on_right():
    pass 

#used only as placeholder function
def front_is_clear():
    pass 

#used only as placeholder function
def right_is_clear():
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
    while wall_on_right():
        move()
    turn_right()
    move()
    turn_right()
    move()
    while front_is_clear():
        move()
    turn_left()
    
while not at_goal():
   if right_is_clear():
       turn_right()
       move()
       continue
        
   if front_is_clear():
       move()
       continue

   turn_left()
