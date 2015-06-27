### Scanning for Servos
After setting up the circuits and connecting the servos to your computer using the usb module, you can proceed to check if the servos are detected. To do this,

1. Open the terminal
2. Change directory into the open_robotics_grasper directory
3. Find the id of your usb device connected by running: <code>ls /dev/tty.usbserial* </code>
4. If using the AX Servo series, run: <code>python Servo.py -d /dev/ttyUSB0 --baud 1000000 --scan <\code>. If not, run: <code>python Servo.py -d /dev/ttyUSB0 --scan <\code>
