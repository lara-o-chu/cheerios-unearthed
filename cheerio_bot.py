from pybricks.pupdevices import Motor,ColorSensor
from pybricks.parameters import Port, Direction
from pybricks.robotics import DriveBase
from pybricks.tools import wait
from pybricks.tools import StopWatch


class Cheerio:

    left_motor = Motor(Port.A, Direction.COUNTERCLOCKWISE)
    right_motor = Motor(Port.C,Direction.CLOCKWISE)
    left_color_sensor = ColorSensor(Port.F)
    right_color_sensor = ColorSensor(Port.E)
    left_attachment_motor = Motor(Port.D,Direction.CLOCKWISE)
    right_attachment_motor = Motor(Port.B,Direction.CLOCKWISE)

    cheerio_drive = DriveBase(left_motor, right_motor, wheel_diameter=56, axle_track=96)

    cheerio_drive.use_gyro(True)

    def is_stalled(self):
        return self.cheerio_drive.stalled()

    def drive_straight(self, speed, distance, wait=True):
        self.cheerio_drive.settings(straight_speed=speed)
        self.cheerio_drive.straight(distance=distance,wait=wait)

    def turn(self, speed, degrees, wait=True):
        self.cheerio_drive.settings(turn_rate=speed)
        self.cheerio_drive.turn(angle=degrees, wait=wait)

    
    def clean_dot_wheels_dot_com(self):
        self.drive_straight(speed=500, distance=10000)

    def polgon(self,distance,sides):
        for c in range(sides):
            self.cheerio_drive.straight(distance)
            self.cheerio_drive.turn(360.0/sides)


