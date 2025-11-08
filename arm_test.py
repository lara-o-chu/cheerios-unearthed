from cheerio_bot import Cheerio
from pybricks.tools import wait
from pybricks.tools import StopWatch

def run_arm_test():
    bot = Cheerio()

    bot.left_attachment_motor.run(-10000)
    wait(3000)
    bot.left_attachment_motor.stop()


run_arm_test()