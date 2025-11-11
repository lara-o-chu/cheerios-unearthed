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
    
    # REMOVE
    print("After Silo:", bot.cheerio_drive.distance(), bot.cheerio_drive.angle())

    # turn to face forward
    bot.turn(speed=100, degrees=180)
    
    # REMOVE
    print("After Turn:", bot.cheerio_drive.distance(), bot.cheerio_drive.angle())

    # TODO: CHANGE THIS TO USE THE COLOR SENSOR

    # drive to boulder
    # bot.drive_straight(speed=967,distance=190,wait=False)
    bot.cheerio_drive.drive(speed=200,turn_rate=0)
    while bot.right_color_sensor.reflection() > 20:
        wait(1)
    bot.drive_straight(speed=100,distance=36)
    # REMOVE
    print("Found Black:", bot.cheerio_drive.distance(), bot.cheerio_drive.angle())
    bot.turn (speed=160, degrees=-45)

    # REMOVE
    print("Turned:", bot.cheerio_drive.distance(), bot.cheerio_drive.angle())

    # heavy lifting arm
    bot.drive_straight(speed=100,distance=15)
    bot.right_attachment_motor.run_angle(speed=300,rotation_angle=-350)
    bot.right_attachment_motor.run_angle(speed=300,rotation_angle=350)

    # REMOVE
    print("Lifted:", bot.cheerio_drive.distance(), bot.cheerio_drive.angle())

    # who lived here
    bot.drive_straight(967,90)
    bot.turn(speed=400,degrees=-30,wait=False)
    watch=StopWatch()

    # REMOVE
    print(bot.cheerio_drive.distance(), bot.cheerio_drive.angle())

    settings = bot.cheerio_drive.settings()
    print(settings)

    print("starting while loop")

    while not bot.cheerio_drive.done() and not bot.is_stalled() and not watch.time() > 1000:
        message = "done: " + str(bot.cheerio_drive.done()) 
        message = message + ", stalled: " + ("True" if bot.is_stalled() else "False")
        message = message + ", time: " + str(watch.time())
        # print(message)
        wait(10)

    # REMOVE
    print(bot.cheerio_drive.distance(), bot.cheerio_drive.angle())

    print("ended while loop")

    bot.drive_straight(speed=100,distance=-77)
    # bot.turn(speed=100,degrees=34,wait=False)
    bot.cheerio_drive.drive(0,100)
    # bot.cheerio_drive.turn()
    while bot.right_color_sensor.reflection() > 20:
        wait(1)
    # bot.drive_straight(speed=100,distance=)
    # bot.drive_straight(340,25)
    # DO NOT MESS WITH THIS 40 POINT,ALMOST WORKING, PICE OF CODE
    bot.turn(speed=250, degrees=-42)
    bot.drive_straight(speed=250,distance=530)
    bot.turn(300,48)
    bot.drive_straight(300,-300)
    bot.drive_straight(300,90)
    bot.turn(450,-45)
    bot.left_attachment_motor.run_angle(967,-85)
    bot.left_attachment_motor.run_angle(967,85)
    bot.drive_straight(456,228)
    
    

    # bot.drive_straight(speed=455,distance=-5000)
    # bot.turn(speed=400,degrees=30)

#     # back up
#     bot.drive_straight(speed=250,distance=-150)
#     bot.turn(speed=100, degrees=-25)

#     # drive fast to red home area
#     bot.drive_straight(speed=925,distance=685)
#     bot.turn(speed=250,degrees=-43)
#     bot.drive_straight(speed=925,distance=750)
#     bot.turn (speed=500,degrees=-67)
#     bot.drive_straight(speed=967,distance=650)

# # blue_mission()
