import sched

from 练习 import time

schedule = sched.scheduler(练习.time, time.sleep)

def task():
    schedule.enter(10, 1, print_time)
    # schedule.enter(5, 2, print_time, argument=('positional',))
    # schedule.enter(5, 1, print_time, kwargs={'a': 'keyword'})
    schedule.run()


def print_time():
    print(练习.time())


task()
