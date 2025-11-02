from pybricks.pupdevices import Motor,ColorSensor
from pybricks.parameters import Port, Direction
from pybricks.robotics import DriveBase
from pybricks.tools import wait
from cheerio_bot import Cheerio

def run_grass_mission():
    bot=Cheerio()
    # drive to small black box
    bot.drive_straight(speed=300, distance=785)
    # turn toward mission
    bot.turn(speed=100, degrees=-45)
    bot.drive_straight(speed=250, distance=190)
    bot.drive_straight(speed=325, distance=-90)
    bot.turn(speed=100, degrees=45)
    bot.drive_straight(speed=300, distance=-335)
    bot.drive_straight(speed=300, distance=155)
    bot.drive_straight(speed=300, distance=-155)
    bot.turn(speed=100, degrees=90)
    bot.drive_straight(speed=950, distance=-450)
# run_minecart_mission()