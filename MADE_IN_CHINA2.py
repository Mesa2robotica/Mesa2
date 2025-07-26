from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = PrimeHub()
motorD=Motor(Port.B,Direction.COUNTERCLOCKWISE)
motori=Motor(Port.A,Direction.CLOCKWISE)
colorsensori=ColorSensor(Port.F)
colorsensord=ColorSensor(Port.C)
colorsensorm=ColorSensor(Port.D)
Color.BLACKD=Color(h=185,s=8,v=99)
Color.BLACKI=Color(h=198,s=29,v=31)
Color.BLACKM=Color(h=210,s=22,v=24)
Color.WHITED=Color(h=204,s=13,v=99)
Color.WHITEI=Color(h=0,s=0,v=100)
Color.WHITEM=Color(h=0,s=0,v=100)
Color.GREENI= Color(h=161,s=75,v=60)
Color.GREEND= Color(h=162,s=75,v=60)

my_colorsd = (Color.GREEND,Color.NONE,Color.WHITED,Color.BLACKD)
my_colorsi = (Color.GREENI,Color.NONE,Color.WHITEI,Color.BLACKI)
my_colorsm = (Color.NONE,Color.WHITEM,Color.BLACKM)
colorsensord.detectable_colors(my_colorsd)
colorsensori.detectable_colors(my_colorsi)
colorsensorm.detectable_colors(my_colorsm)

while True:
    colord=colorsensord.color()
    colori=colorsensori.color()
# seguidor de linea
    if colorsensord.reflection() < 30: 
        motorD.run(-120)
    if colorsensori.reflection() < 30:
        motori.run(-120) 

    if colorsensord.reflection() > 80:
        motorD.run(90)
    if colorsensori.reflection() > 80:
        motori.run(90)

# doble negro
    if colorsensori.color() == Color.BLACKI and colorsensord.color() == Color.BLACKD and colorsensorm.color() == Color.BLACKM:
        motori.run(50)
        motord.run(50)
        wait(500)
    if colorsensori.color() == Color.GREENI and colorsensord.color() == Color.GREEND:
        hub.display.char("DV")
        motorD.stop()
        motori.stop()
        wait(500)
    if colorsensord.color() == Color.GREEND: 
        #hub.display.char("VD")
        #wait(2000)
        hub.imu.reset_heading(0)
        #while True:
            #print(hub.imu.heading())
        while hub.imu.heading()<90:
            motorD.run(-50)
            motori.run(50)
        motorD.stop()
        motori.stop()
    if colorsensori.color() == Color.GREENI:
        #hub.display.char("VI")
        #wait(2000)
        hub.imu.reset_heading(0)
        while True:
            print(hub.imu.heading())
            while hub.imu.heading()>-90:
                motorD.run(50)
                motori.run(-50)
            motorD.stop()
            motori.stop()






