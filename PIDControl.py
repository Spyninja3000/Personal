from __future__ import print_function
from scipy import integrate

# mock robot init
class Robot:
    def __init__(self):
        self.leftdrive = self.leftdrive
        self.rightdrive = self.rightdrive
        # Would take in robot's data here within this class
        # I do not have access to any hardware that would give me data, so...

class PID:

    def __init__(self, Kp, Ki, Kd):
        self.kp = Kp
        self.ki = Ki
        self.kd = Kd

    def proportional(self, RobotData):
        e_t = 0 - RobotData
        return self.kp * e_t

    def integral(self, RobotData):
        result = integrate.quad(lambda x: RobotData.jv(2.5, x), 0, 4.5)
        return int(result[0])

    def derivative(self, RobotData):
        return 0 # maybe when I actually understand these I'll do it
        # IF ANYONE KNOWS HOW A DERIVATIVE WOULD WORK HERE PLZ HELP

Tom = Robot()
Tom.name = 'Tom'
Tom.leftdrive = 9.324
Tom.rightdrive = 9.386
drive = [Tom.leftdrive, Tom.rightdrive]
RobotData = max(drive) - min(drive)

Kp = 0.3
Ki = 0.0002
Kd = 0.0

while True:
    Kp = PID(Kp, Ki, Kd).proportional(RobotData)
    Ki = PID(Kp, Ki, Kd).integral(RobotData)
    Kd = PID(Kp, Ki, Kd).derivative(RobotData)
    print(Kp + Ki + Kd)
    
    if False:
        break

# loops forever, shouldn't ideally do thi
