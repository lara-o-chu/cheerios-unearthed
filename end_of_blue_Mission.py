from cheerio_bot import Cheerio

def run_end_of_blue_mission():
    bot = Cheerio()

    # drive to silo
    # bot.drive_straight(speed=500, distance=-400)    # hit silo
    # for rat in range(4):
    #     bot.left_attachment_motor.run_angle(speed=450,rotation_angle=-150)
    #     bot.left_attachment_motor.run_angle(speed=450,rotation_angle=150)
    
    # # turn to face forward
    # bot.turn(speed=100, degrees=180)
    
    # # TODO: CHANGE THIS TO USE THE COLOR SENSOR

    # # drive to boulder
    # bot.drive_straight(speed=967,distance=190)
    # bot.turn (speed=100, degrees=-45)

    # # heavy lifting arm
    # bot.right_attachment_motor.run_angle(speed=300,rotation_angle=-350)
    # bot.right_attachment_motor.run_angle(speed=300,rotation_angle=350)

    # # who lived here
    # bot.drive_straight(967,90)
    # bot.turn(speed=400,degrees=-30)
    # bot.turn(speed=400,degrees=30)

    # back up
    # bot.drive_straight(speed=250,distance=-150)
    # bot.turn(speed=100, degrees=-25)

    # # drive fast to red home area
    # bot.drive_straight(speed=925,distance=685)
    # bot.turn(speed=250,degrees=-43)
    # bot.drive_straight(speed=925,distance=750)
    # bot.turn (speed=500,degrees=-67)
    # bot.drive_straight(speed=967,distance=650)
    bot.drive_straight(340,25)
    bot.turn(speed=250, degrees=-45)
    bot.drive_straight(speed=250,distance=513)
    bot.turn(300,41)
    bot.drive_straight(300,-300)
    bot.drive_straight(300,90)
    bot.turn(450,-45)
    bot.left_attachment_motor.run_angle(967,-85)
    bot.left_attachment_motor.run_angle(967,85)
    bot.drive_straight(456,456)
    
    


# blue_mission()
