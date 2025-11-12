from cheerio_bot import Cheerio

def run_pirate_boat():
    bot=Cheerio()

    # Start in red home area 
    # Drive forward until pushing against boat mission
    bot.drive_straight(speed=300, distance=580)

    
    # Lower arm
    bot.left_attachment_motor.run_angle(speed=2000, rotation_angle=-2160)
    bot.drive_straight(speed=100, distance=-20)
    bot.drive_straight(speed=100, distance=30)

    # Change to gear spin side of gear 
    bot.right_attachment_motor.run_angle(speed=100, rotation_angle=-200)
    #spin thingy
    bot.left_attachment_motor.run_angle(speed=2000, rotation_angle=-4000)
    #Switch setting
    bot.right_attachment_motor.run_angle(speed=100,rotation_angle=-220)
    bot.drive_straight(speed=200, distance=-75)
    #lift arm
    bot.left_attachment_motor.run_angle(speed=2000, rotation_angle=2900)
    # Back up to home (Hopefully pull sand)
    bot.drive_straight(speed=325,distance=-750)
    












