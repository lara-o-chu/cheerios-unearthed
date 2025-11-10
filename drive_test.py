from cheerio_bot import Cheerio
from pybricks.tools import wait
from pybricks.tools import StopWatch

def run_drive_test():
    bot = Cheerio()

    # drive to silo
    bot.cheerio_drive.drive(speed=0,turn_rate=100)
    wait(5000)
    # bot.drive_straight(speed=200, distance=700, wait=False)

    # while not bot.cheerio_drive.done():
    # while True:
    #     print (bot.right_color_sensor.reflection())
    #     wait(10)

run_drive_test()