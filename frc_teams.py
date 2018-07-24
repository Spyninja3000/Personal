'''

This is a program to analyze the best teams of the FIRST Robotics Competition (FRC)
By using each teams' position on an alliance and how far each of their alliances get each year,
I have come up with a very tentative ranking system to evaluate which teams are the best in the competition
This list was compiled based on data from the six Einstein-level competitions that have happened from 2015 to 2018

'''


years = {

    '2015': {
        'C': [1023, 148, 2056, 118, 987, 1325, 368, 3132],
        '1': [2338, 1114, 330, 1678, 2826, 3339, 359, 3476],
        '2': [3996, 1923, 492, 1671, 4265, 20, 337, 1255],
        '3': [1089, 900, 3944, 5012, 2512, 1711, 144, 2526]
    },

    '2016': {
        'C': [217, 694, 1501, 195, 2122, 2056, 330, 148],
        '1': [3476, 3339, 1986, 987, 2052, 1690, 2481, 1678],
        '2': [4678, 379, 5050, 1197, 3538, 3015, 120, 364],
        '3': [188, 1511, 4828, 1065, 41, 1405, 1086, 2990]
    },

    '2017_HOU': {
        'C': [2122, 1318, 5654, 973, 604, 118],
        '1': [987, 2046, 2415, 1011, 2848, 1678],
        '2': [4910, 1595, 2630, 2928, 1868, 4188],
        '3': [6314, 2907, 4112, 5499, 2903, 5892]
    },

    '2017_STL': {
        'C': [1058, 3452, 125, 1986, 2056, 2767],
        '1': [67, 3683, 5687, 3310, 1241, 254],
        '2': [1640, 2084, 1796, 302, 384, 862],
        '3': [2137, 2537, 597, 3719, 1511, 1676]
    },

    '2018_HOU': {
        'C': [4911, 1533, 4488, 3476, 254, 1678],
        '1': [2910, 1296, 1574, 1323, 148, 1619],
        '2': [4499, 2655, 3965, 1072, 2976, 4061],
        '3': [5006, 3593, 3374, 1778, 3075, 1723]
    },

    '2018_MI': {
        'C': [868, 2056, 217, 494, 3707, 2767],
        '1': [4003, 1241, 3357, 865, 195, 27],
        '2': [4541, 2869, 4967, 4917, 333, 2708],
        '3': [5422, 6090, 4130, 51, 70, 4027]
    }

}

advances = {

    '2015': {
        'Win Finals': [118, 1678, 1671, 5012],  # 4
        'Win Semis': [987, 2826, 4265, 2512],  # 4
        'Win Quarters': [148, 1114, 1923, 900, 1023, 2338, 3996, 1089],  # 8
        'Lost Quarters': [2056, 330, 492, 3944, 368, 359, 337, 144, 3132, 3476, 1255, 2526, 1325, 3339, 20, 1711]  # 16
    },

    '2016': {
        'Win Finals': [330, 2481, 120, 1086],
        'Win Semis': [2056, 1690, 3015, 1405],
        'Win Quarters': [148, 1678, 364, 2990, 195, 987, 1197, 1065],
        'Lost Quarters': [217, 3476, 4678, 188, 2122, 2052, 3538, 41, 1501, 1986, 5050, 4828, 694, 3339, 379, 1511]
    },

    '2017_HOU': {
        'Win Finals': [973, 1011, 2928, 5499],
        'Win Semis': [118, 1678, 4188, 5892],
        'Win Quarters': [2122, 987, 4910, 6314, 604, 2848, 1868, 2903],
        'Lost Quarters': [5654, 2415, 2630, 4112, 1318, 2046, 1595, 2907]
    },

    '2017_STL': {
        'Win Finals': [2767, 254, 862, 1676],
        'Win Semis': [1986, 3310, 302, 3719],
        'Win Quarters': [2056, 1241, 384, 1511, 125, 5687, 1796, 597],
        'Lost Quarters': [3452, 3683, 2084, 2537, 1058, 67, 1640, 2137]
    },

    '2018_HOU': {
        'Win Finals': [254, 148, 2976, 3075],
        'Win Semis': [4911, 2910, 4499, 5006],
        'Win Quarters': [1678, 1619, 4061, 1723, 3476, 1323, 1072, 1778],
        'Lost Quarters': [4488, 1574, 3965, 3374, 1533, 1296, 2655, 3593]
    },

    '2018_MI': {
        'Win Finals': [2767, 27, 2708, 4027],
        'Win Semis': [217, 3357, 4967, 4130],
        'Win Quarters': [2056, 1241, 2869, 6090, 3707, 195, 333, 70],
        'Lost Quarters': [868, 4003, 4541, 5422, 494, 865, 4917, 51]
    }

}

points = {}

highest = 16.7  # todo This value can be toggled
# it reflects the point value that either the captain or the event winner receives
# 16.7 makes it so that all other teams are basically a percentage of the top team

for comp in years:
    for ranking_class in years[comp]:
        for team in years[comp][ranking_class]:
            points[team] = 0

for comp in years:
    for ranking_class in years[comp]:
        for team in years[comp][ranking_class]:
            if ranking_class == 'C':
                points[team] += highest
            elif ranking_class == '1':
                points[team] += highest * 0.75
            elif ranking_class == '2':
                points[team] += highest * 0.5
            elif ranking_class == '3':
                points[team] += highest * 0.25
            else:
                raise Exception

for comp in advances:
    for advancement_class in advances[comp]:
        for team in advances[comp][advancement_class]:
            if advancement_class == 'Win Finals':
                points[team] += highest
            elif advancement_class == 'Win Semis':
                points[team] += highest * 0.75
            elif advancement_class == 'Win Quarters':
                points[team] += highest * 0.5
            elif advancement_class == 'Lost Quarters':
                points[team] += highest * 0.25
            else:
                raise Exception

ranked = sorted(points, key=lambda team_: points[team_], reverse=True)

for team in ranked:
    space1 = ""
    space2 = ""

    rank_len = len(str(ranked.index(team) + 1))
    if rank_len == 1:
        space1 = "  "
    elif rank_len == 2:
        space1 = " "
    elif rank_len == 3:
        space1 = ""
    else:
        raise Exception

    team_len = len(str(team))
    if team_len == 2:
        space2 = "  "
    elif team_len == 3:
        space2 = " "
    elif team_len == 4:
        space2 = ""
    else:
        raise Exception

    print(str(ranked.index(team) + 1) + ". " + space1 + str(team) + space2 + " | pts: " + str(int(points[team])))