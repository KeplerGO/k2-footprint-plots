from matplotlib import pyplot as pl
from matplotlib import style
from matplotlib.ticker import MultipleLocator
import matplotlib.patheffects as path_effects
from K2fov import plot

from fieldplot import annotate_target

CAMPAIGN = 18

style.use('gray.mplstyle')
p = plot.K2FootprintPlot(figsize=(11, 11))
p.plot_campaign(5, annotate_channels=False, facecolor='#888888', lw=0)
p.plot_campaign(16, annotate_channels=False, facecolor='#aaaaaa', lw=0)
p.plot_campaign(CAMPAIGN, annotate_channels=False, facecolor='white', lw=1)

pl.annotate('C18 overlaps\nwith C5', xy=(125.7, 23.5), xycoords='data', ha='center',
            xytext=(40, 40), textcoords='offset points',
            size=30, zorder=99999, color='#888888',
            arrowprops=dict(arrowstyle="simple",
                            fc="#888888", ec="none",
                            connectionstyle="arc3,rad=0.0"),
            )
pl.annotate('C16', xy=(141.2, 22.5), xycoords='data', ha='center',
            xytext=(-40, 40), textcoords='offset points',
            size=30, zorder=99999, color='#aaaaaa',
            arrowprops=dict(arrowstyle="simple",
                            fc="#aaaaaa", ec="none",
                            connectionstyle="arc3,rad=0.0"),
            )

annotate_target(127.578771, +22.235908, "K2-34")
annotate_target(126.61603759, +10.08037466, "HIP 41378")

# Plot the Beehive cluster
import pandas as pd
df = pd.read_csv('catalogs/beehive.csv')
for member in df.iterrows():
    annotate_target(member[1].RA_d, member[1].DEC_d, "", size=10, color='#c0392b')
text = pl.text(130., 20.5, 'M44 (Beehive)', style='italic', color='black',
               zorder=999, fontsize=30, va='center', ha='center')
text.set_path_effects([path_effects.Stroke(linewidth=4, foreground='white'),
                       path_effects.Normal()])

# Plot the M67 cluster
df = pd.read_csv('catalogs/m67.csv')
for member in df.iterrows():
    annotate_target(member[1].RA_d, member[1].DEC_d, "", size=10, color='#c0392b')
text = pl.text(132.8250 - 0.6, +11.8000, 'M67', style='italic', color='black',
               zorder=999, fontsize=30, va='center')
text.set_path_effects([path_effects.Stroke(linewidth=4, foreground='white'),
                       path_effects.Normal()])


# Plot the M67 cluster
#df = pd.read_csv('catalogs/stello-m67-paper.txt')
#for member in df.iterrows():
#    annotate_target(member[1].RA, member[1].Dec, "", size=10, color='#c0392b')
#text = pl.text(132.8250 - 0.6, +11.8000, 'M67', style='italic', color='black',
#               zorder=999, fontsize=30, va='center')
#text.set_path_effects([path_effects.Stroke(linewidth=4, foreground='white'),
#                       path_effects.Normal()])

"""
df = pd.read_csv('catalogs/confirmed-planets.csv')
for member in df.iterrows():
    annotate_target(float(member[1].ra), float(member[1].dec), member[1]['name'], padding=0.5, zorder=9e99)
"""

pl.suptitle('K2 Campaign {}'.format(CAMPAIGN), fontsize=44)
pl.xlim([144, 120.5])
pl.ylim([9.5, 27])
p.ax.xaxis.set_major_locator(MultipleLocator(2))
p.ax.yaxis.set_major_locator(MultipleLocator(2))
pl.tight_layout()
for extension in ['png', 'eps']:
    pl.savefig('k2-c{}-field.{}'.format(CAMPAIGN, extension), dpi=100)
pl.close()
