let start: number;
//  Python3
//  Movement test of direction and speed
//  Movement functions
function move_stop(): any[] {
    xgo.execution_action(xgo.action_enum.Default_posture)
    return []
}

function move_forward(spd: number = 50): any[] {
    //  input speed 
    xgo.move_xgo(xgo.direction_enum.Forward, spd)
    return []
}

function move_back(spd: number = 50): any[] {
    //  input speed 
    xgo.move_xgo(xgo.direction_enum.Backward, spd)
    return []
}

function turn_left(sec: number = 2): any[] {
    //  input time in seconds
    xgo.rotate_angle_continue(xgo.rotate_direction_enum.turn_left, 60, sec)
    return []
}

function turn_right(sec: number = 2): any[] {
    //  input time in seconds
    xgo.rotate_angle_continue(xgo.rotate_direction_enum.turn_right, 60, sec)
    return []
}

function timed_forward(spd: number = 50, sec: number = 2.5): any[] {
    xgo.move_xgo(xgo.direction_enum.Forward, spd)
    let milisec = sec * 1000
    basic.pause(milisec)
    move_stop()
    return []
}

function timed_back(spd: number = 50, sec: number = 2.5): any[] {
    xgo.move_xgo(xgo.direction_enum.Backward, spd)
    let milisec = sec * 1000
    basic.pause(milisec)
    move_stop()
    return []
}

//  Initialise communication between Microbit and XGO
xgo.init_xgo_serial(SerialPin.P14, SerialPin.P13)
while (true) {
    //  Show ready at power on
    basic.showIcon(IconNames.Happy)
    //  Microbit program running
    basic.pause(1000)
    if (start == 0) {
        xgo.execution_action(xgo.action_enum.Sit_down)
        //  XGO connection successful
        start = 1
    }
    
    //  Test sequence on logo touch
    if (input.logoIsPressed()) {
        move_stop()
        //  speed test
        for (let test of [16, 50, 90]) {
            // xgo.move_xgo(xgo.speed_enum.test)
            timed_forward(test)
            timed_back(test)
        }
        turn_left(5)
        turn_right(6)
        move_stop()
    }
    
}
