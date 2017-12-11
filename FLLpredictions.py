# A handy program to determine how much of a chance a First Lego League team has of making it to the next level of competition
# It interprets each team as a dictionary of scores
# By: Tejas Shah


from __future__ import print_function
import numpy

robonators = {'robot': 40, 'design': 33, 'core values': 30, 'project': 31} # team 6880
terabytes = {'robot': 20, 'design': 24, 'core values': 31, 'project': 30} # team 6881    # In case you want to check out the teams that I coach,
honorbots = {'robot': 55, 'design': 28, 'core values': 29, 'project': 33} # team 9682    # here are their numbers. They're all in Georgia.
rrambots = {'robot': 45, 'design': 27, 'core values': 31, 'project': 29} # team 22346
perfect_team = {'robot': 100, 'design': 36, 'core values': 36, 'project': 36}
worst_team = {'robot': 0, 'design': 0, 'core values': 0, 'project': 0}
your_team = {'robot': None, 'design': None, 'core values': None, 'project': None} # enter in your team's values here in place of the 'None's

robot_scores = [70, 50, robonators['robot'], terabytes['robot'], 45, honorbots['robot'], 55, 20, 70, 55, 60, 65, 30, 70, 35, 70, rrambots['robot'], 50, 70, 105, 10, 85, 50, 65]
# replace these scores with the final scoreboard of the competition

def robot_chance(team):
    average_robot = int(numpy.average(robot_scores))
    best_robot = max(robot_scores)
    good_robot = numpy.average([average_robot, best_robot])
    dif = int(float(team['robot'] / good_robot) * 100)
    return dif


def design_chance(team):
    average = 32
    best = 36
    good = numpy.average([best, average])
    dif = int(float(team['design'] / good) * 100)
    return dif


def core_chance(team):
    average = 32
    best = 36
    good = numpy.average([best, average])
    dif = int(float(team['core values'] / good) * 100)
    return dif


def project_chance(team):
    average = 32
    best = 36
    good = numpy.average([best, average])
    dif = int(float(team['project'] / good) * 100)
    return dif


def total_chance(team):
    rob = robot_chance(team) * 0.25
    des = design_chance(team) * 0.10
    proj = project_chance(team) * 0.50
    core = core_chance(team) * 0.15
    total = rob + des + proj + core
    return total

def main():
    #print('Robonators: ' + str(total_chance(robonators)))
    #print('Terabytes: ' + str(total_chance(terabytes)))
    #print('Honorbots: ' + str(total_chance(honorbots)))
    #print('Rrambots: ' + str(total_chance(rrambots)))
    #print(total_chance(perfect_team))
    #print(total_chance(worst_team))
    print("Your team's percent chance of making it to the next round is: " + str(total_chance(your_team))) # change 'your_team' to the team name

if __name__ == '__main__':
    main()
