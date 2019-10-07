from Models.backend import baseball
from Models import Person
currentDate = date.today()
from matplotlib.pylab import plt #load plot library
from matplotlib.collections import LineCollection
from matplotlib import colors as mcolors
def GenerateWpaGraph(GamePck):
    """Returns a list of the homeTeam wPA and generates the Win probability graph of a specified game """
    game = baseballs.get('game_winProbability', {'ver': 'v1','gamePk': GamePck})

    atbat = [0]
    home = 50

    homeL = [50]

    for item in game:
        for key, val in item.items():
            if key == 'atBatIndex':
                atbat.append(val)

            if key == 'homeTeamWinProbabilityAdded':

                home += val
                homeL.append(home)

    c = ['g' if a >= 50 else 'r' for a in homeL]
    lines = [((x0,y0), (x1,y1)) for x0, y0, x1, y1 in zip(atbat[:], homeL[:], atbat[1:], homeL[1:])]
    coloredLines = LineCollection(lines, colors = c, linewidths = (2,))
    fig,ax = plt.subplots(1)
    ax.add_collection(coloredLines)
    ax.autoscale_view()
    plt.show()
    return homeL
