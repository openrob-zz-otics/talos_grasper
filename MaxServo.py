import Servo
import time

dyn = Servo.USB2Dynamixel_Device( 'COM26', 57600 )
test_servo = Servo.Robotis_Servo( dyn, 1 )

test_servo.init_cont_turn()
#test_servo.kill_cont_turn()

while True:
    test_servo.set_angvel(3)
    time.sleep(3)
    test_servo.set_angvel(-3)
    time.sleep(3)   
    