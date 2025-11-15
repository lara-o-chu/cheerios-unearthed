from cheerio_bot import Cheerio
from pybricks.tools import wait
from pybricks.tools import StopWatch

def run_drive_test():
    bot = Cheerio()

    bot.report_position("starting drive test")

    bot.gyro_turn_to_heading(turn_rate=-200,target_heading=-60)
    wait(100)
    bot.report_position("middle of drive test")
    bot.gyro_turn_to_heading(turn_rate=-50,target_heading=-80)
    wait(100)
    bot.report_position("ending drive test")


run_drive_test()