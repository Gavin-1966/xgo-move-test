# Python3
# Movement test of direction and speed

# Movement functions

def move_stop():
    xgo.execution_action(xgo.action_enum.Default_posture)
    return()

def move_forward(spd=50): # input speed 
    xgo.move_xgo(xgo.direction_enum.Forward, spd)
    return()

def move_back(spd=50): # input speed 
    xgo.move_xgo(xgo.direction_enum.Backward, spd)
    return()

def turn_left(sec=2): # input time in seconds
    xgo.rotate_angle_continue(xgo.rotate_direction_enum.turn_left, 60, sec)
    return()

def turn_right(sec=2): # input time in seconds
    xgo.rotate_angle_continue(xgo.rotate_direction_enum.turn_right, 60, sec)
    return()

def timed_forward(spd=50, sec=2.5):
    xgo.move_xgo(xgo.direction_enum.Forward, spd)
    milisec=sec*1000
    basic.pause(milisec)
    return()

def timed_back(spd=50, sec=2.5):
    xgo.move_xgo(xgo.direction_enum.Backward, spd)
    milisec=sec*1000
    basic.pause(milisec)
    return()

# Initialise communication between Microbit and XGO
xgo.init_xgo_serial(SerialPin.P14, SerialPin.P13)
xgo.execution_action(xgo.action_enum.Sit_down) # demonstrates connection sucessful

while True:
    # Test sequence on logo touch
    if input.logo_is_pressed():
        move_stop()
        timed_forward()
        timed_back()
        turn_left()
        turn_right()
        move_stop()
    