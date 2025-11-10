from cheerio_bot import Cheerio

def run_pirate_boat():
    bot=Cheerio()

    # Start in red home area 
    # Drive forward until pushing against boat mission
    bot.drive_straight(speed=400, distance=580)

    
    # Lower arm
    bot.left_attachment_motor.run_angle(speed=150, rotation_angle=-2160)
    bot.drive_straight(speed=200, distance=-20)
    bot.left_attachment_motor.run_angle(speed=150, rotation_angle=360)
    '''# Change to gear spin side of gear 
    bot.right_attachment_motor.run_angle(speed=100, rotation_angle=-180)
    # Spin gears
    bot.left_attachment_motor.run_angle(speed=200, rotaion_angle=500)
    #change to lifty thingy gear setting
    bot.right_attachment_motor(speed=100, rotation_angle=-180)
    # Raise arm
    bot.left_attachment_motor(speed=150, distance=-720)
    # Back up to home (Hopefully pull sand)
    bot.drive_straight(speed=400,distance= -447)
    '''












