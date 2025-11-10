from cheerio_bot import Cheerio
from pybricks.tools import wait
from pybricks.tools import StopWatch

def run_check_reflection():
    bot = Cheerio()

    # drive to silo
    # bot.drive_straight(speed=200, distance=700, wait=False)

    # while not bot.cheerio_drive.done():
    while True:
        print (bot.right_color_sensor.reflection())
        wait(10)

run_check_reflection()