from pybricks.pupdevices import Motor,ColorSensor
from pybricks.parameters import Port, Direction
from pybricks.robotics import DriveBase
from pybricks.tools import wait
from cheerio_bot import Cheerio

def run_minecart_mission():
    bot=Cheerio()
    # back up into the wall a little bit so we can drive straght
    bot.cheerio_drive.drive(speed=-200,turn_rate=0)
    wait(500)
    # drive to small black box
    bot.drive_straight(speed=300, distance=724)
    # turn toward mission
    bot.turn(speed=100, degrees=90)
    bot.drive_straight(speed=250, distance=408, acceleration=100)
    bot.turn(speed=100, degrees=-90)
    bot.drive_straight(speed=250, distance=-114, acceleration=100)
    bot.right_attachment_motor.run_angle(speed=600, rotation_angle=-420)
    bot.drive_straight(speed=250, distance=62, acceleration=100)
    bot.right_attachment_motor.run_angle(600, 240)
    bot.drive_straight(speed=250,distance=115, acceleration=100)
    bot.left_attachment_motor.run_angle(620, 950)
    bot.left_attachment_motor.run_angle(620, 60)
    bot.left_attachment_motor.run_angle(420, -1010)
 
    bot.drive_straight(speed=250, distance=-87)
    bot.turn(speed=100, degrees=-90)
    bot.drive_straight(speed=250, distance=369)
    bot.turn(speed=100, degrees=-90)
    bot.drive_straight(speed=300, distance=764)

# run_minecart_mission()