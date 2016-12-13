from matplotlib import pyplot as pl
from matplotlib import style
from matplotlib.ticker import MultipleLocator
import matplotlib.patheffects as path_effects
from K2fov import plot

from K2fov import getKeplerFov
from K2fov.c9 import SUPERSTAMP
import numpy as np

from fieldplot import annotate_target

CAMPAIGN = 9

style.use('gray.mplstyle')
p = plot.K2FootprintPlot(figsize=(11, 11))
p.plot_campaign(11, annotate_channels=False, facecolor='#aaaaaa', lw=0)
p.plot_campaign(CAMPAIGN, annotate_channels=False, facecolor='white', lw=1)

pl.annotate('C11', xy=(263., -16.5), xycoords='data', ha='center',
            xytext=(-20, 40), textcoords='offset points',
            size=30, zorder=99999, color='#aaaaaa',
            arrowprops=dict(arrowstyle="simple",
                            fc="#aaaaaa", ec="none",
                            connectionstyle="arc3,rad=0.0"),
            )

# Plot the C9 microlensing superstamp
fov = getKeplerFov(9)
superstamp_patches = []
for ch in SUPERSTAMP["channels"]:
    v_col = SUPERSTAMP["channels"][ch]["vertices_col"]
    v_row = SUPERSTAMP["channels"][ch]["vertices_row"]
    radec = np.array([
                        fov.getRaDecForChannelColRow(int(ch),
                                                     v_col[idx],
                                                     v_row[idx])
                        for idx in range(len(v_col))
                      ])
    patch = pl.fill(radec[:, 0], radec[:, 1],
            lw=0, facecolor="#27ae60", zorder=100)
    superstamp_patches.append(patch)
text = pl.text(268.6, -27.6, 'Microlensing\nsuperstamp', color='#27ae60',
               zorder=999, fontsize=22, va='center', ha='left')
text.set_path_effects([path_effects.Stroke(linewidth=4, foreground='white'),
                       path_effects.Normal()])


"""
annotate_target(187.27789633, 2.05240632, "3C 273")
annotate_target(180.44154, -3.76128, "GW Vir", ha='right')
"""

# Mars was in the field when C9 started on April 21st
ra = [264.32006, 266.32142, 268.32035, 270.31586, 272.30694, 274.29257,
      276.27171, 278.24329, 280.20625, 282.15951]
dec = [-23.25199, -23.38232, -23.48986, -23.57480, -23.63741, -23.67799,
       -23.69692, -23.69462, -23.67157, -23.62832]
pl.plot(ra, dec, lw=4, zorder=1500, c='#2980b9', ls='dashed')
text = pl.text(266, -23, 'Mars', zorder=1999, style='italic',
               fontsize=22, va='center', color='#2980b9')
text.set_path_effects([path_effects.Stroke(linewidth=4, foreground='white'),
                       path_effects.Normal()])

"""
# Plot Lagoon nebula
import pandas as pd
df = pd.read_csv('catalogs/lagoon.csv')
for member in df.iterrows():
    annotate_target(member[1].ra, member[1].dec, "", size=5, color='#c0392b')
text = pl.text(270.5, -24.4, 'Lagoon Nebula', color='#c0392b',
               zorder=999, fontsize=22, va='center', ha='left')
text.set_path_effects([path_effects.Stroke(linewidth=4, foreground='white'),
                       path_effects.Normal()])


import pandas as pd
df = pd.read_csv('catalogs/c9-w33.csv')
for member in df.iterrows():
    annotate_target(member[1].ra, member[1].dec, "", size=5, color='#c0392b')
text = pl.text(273, -17.9, 'W33 (O-Type Stars)', color='#c0392b',
               zorder=999, fontsize=22, va='center', ha='left')
text.set_path_effects([path_effects.Stroke(linewidth=4, foreground='white'),
                       path_effects.Normal()])
"""

annotate_target(270.9042, -24.3867, "M8 (Lagoon Nebula)", extended=True)
annotate_target(273.5583, -17.9306, "W33 (OB stars)", extended=True)


pl.suptitle('K2 Campaign {}'.format(CAMPAIGN), fontsize=44)
pl.xlim([279.5, 262])
pl.ylim([-29.8, -12.5])
p.ax.xaxis.set_major_locator(MultipleLocator(2))
p.ax.yaxis.set_major_locator(MultipleLocator(2))
pl.tight_layout()
for extension in ['png', 'eps']:
    pl.savefig('k2-c{}-field.{}'.format(CAMPAIGN, extension), dpi=100)
pl.close()
