### Scanning for Servos
After setting up the circuits and connecting the servos to your computer using the usb module, you can proceed to check if the servos are detected. To do this,

1. Open the terminal
2. Change directory into the open_robotics_grasper directory
3. Find the id of your usb device connected by running: 
    <pre><code>ls /dev/tty.usbserial*</pre></code>
4. If using the AX Servo series, run:
<pre><code>python Servo.py -d /dev/[YOUR_USB_DEVICE] --baud 1000000 --scan</pre></code>
If not, run:
<pre><code>python Servo.py -d /dev/[YOUR_USB_DEVICE] --scan</pre></code>

