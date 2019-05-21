# Extra functions that are useful

import datetime


def format_date_time():
    now = str(datetime.datetime.now().strftime("%Y-%m-%d %H-%M-%S"))
    return now + ".txt"
