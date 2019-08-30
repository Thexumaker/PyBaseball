import numpy as np
import matplotlib
import matplotlib.pyplot as plt
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


c = mcolors.ColorConverter().to_rgb
rvb = make_colormap([c('blue'), c('lightskyblue'), .20, c('lightsalmon'),c('salmon'), .30, c('salmon'),c('red')])

StrikeZonex = [1,2,3]
StrikeZoney = [-1.5,0,1.5]

z = np.array([[0.357, 0.333, 0.286], [0.349, 0.429, 0.292], [0.238, 0.256, 0.5]])
fig, ax = plt.subplots()
for i in range(len(StrikeZoney)):
    for j in range(len(StrikeZonex)):
        text = ax.text(j, i, z[i, j],
                       ha="center", va="center", color="black")

im = ax.imshow(z,cmap = rvb)
fig.tight_layout()

plt.show()
