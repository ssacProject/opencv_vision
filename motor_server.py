import time
from Adafruit_MotorHAT import Adafruit_MotorHAT
import socket
ip = '192.168.10.102'
#ip = '127.0.0.1'
server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_socket.bind((ip,9000))
server_socket.listen(5)

# sets motor speed between [-1.0, 1.0]
def set_speed(motor_ID, value):
	max_pwm = 115.0
	speed = int(min(max(abs(value * max_pwm), 0), max_pwm))

	if motor_ID == 1:
		motor = motor_left
	elif motor_ID == 2:
		motor = motor_right
	else:
		return
	
	motor.setSpeed(speed)

	if value > 0:
		motor.run(Adafruit_MotorHAT.BACKWARD)
	else:                
		motor.run(Adafruit_MotorHAT.FORWARD)


# stops all motors
def all_stop():
	motor_left.setSpeed(0)
	motor_right.setSpeed(0)

	motor_left.run(Adafruit_MotorHAT.RELEASE)
	motor_right.run(Adafruit_MotorHAT.RELEASE)




# setup motor controller
motor_driver = Adafruit_MotorHAT(i2c_bus=1)

motor_left_ID = 1
motor_right_ID = 2

motor_left = motor_driver.getMotor(motor_left_ID)
motor_right = motor_driver.getMotor(motor_right_ID)

set_speed(motor_left_ID,   0.0)
set_speed(motor_right_ID,  0.0)

time.sleep(1.0)

left = 0.0
right = 0.0

client_socket,address = server_socket.accept()
print("I got a connection from",address)
try:
    while 1:
        recData = client_socket.recv(512).decode()
        print(recData)
        if recData is 'w' :
            left  += 0.1
            right += 0.1
            set_speed(motor_left_ID,   left)
            set_speed(motor_right_ID,  right)
            sendData =str(left)+" "+str(right)
            client_socket.send(sendData.encode("utf-8"))
        elif recData is 's':
            left = 0.0
            right = 0.0
            set_speed(motor_left_ID,left)
            set_speed(motor_right_ID,right)
            sendData =str(left)+" "+str(right)
            client_socket.send(sendData.encode("utf-8"))
        elif recData is 'd':#left
            left += 0.1
            right += 0.0
            set_speed(motor_left_ID, left)
            set_speed(motor_right_ID,right)
            sendData = str(left)+" "+str(right)
            client_socket.send(sendData.encode("utf-8"))
        elif recData is 'a':
            left += 0.0
            right += 0.1
            set_speed(motor_left_ID, left)
            set_speed(motor_right_ID,right)
            sendData = str(left)+" "+str(right)
            client_socket.send(sendData.encode("utf-8"))
        # time.sleep(1.0)

except KeyboardInterrupt:  
    print("key int")
    all_stop()

# stop the motors as precaution
all_stop()
server_socket.close()
print('SOCKET closed....End')
