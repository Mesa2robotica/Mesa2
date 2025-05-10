from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = PrimeHub()

#creación de variable
motor_izquierdo = Motor(Port.B) 
motor_derecho= Motor(Port.D,Direction.COUNTERCLOCKWISE)
sensor = ColorSensor (Port.E)

#Comando de trabajo
Color.BLACK = Color(h=240, s=13, v=9)
Color.WHITE = Color(h=300, s=1, v=52)

my_colors = (Color.BLACK, Color.WHITE) 
sensor.detectable_colors(my_colors)

while True: 
    color = sensor.color()
    print(color)   
    wait(20)

    if color == Color.BLACK:
        print ("es negro")
        
        wait(100)
        motor_izquierdo.run(150)
        motor_derecho.run(150)
        wait(50)
        
    if color == Color.WHITE:
        motor_derecho.stop()
        motor_izquierdo.stop() 
        motor_izquierdo.run(-300)
        motor_derecho.run(-300)
        wait(2000)
        motor_izquierdo.run_angle(170*3,45*3,wait=False)
        motor_derecho.run_angle(170*3,-45*3,wait=False)
        wait(750)
        
"""
color = sensor.color()
    print(color) 
"""
"""
#comando de trabajo
while True: 
    color = sensor.color()
    if color == Color.WHITE: 
        print("blanco")
        wait(1000)
        motor_izquierdo.run_time(200,6000,then=Stop.HOLD,wait=False)
        motor_derecho.run_time(200,6000,then=Stop.HOLD,wait=False)
        wait(1150)
        motor_izquierdo.run_angle(170*3,90*3,wait=False)
        motor_derecho.run_angle(170*3,-90*3,wait=False)
        wait(750)
        
    else:  
        motor_izquierdo.run_time(-150,2000,then=Stop.HOLD,wait=False)
        motor_derecho.run_time(-250,2000,then=Stop.HOLD,wait=False)
        wait(3000)
        """
