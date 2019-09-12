import matplotlib.pyplot as plt
import numpy as np
import matplotlib.colors as mcolors
def make_colormap(seq):
    """Return a LinearSegmentedColormap
    seq: a sequence of floats and RGB-tuples. The floats should be increasing
    and in the interval (0,1).
    """
    seq = [(None,) * 3, 0.0] + list(seq) + [1.0, (None,) * 3]
    cdict = {'red': [], 'green': [], 'blue': []}
    for i, item in enumerate(seq):
        if isinstance(item, float):
            r1, g1, b1 = seq[i - 1]
            r2, g2, b2 = seq[i + 1]
            cdict['red'].append([item, r1, r2])
            cdict['green'].append([item, g1, g2])
            cdict['blue'].append([item, b1, b2])
    return mcolors.LinearSegmentedColormap('CustomMap', cdict)

class Zone:
    def __init__(self,zone,color,temp,value):

        self.zone = zone #int
        self.color = color #rgb value
        self.temp = temp #string
        self.value = value #int
    def get():
        return [self.zone,self.color,self.temp,self.value]

class strikeZone(object):
    def __init__(self,name):
        self.name = name
        self.strikezone = dict.fromkeys([1,2,3,4,5,6,7,8,9])
    def updateStrikeZone(self,Zone, Zonedata):
        d = dict(zip(Zone,Zonedata))

        self.strikezone.update(d)
    def visualize(self):

        c = mcolors.ColorConverter().to_rgb
        rvb = make_colormap([c('blue'), c('lightskyblue'), .20, c('lightsalmon'),c('salmon'), .30, c('salmon'),c('red')])

        StrikeZonex = [1,2,3]
        StrikeZoney = [-1.5,0,1.5]
        row1 = []
        row2 = []
        row3 = []
        for i in range(1,4):
            row1.append(self.strikezone.get(i))
        for i in range(4,7):
            row2.append(self.strikezone.get(i))
        for i in range(7,10):
            row3.append(self.strikezone.get(i))



        z = np.array([row1, row2, row3])
        fig, ax = plt.subplots()
        for i in range(len(StrikeZoney)):
            for j in range(len(StrikeZonex)):
                text = ax.text(j, i, z[i, j],
                               ha="center", va="center", color="black")

        im = ax.imshow(z,cmap = rvb)
        fig.tight_layout()

        plt.show()
