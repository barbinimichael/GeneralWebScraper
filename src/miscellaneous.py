# Extra functions that are useful

import datetime
import string
import random


def format_date_time():
    now = str(datetime.datetime.now().strftime("%Y-%m-%d %H-%M-%S"))
    return now + ".txt"


def random_string(stringlength=10):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringlength))