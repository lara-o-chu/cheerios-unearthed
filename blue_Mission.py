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
    bot.right_attachment_motor.run_angle(speed=300,rotation_angle=-340)
    bot.right_attachment_motor.run_angle(speed=300,rotation_angle=340)

    # REMOVE
    print("Lifted:", bot.cheerio_drive.distance(), bot.cheerio_drive.angle())

    # who lived here
    bot.drive_straight(200,70)
    bot.turn(speed=400,degrees=-30,wait=False)
    watch=StopWatch()

    # REMOVE
    print("Before Who Lived Here While Loop:", bot.cheerio_drive.distance(), bot.cheerio_drive.angle())

    print("starting while loop")

    while not bot.cheerio_drive.done() and not bot.is_stalled() and not watch.time() > 1000:
        message = "done: " + str(bot.cheerio_drive.done()) 
        message = message + ", stalled: " + ("True" if bot.is_stalled() else "False")
        message = message + ", time: " + str(watch.time())
        # print(message)
        wait(10)

    # REMOVE
    print("After Who Lived Here While Loop:", bot.cheerio_drive.distance(), bot.cheerio_drive.angle())

    print("ended while loop")

    bot.drive_straight(speed=100,distance=-77)
    # bot.turn(speed=100,degrees=34,wait=False)
    bot.cheerio_drive.drive(0,100)
    # bot.cheerio_drive.turn()
    while bot.right_color_sensor.reflection() > 20:
        wait(1)
    bot.cheerio_drive.stop()

    # bot.drive_straight(speed=100,distance=)
    # bot.drive_straight(340,25)
    # DO NOT MESS WITH THIS 40 POINT,ALMOST WORKING, PICE OF CODE

    print("Before Last Turn Toward to Whats on Sale:", bot.cheerio_drive.distance(), bot.cheerio_drive.angle())
    
    # wait(200)

    # current_heading =bot.cheerio_drive.angle()

    # target_heading=-80
    # turn_angle =target_heading-current_heading

    # print("current_heading", current_heading)
    # print("target_heading", target_heading)
    # print("turn_angle", turn_angle)

    bot.turn(speed=167, degrees=-41)
    # bot.turn(speed=167, degrees=turn_angle, acceleration=100) 
    # bot.turn(speed=167, degrees=turn_angle) 

    print("Before Driving to Whats on Sale:", bot.cheerio_drive.distance(), bot.cheerio_drive.angle())

    # wait(200)

    print("Final:", bot.cheerio_drive.distance(), bot.cheerio_drive.angle())


    bot.drive_straight(speed=250,distance=540)
    bot.turn(300,48)
    bot.drive_straight(300,-300)
    bot.drive_straight(300,90)
    bot.turn(450,-45)
    bot.left_attachment_motor.run_angle(967,-85)
    bot.left_attachment_motor.run_angle(967,85)
    bot.drive_straight(456,218)
    bot.turn(speed=100,degrees=-90)
    bot.cheerio_drive.drive(300,0)
    while bot.right_color_sensor.reflection()>20 and bot.left_color_sensor.reflection()> 20 :
        wait(1)
    bot.turn(100,80)
    bot.drive_straight(200,10000)
