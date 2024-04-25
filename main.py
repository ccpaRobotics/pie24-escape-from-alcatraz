drive_motor = "6_5169793973449801317"
arm_motor = "6_1121225532052018424"
servo = "4_1833482520634428295"
servo_status = 0
arm_position = 0

def full_speedahead(lv,rv):
    PWR = 10
    Robot.set_value(drive_motor, "velocity_a", -lv * PWR)
    Robot.set_value(drive_motor, "velocity_b", rv * PWR)
    
#def move_arm(direction):
    # global arm_position
    #PWR = 10
    #Robot.set_value(arm_motor, "velocity_b", direction * PWR)
    # if arm_position == 0:
    #     arm_position = 1
    # elif arm_position == 1:
    #     arm_position = 0
    
def teleop_setup():
    global servo_status
    # global arm_position
    servo_status = 0
    arm_position = 0
    #Robot.set_value(arm_motor, "velocity_a", 1.0)
    #Robot.set_value(arm_motor, "velocity_b", 1.0)
    #print(Robot.get_value(arm_motor, "velocity_a"))
    #print(Robot.get_value(arm_motor, "velocity_b"))
    print ("Tele-operated mode has started!")

def teleop_main():
    
    # gripper
    # servo goes 1 to -1
    # if you go to 1.0 u will be sad bc not enough voltage
    global servo_status
    global arm_position
    servo_thing = Robot.get_value(servo,"servo0")
    button_a = Gamepad.get_value("button_a")
    
    if button_a == True and servo_status == 0:
        print("a is pressed")
        Robot.set_value(servo, "servo0", 0.9)
        servo_status = 1
    
    if button_a == False and servo_status == 1:
        print("a is released")
        Robot.set_value(servo, "servo0", -.9)
        servo_status = 0
    
    # arm
    dpad_up = Gamepad.get_value("dpad_up")
    dpad_down = Gamepad.get_value("dpad_down")
    # dpad_left = Gamepad.get_value("dpad_left")
    
    if dpad_up: #and arm_position == 0:
        print("dpad_up pressed")
        print(arm_position)
        Robot.set_value(arm_motor, "velocity_a", 1 * -1.0)
        Robot.set_value(arm_motor, "velocity_b", 1 * -1.0)
        arm_position = 1
        
    elif dpad_down: #and arm_position == 1:
        print("dpad_down pressed")
        print(arm_position)
        Robot.set_value(arm_motor, "velocity_a", 1 * 1.0)
        Robot.set_value(arm_motor, "velocity_b", 1 * 1.0)
        arm_position = 0
        #cannot go below 0

    else:
        Robot.set_value(arm_motor,"velocity_a",0.0)
        Robot.set_value(arm_motor,"velocity_b",0.0)

    # drivetrain
    right_y = Gamepad.get_value("joystick_right_y")
    right_x = Gamepad.get_value("joystick_right_x")
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
        # Robot.set_value(motor_id, "velocity_b", -0.5)

    else:
        full_speedahead(0,0)
        
        #velocity_b connects to Out2 on motor controller
        
# AUTONOMOUS

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
    
