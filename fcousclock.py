# Test
import time

def countdown(minutes):
    seconds = minutes * 60
    while seconds > 0:
        mins, secs = divmod(seconds, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        seconds -= 1

# 设置专注时长为25分钟
focus_minutes = 25

# 设置休息时长为5分钟
break_minutes = 5

while True:
    print("Focus mode starts now.")
    countdown(focus_minutes)
    print("Time's up! Take a break.")
    countdown(break_minutes)
