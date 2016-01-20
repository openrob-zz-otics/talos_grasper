from Servo import *
import math
import time
import sys
import os

#sys.stdout.write("USB serial devices found:\n")
#os.system("ls /dev/*[uU][sS][bB]*")
#sys.stdout.write("Choose the dev_name for Arm Servo: ")
#dev_name = raw_input()

dyn = USB2Dynamixel_Device("COM26", 57600)

#print find_servos(dyn)
#recover_servo(dyn)

#servo 2 forearm, servo 5 elbow
serv_2 = Robotis_Servo(dyn, 2)
serv_5 = Robotis_Servo(dyn ,5)

sleeptime = 5
speed = 2

serv_5.set_angvel(0.5)
serv_5.set_cw_limit(800)
serv_5.set_ccw_limit(2800)
print "Elbow encoder " + str(serv_5.read_encoder())

serv_2.set_angvel(0.5)
serv_2.set_cw_limit(1)
serv_2.set_ccw_limit(4095)
print "Forearm encoder " + str(serv_2.read_encoder())
print "Multi-turn offset" + str(serv_2.read_multi_offset())

print "Enter servo value: "
keys_in = raw_input()
while(str(keys_in) != 'q'):
	serv_2.move_to_encoder(int(keys_in))
	#serv_2.set_multi_offset(0)#int(keys_in))
	serv_5.move_to_encoder((1800 - int(keys_in)) / 2 + 1800)
	keys_in = raw_input()

#print serv.recieve_reply()
