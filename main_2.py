from spike import PrimeHub, LightMatrix, Button, StatusLight, ForceSensor, MotionSensor, Speaker, ColorSensor, App, DistanceSensor, Motor, MotorPair
from spike.control import wait_for_seconds, wait_until, Timer

# declare the hardware attached to the robot
hub = PrimeHub()
color = ColorSensor('A')
motors = MotorPair('F', 'B')

# parameters, adjust as necessary
lo_light = 25 # average amount of light next to line
hi_light = 90 # average amount of light on the line
turn_max = 5 # tightness of turning, less values drive straighter

# turn and find the line
# while(color.get_reflected_light() < hi_light - 3):
  #  motors.start_at_power(66, -25)

# stop the motors from the previous operation
# motors.stop()

# scales an input to the specified bounds
# essentially an y = mx + b equation
def scale(amt):
    in_min=lo_light
    in_max=hi_light
    out_min = -turn_max
    out_max = turn_max
    return (amt - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

# main loop, replace True with your condition for stopping
while(True):
    # calculate turn amount based on light value
    color_amt = color.get_reflected_light()
    turn_amt = 0
    if color_amt > 90:
        turn_amt = -40
    
        # move the motors at 50% power and the specified turning amount
    # drives without a set distance so that it does not jerk while moving
    motors.start_at_power(30, int(turn_amt)) # cast turn_amt to int

    color_amt_2 = color.get_reflected_light()
    if color_amt_2 < 90:
        turn_amt = 50

    # move the motors at 50% power and the specified turning amount
    # drives without a set distance so that it does not jerk while moving
    motors.start_at_power(30, int(turn_amt)) # cast turn_amt to int

    # print values to SPIKE App console for debugging
    print('Color input: {} | Turn amount: {}'.format(color_amt, turn_amt))
