from pybricks.pupdevices import Motor,ColorSensor
from pybricks.parameters import Port, Direction
from pybricks.robotics import DriveBase
from pybricks.tools import wait
from CheerioBot import Cheerio

def blue_mission():
    bot = Cheerio()

    # drive to silo
    bot.drive_straight(speed=500, distance=-400)    # hit silo
    for rat in range(4):
        bot.left_attachment_motor.run_angle(speed=450,rotation_angle=-300)
        bot.left_attachment_motor.run_angle(speed=450,rotation_angle=300)
     # turn to face forward
    bot.turn(speed=100, degrees=180)
    #TODO:CHANGE THIS TO USE THE COLOR SENSOR

    # drive to boulder

    bot.drive_straight(967,220)

    # boulder+arm
    bot.turn (speed=100, degrees=-45)

    bot.right_attachment_motor.run_angle(300,-350)
    
    bot.right_attachment_motor.run_angle(300,350)

    bot.drive_straight(967,90)

    bot.turn(speed=100, degrees=-45)

blue_mission()
