# Methodical approach to Law of Cosines programming - FRC team 1261 robolions
# Makes minute interval changes rather than steady and long changes
# checks for violations in between each interval of change

from numpy import arange

current_boom = 0
current_vert = 0

def isViolating(current):
    if current >= 12:
        return True
    else:
        return False

def setBoomPower(power, current=current_boom):
    print "Running Boom at " + str(power)
    current += power
    return current

def setVertPower(power, current=current_vert):
    print "Running Vert at " + str(power)
    current += power
    return current

boomPower = 13
vertPower = 5

boom_intervals = []
boom_step = 0.1
for interval in arange(0, boomPower, boom_step):
    boom_intervals.append(boom_step)

for interval in boom_intervals:
    if isViolating(current_boom):
        print "Boom extended too far"
    else:
        current_boom += setBoomPower(interval)

vert_intervals = []
vert_step = 0.1
for interval in arange(0, vertPower, vert_step):
    vert_intervals.append(vert_step)

for interval in vert_intervals:
    if isViolating(current_vert):
        print "Vert extended too far"
    else:
        current_vert += setVertPower(interval)