from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = PrimeHub()

#Creacion de variable
motor_izquierdo = Motor(Port.B)
motor_derecho = Motor(Port.D)

#Comando de trabajo

motor_izquierdo.run_time(720,6000,then=Stop.HOLD,wait=False)
motor_derecho.run_time(-720,6000,then=Stop.HOLD,wait=False)
wait(1150)
motor_izquierdo.run_angle(720,rotation_angle= 90,then=Stop.HOLD,wait=True)
wait(850)
motor_izquierdo.run_time(720,6000,then=Stop.HOLD,wait=False)
motor_derecho.run_time(-720,6000,then=Stop.HOLD,wait=False)
wait(700)
motor_izquierdo.run_angle(720,rotation_angle= 90,then=Stop.HOLD,wait=True)
wait(850)
motor_izquierdo.run_time(720,6000,then=Stop.HOLD,wait=False)
motor_derecho.run_time(-720,6000,then=Stop.HOLD,wait=False)
wait(1150)
motor_izquierdo.run_angle(720,rotation_angle= 90,then=Stop.HOLD,wait=True)
wait(850)
motor_izquierdo.run_time(720,6000,then=Stop.HOLD,wait=False)
motor_derecho.run_time(-720,6000,then=Stop.HOLD,wait=False)
wait(700)
motor_izquierdo.run_angle(720,rotation_angle= 90,then=Stop.HOLD,wait=True)
wait(850)
motor_izquierdo.run_time(720,6000,then=Stop.HOLD,wait=False)
motor_derecho.run_time(-720,6000,then=Stop.HOLD,wait=False)
wait(1150)
