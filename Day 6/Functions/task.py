#1 example
def my_function():
    print("Hello")
    print("Bye")

my_function()

#2 example
def user_name():
    name=input("What is your name?")
    print("Hello," + name)

print("Hello")
user_name()

#for loop and while loop in Reeborg game
#for loop
for step in range(6):
    path()
#whole loop
number_of_hurdles = 6
while number_of_hurdles > 0:
    path()
    number_of_hurdles -= 1
    print(number_of_hurdles)
#for hurdle 2
while not at_goal: # or we can use while at_goal != True
    path()
#for hurdle 3
#also remove 1st line in path()
while not at_goal():
    if  wall_in_front():
        path()
    else:
        move()
#for hurdle 4
def jump():
    turn_left()
    while wall_on_right():
        move()
    turn_right()
    move()
    turn_right()
    while front_is_clear():
        move()
    turn_left()


while not at_goal():
    if wall_in_front():
        jump()
    else:
        move()
#muze
write turn_right portion only
while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()


#Debugging portion is remaining for to do after 15th session
#video number 50