drive_motor = "6_5169793973449801317"
servo = "????"

# Set SERVO based on robot info

def autonomous_setup():
    print ("Autonomous mode has started!")
    Robot.set_value(drive_motor,"pid_enabled_a", False)
    Robot.set_value(drive_motor,"pid_enabled_b", False)
    Robot.run(autonomous_actions)

def autonomous_main():
    pass

def autonomous_actions():
    print ("Autonomous action sequence started")
    print ("1 second has passed in autonomous mode")
    Robot.set_value(drive_motor, "velocity_a", -0.5)
    Robot.set_value(drive_motor, "velocity_b", -0.5)
    
def full_speedahead(lv,rv):
    PWR = 10
    Robot.set_value(drive_motor, "velocity_a", -lv * PWR)
    Robot.set_value(drive_motor, "velocity_b", rv * PWR)
    
def teleop_setup():
    print ("Tele-operated mode has started!")

def teleop_main():
    right_y = Gamepad.get_value("joystick_right_y")
    right_x = Gamepad.get_value("joystick_right_x")
    
    # this doesn't seem to work
    Robot.set_value(servo, "servo0", 1)
    
    if abs(right_y)<0.1 and abs(right_x) < 0.1:
        full_speedahead(0,0)

    if right_y <= 0:
        if right_x <= 0:
            #we're in upper left quadrant
            full_speedahead(-right_y+right_x,-right_y)
        elif right_x >= 0:
            #upper right quadrant
            full_speedahead(-right_y,-right_y-right_x)
    elif right_y >= 0:
        if right_x <= 0:
            #lower left quadrant
            full_speedahead(-right_y-right_x,-right_y)
        elif right_x >= 0:
            full_speedahead(-right_y,-right_y+right_x)
        
       # Robot.set_value(motor_id, "velocity_a", -0.5)
        #Robot.set_value(motor_id, "velocity_b", -0.5)
    else:
        full_speedahead(0,0)
 
        
        #velocity_b connects to Out2 on motor controller


