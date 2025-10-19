from pybricks.pupdevices import Motor,ColorSensor
from pybricks.parameters import Port, Direction
from pybricks.robotics import DriveBase
from pybricks.tools import wait


class Cheerio:

    left_motor = Motor(Port.A, Direction.COUNTERCLOCKWISE)
    right_motor = Motor(Port.C,Direction.CLOCKWISE)
    left_color_sensor = ColorSensor(Port.F)
    right_color_sensor = ColorSensor(Port.E)
    left_attachment_motor = Motor(Port.D,Direction.CLOCKWISE)
    right_attachment_motor = Motor(Port.B,Direction.CLOCKWISE)

    cheerio_drive = DriveBase(left_motor, right_motor, wheel_diameter=56, axle_track=96)

    cheerio_drive.use_gyro(True)

    def drive_straight(self, speed, distance):
        self.cheerio_drive.settings(straight_speed=speed)
        self.cheerio_drive.straight(distance=distance)

    def turn(self, speed, degrees):
        self.cheerio_drive.settings(turn_rate=speed)
        self.cheerio_drive.turn(angle=degrees)


    def polgon(self,distance,sides):
        for c in range(sides):
            self.cheerio_drive.straight(distance)
            self.cheerio_drive.turn(360.0/sides)


def minecart_mission():
    bot=Cheerio()
    # drive to small black box
    bot.drive_straight(speed=300, distance=725)
    # turn toward mission
    bot.turn(speed=100, degrees=90)
    bot.drive_straight(speed=250, distance=450)
    bot.turn(speed=100, degrees=-90)
    bot.drive_straight(speed=50, distance=70)

def blue_mission():
    bot = Cheerio()

    # drive to silo
    bot.drive_straight(speed=500, distance=-400)    # hit silo
    for rat in range(4):
        bot.left_attachment_motor.run_angle(968,610)
        bot.left_attachment_motor.run_angle(969,-200)

     # turn to face forward
    bot.turn(speed=100, degrees=180)
    #TODO:CHANGE THIS TO USE THE COLOR SENSOR

    # drive to boulder
    bot.drive_straight(967,195)

    # boulder+arm

    bot.turn (speed=100, degrees=-45)

    bot.right_attachment_motor.run_angle(300,-350)
    
    bot.right_attachment_motor.run_angle(300,350)

    bot.drive_straight(967,90)

    bot.turn(speed=100, degrees=-45)

blue_mission()
# minecart_mission()

c_drive=Cheerio()
  
# c_drive.polgon(100,5)
# c_drive.cheerio_drive.settings(straight_speed=967)
# c_drive.cheerio_drive.straight(-330)
# # c_drive.cheerio_drive.turn(-90)
# c_drive.cheerio_drive.settings(straight_speed=250)
# c_drive.cheerio_drive.straight(650)
# c_drive.cheerio_drive.straight(-625)
# c_drive.cheerio_drive.straight(-330)


# c_drive.cheerio_drive.turn(90)
# c_drive.cheerio_drive.straight(-398)
# c_drive.cheerio_drive.turn(90)
# c_drive.cheerio_drive.straight(117)
# c_drive.cheerio_drive.turn(-12)
# c_drive.left_attachment_motor.run_angle(100,-240)
# c_drive.left_attachment_motor.run_angle(800, 1000)



# c_drive.right_attachment_motor.run_angle(9870,-250)
# wait(1000)
# # c_drive.right_attachment_motor.run_angle(987000,250)
# c_drive.right_attachment_motor.run_angle(987,200)
