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

    default_settings = cheerio_drive.settings()
    default_straight_speed = default_settings[0]
    default_straight_acceleration = default_settings[1]
    default_turn_rate = default_settings[2]
    default_turn_acceleration = default_settings[3]


    def is_stalled(self):
        return self.cheerio_drive.stalled()

    def drive_straight(self, speed, distance, acceleration=default_straight_acceleration, wait=True):
        self.cheerio_drive.settings(straight_speed=speed,straight_acceleration=acceleration)
        self.cheerio_drive.straight(distance=distance,wait=wait)

    def turn(self, speed, degrees, acceleration=default_turn_acceleration, wait=True):
        self.cheerio_drive.settings(turn_rate=speed,turn_acceleration=acceleration)
        self.cheerio_drive.turn(angle=degrees, wait=wait)

    
    def clean_dot_wheels_dot_com(self):
        self.drive_straight(speed=500, distance=10000)

    def polgon(self,distance,sides):
        for c in range(sides):
            self.cheerio_drive.straight(distance)
            self.cheerio_drive.turn(360.0/sides)

    def report_position(self,comment="position:"):
        print(comment, self.cheerio_drive.distance(), self.cheerio_drive.angle())

    def gyro_turn_to_heading(self,turn_rate,target_heading):
        self.report_position("starting gyro turn")
        start_heading=self.cheerio_drive.angle()
        self.cheerio_drive.drive(speed=0,turn_rate=turn_rate)
        if(start_heading < target_heading):
            while(self.cheerio_drive.angle()<target_heading):
                wait(1)
        else:
            while(self.cheerio_drive.angle()>target_heading):
                wait(1)
        self.cheerio_drive.brake()
        self.report_position("ending gyro turn")


