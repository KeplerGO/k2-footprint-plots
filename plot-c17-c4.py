from matplotlib import pyplot as pl
from matplotlib import style
from matplotlib.ticker import MultipleLocator
import matplotlib.patheffects as path_effects
from K2fov import plot

from fieldplot import annotate_target

CAMPAIGN = 1713

style.use('gray.mplstyle')
p = plot.K2FootprintPlot(figsize=(11, 11))
p.plot_campaign(4, annotate_channels=False, facecolor='#aaaaaa', lw=0)
p.plot_campaign(13, annotate_channels=False, facecolor='#aaaaaa', lw=0)
p.plot_campaign(CAMPAIGN, annotate_channels=False, facecolor='white', lw=1)

pl.annotate('C2', xy=(241.1, -18.3), xycoords='data',
            xytext=(40, 40), textcoords='offset points',
            size=30, zorder=99999, color='#aaaaaa',
            arrowprops=dict(arrowstyle="simple",
                            fc="#aaaaaa", ec="none",
                            connectionstyle="arc3,rad=0.0"),
            )

# Plot Pleiades
import pandas as pd
df = pd.read_csv('catalogs/pleiades.csv')
for member in df.iterrows():
    annotate_target(member[1].RA_d, member[1].DEC_d, "", size=15, color='#c0392b')

text = pl.text(67.9, 25.5, 'Taurus-Auriga', style='italic', color='#c0392b',
               zorder=999, fontsize=30, va='center', ha='center')
text.set_path_effects([path_effects.Stroke(linewidth=4, foreground='white'),
                       path_effects.Normal()])


# Plot the Hyades cluster
df = pd.read_csv('catalogs/hyades.csv')
for member in df.iterrows():
    annotate_target(member[1].RA_d, member[1].DEC_d, "", size=15, color='#c0392b')

text = pl.text(67, 16, 'Hyades', style='italic', color='#c0392b',
               zorder=999, fontsize=30, va='center', ha='center')
text.set_path_effects([path_effects.Stroke(linewidth=4, foreground='white'),
                       path_effects.Normal()])

# Plot Taurus
df = pd.read_csv('catalogs/taurus-auriga.csv')
for member in df.iterrows():
    annotate_target(member[1]._RAJ2000, member[1]._DEJ2000, "", size=15, color='#c0392b')

text = pl.text(67.9, 25.5, 'Taurus-Auriga', style='italic', color='#c0392b',
               zorder=999, fontsize=30, va='center', ha='center')
text.set_path_effects([path_effects.Stroke(linewidth=4, foreground='white'),
                       path_effects.Normal()])


"""
annotate_target(233.97117, -14.22006, "HP Lib")
annotate_target(229.98062, -25.00681, "GW Lib")
annotate_target(240.48106314, -21.98038959, "HIP 78530")
annotate_target(226.948721, -16.460728, "L5 Dwarf", ha='right')
annotate_target(232.39476389, -17.44094162, "33 Lib")

text = pl.text(240.2, -23.2, 'Upper Sco', style='italic',
               zorder=999, fontsize=22, va='center', ha='center')
text.set_path_effects([path_effects.Stroke(linewidth=4, foreground='white'),
                       path_effects.Normal()])
"""

pl.suptitle('K2 Campaign {}'.format(CAMPAIGN), fontsize=44)
pl.xlim([77, 53])
pl.ylim([10, 30])
p.ax.xaxis.set_major_locator(MultipleLocator(2))
p.ax.yaxis.set_major_locator(MultipleLocator(2))
pl.tight_layout()
pl.savefig('k2-c{}-field.png'.format(CAMPAIGN), dpi=100)
pl.close()
