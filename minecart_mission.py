from pybricks.pupdevices import Motor,ColorSensor
from pybricks.parameters import Port, Direction
from pybricks.robotics import DriveBase
from pybricks.tools import wait
from cheerio_bot import Cheerio

def run_minecart_mission():
    bot=Cheerio()
    # drive to small black box
    bot.drive_straight(speed=300, distance=764)
    # turn toward mission
    bot.turn(speed=100, degrees=90)
    bot.drive_straight(speed=250, distance=408)
    bot.turn(speed=100, degrees=-90)
    bot.drive_straight(speed=250, distance=-124, acceleration=134)
    bot.right_attachment_motor.run_angle(speed=600, rotation_angle=-420)
    bot.drive_straight(speed=250, distance=42, acceleration=134)
    bot.right_attachment_motor.run_angle(600, 240)
    bot.drive_straight(speed=250,distance=145, acceleration=134)
    bot.left_attachment_motor.run_angle(620, 665)
    bot.left_attachment_motor.run_angle(620, 355)
    bot.left_attachment_motor.run_angle(420, -1010)
    bot.drive_straight(speed=250, distance=-87)
    bot.turn(speed=100, degrees=-90)
    bot.drive_straight(speed=250, distance=369)
    bot.turn(speed=100, degrees=-90)
    bot.drive_straight(speed=300, distance=764)

# run_minecart_mission()