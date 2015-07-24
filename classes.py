import random
from urllib.request import urlopen
import bs4


class InstanceCounter(object):
    count = 0

    def __init__(self, val):
        self.val = val
        InstanceCounter.count += 1

    def set_val(self, newval):
        self.val = newval

    def get_val(self):
        return self.val

    def get_count(self):
        return InstanceCounter.count

    def increment(self):
        self.val = random.randint(1, 10)

# for obj in (a, b, c):
#     print((obj.get_val()))
#     print((obj.get_count()))
