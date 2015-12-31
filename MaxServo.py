import Servo
import time

dyn = Servo.USB2Dynamixel_Device( '/dev/ttyUSB0', 57600 )
test_servo = Servo.Robotis_Servo( dyn, 1 )

test_servo.init_cont_turn()
#test_servo.kill_cont_turn()

vel = 2.0

while True:
    vel = vel * -1
    test_servo.set_angvel(vel)
    for x in range(0, 5) :
        print test_servo.read_angle()
        time.sleep(1)
