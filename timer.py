# this file is by igniteflow and changed a bit by MelanX
# https://gist.github.com/igniteflow/1253276

import datetime


class Timer(object):
    """A simple timer class"""

    def __init__(self):
        pass

    def start(self):
        """Starts the timer"""
        self.start = datetime.datetime.now()
        return self.start

    def stop(self):
        """Stops the timer.  Returns the time elapsed"""
        self.stop = datetime.datetime.now()
        return self.stop - self.start

    def reset(self):
        """Resets the timer."""
        del self.start
        del self.stop
        return

    def now(self):
        """Returns the current time with a message"""
        return datetime.datetime.now()

    def elapsed(self):
        """Time elapsed since start was called"""
        return datetime.datetime.now() - self.start

    def split(self):
        """Start a split timer"""
        self.split_start = datetime.datetime.now()
        return self.split_start

    def unsplit(self):
        """Stops a split. Returns the time elapsed since split was called"""
        return datetime.datetime.now() - self.split_start
