# Python3
# Movement test of direction and speed

# Movement functions

def move_stop():
    xgo.execution_action(xgo.action_enum.Default_posture)
    return()

def move_forward(spd=50): # input speed 
    xgo.move_xgo(xgo.direction_enum.FORWARD, spd)
    return()

def move_back(spd=50): # input speed 
    xgo.move_xgo(xgo.direction_enum.BACKWARD, spd)
    return()

def turn_left(sec=2): # input time in seconds
    xgo.rotate_angle_continue(xgo.rotate_direction_enum.turn_left, 60, sec)
    return()

def turn_right(sec=2): # input time in seconds
    xgo.rotate_angle_continue(xgo.rotate_direction_enum.turn_right, 60, sec)
    return()

def timed_forward(spd=50, sec=2.5):
    xgo.move_xgo(xgo.direction_enum.FORWARD, spd)
    milisec=sec*1000
    basic.pause(milisec)
    move_stop()
    return()

def timed_back(spd=50, sec=2.5):
    xgo.move_xgo(xgo.direction_enum.BACKWARD, spd)
    milisec=sec*1000
    basic.pause(milisec)
    move_stop()
    return()

# Initialise communication between Microbit and XGO
xgo.init_xgo_serial(SerialPin.P14, SerialPin.P13)

while True:
    # Show ready at power on
    basic.show_icon(IconNames.HAPPY) # Microbit program running
    basic.pause(1000)
    if start ==0:
        xgo.execution_action(xgo.action_enum.Sit_down) # XGO connection successful
        start = 1

    # Test sequence on logo touch
    if input.logo_is_pressed():
        move_stop()
        # speed test
        for test in (16, 50, 90): 
            #xgo.move_xgo(xgo.speed_enum.test)
            timed_forward(test)
            timed_back(test)
        turn_left(5)
        turn_right(6)
        move_stop()
    