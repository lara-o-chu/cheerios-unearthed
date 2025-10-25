from pybricks.pupdevices import Motor,ColorSensor
from pybricks.parameters import Port, Direction
from pybricks.robotics import DriveBase
from pybricks.tools import wait
from cheerio_bot import Cheerio

def run_minecart_mission():
    bot=Cheerio()
    # drive to small black box
    bot.drive_straight(speed=300, distance=710)
    # turn toward mission
    bot.turn(speed=100, degrees=90)
    bot.drive_straight(speed=250, distance=402)
    bot.turn(speed=100, degrees=-90)
    bot.drive_straight(speed=250, distance=-100)
    bot.right_attachment_motor.run_angle(speed=600, rotation_angle=-420)
    bot.drive_straight(speed=250, distance=60)
    bot.right_attachment_motor.run_angle(600, 240)
    bot.drive_straight(speed=250,distance=125)
    bot.left_attachment_motor.run_angle(620, 665)
    bot.left_attachment_motor.run_angle(620, 255)
    bot.left_attachment_motor.run_angle(420, -1010)
    # bot.drive_straight(speed=250, distance=-117)

# run_minecart_mission()