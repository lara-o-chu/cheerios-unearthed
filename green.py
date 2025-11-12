from pybricks.pupdevices import Motor,ColorSensor
from pybricks.parameters import Port, Direction
from pybricks.robotics import DriveBase
from pybricks.tools import wait
from cheerio_bot import Cheerio

def run_grass_mission():
    bot=Cheerio()
    # drive to small black box
    bot.drive_straight(speed=400, distance=785)
    # turn toward mission
    bot.turn(speed=200, degrees=-45)
    # drive to map mission
    bot.drive_straight(speed=220, distance=190)
    # lift at map mission
    bot.right_attachment_motor.run_angle(speed=250, rotation_angle=90)
    # back away from map mission
    bot.drive_straight(speed=200, distance=-90)
    # turn toward wall
    bot.turn(speed=100, degrees=-135)
    # drive toward sweep mission
    bot.drive_straight(speed=200, distance=180)
    # turn toward sweep mission
    bot.turn(speed=150, degrees=90)
    # lower arm
    bot.right_attachment_motor.run_angle(speed=250, rotation_angle=-45)
    # crash into sweep mission
    bot.drive_straight(speed=200, distance=70)
    # lift arm
    bot.right_attachment_motor.run_angle(speed=200, rotation_angle=140)
    # back away from sweep mission
    bot.drive_straight(speed=200, distance=-100)
#     bot.drive_straight(speed=300, distance=-335)
#     bot.drive_straight(speed=300, distance=155)
#     bot.drive_straight(speed=300, distance=-155)
#     bot.turn(speed=100, degrees=90)
#     bot.drive_straight(speed=950, distance=-450)
# # run_minecart_mission()