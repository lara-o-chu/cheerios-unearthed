from cheerio_bot import Cheerio
from pybricks.tools import wait
from pybricks.tools import StopWatch

def run_blue_mission():
    bot = Cheerio()

    bot.cheerio_drive.reset(distance=0, angle=-180)

    # lift arms to correct starting position
    bot.right_attachment_motor.run_angle(speed=350,rotation_angle=-200)
    bot.left_attachment_motor.run_angle(speed=350,rotation_angle=160)

    # back up into the wall a little bit so we can drive straght
    bot.cheerio_drive.drive(speed=200,turn_rate=0)
    wait(500)

    print("Starting", bot.cheerio_drive.distance(), bot.cheerio_drive.angle())

    # drive to silo
    bot.drive_straight(speed=500, distance=-400)    # hit silo
    for rat in range(4):
        bot.left_attachment_motor.run_angle(speed=450,rotation_angle=-150)
        bot.left_attachment_motor.run_angle(speed=450,rotation_angle=150)
    
    # turn to face forward
    bot.turn(speed=100, degrees=180)
    
    # drive to boulder
    bot.cheerio_drive.drive(speed=200,turn_rate=0)
    while bot.right_color_sensor.reflection() > 20:
        wait(1)
    bot.drive_straight(speed=100,distance=36)
    bot.turn (speed=160, degrees=-45)

    # heavy lifting arm
    bot.drive_straight(speed=100,distance=15)
    bot.right_attachment_motor.run_angle(speed=300,rotation_angle=-340)
    bot.right_attachment_motor.run_angle(speed=300,rotation_angle=340)

    # who lived here
    bot.drive_straight(200,70)
    bot.turn(speed=400,degrees=-30,wait=False)
    watch=StopWatch()

    while not bot.cheerio_drive.done() and not bot.is_stalled() and not watch.time() > 1000:
        wait(10)

    bot.drive_straight(speed=100,distance=-77)
    bot.cheerio_drive.drive(0,100)
    while bot.right_color_sensor.reflection() > 20:
        wait(1)
    bot.cheerio_drive.stop()

    bot.gyro_turn_to_heading(turn_rate=-50,target_heading=-78)
    wait(100)

    # whats on sale
    bot.drive_straight(speed=250,distance=560)
    bot.gyro_turn_to_heading(turn_rate=50,target_heading=-45)
    wait(100)
    bot.drive_straight(300,-300)

    # tip the scales
    bot.drive_straight(300,90)
    bot.turn(450,-45)
    bot.left_attachment_motor.run_angle(967,-85)
    bot.left_attachment_motor.run_angle(967,85)

    # drive to red home area
    bot.drive_straight(456,218)
    bot.turn(speed=100,degrees=-90)
    bot.drive_straight(speed=700,distance=350)
    bot.turn(100,80)
    bot.drive_straight(speed=700,distance=300)
    bot.turn(speed=700,degrees=-20)
    bot.drive_straight(700,10000)
