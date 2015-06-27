### Scanning for Servos
After setting up the circuits and connecting the servos to your computer using the usb module, you can proceed to check if the servos are detected. To do this,

1. Open the terminal
2. Change directory into the open_robotics_grasper directory
3. Find the id of your usb device connected by running: 'ls /dev/tty.usbserial*'
4. If using the AX Servo series, run:
'''
     python Servo.py -d /dev/[YOUR_USB_DEVICE] --baud 1000000 --scan
'''
 If not, run:
'''
     python Servo.py -d /dev/[YOUR_USB_DEVICE] --scan 
'''
