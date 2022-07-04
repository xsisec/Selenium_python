from datetime import datetime
import time
import os


def save_screenshot_picture(self, driver) :
    try :
        os.makedirs("../../Application/Reports/screenshots")
    except FileExistsError :
        print("directory already exists")
        dt_format = '%Y%m%d_%H%M%S'
        date_string = datetime.fromtimestamp(time.time()).strftime(dt_format)
        driver.save_screenshot('../../Application/Reports/screenshots/' + date_string + '.png')
