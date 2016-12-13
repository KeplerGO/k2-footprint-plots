from matplotlib import pyplot as pl
from matplotlib import style
from matplotlib.ticker import MultipleLocator
import matplotlib.patheffects as path_effects
from K2fov import plot

from fieldplot import annotate_target

CAMPAIGN = 15

style.use('gray.mplstyle')
p = plot.K2FootprintPlot(figsize=(11, 11))
#p.plot_ecliptic()
p.plot_campaign(2, annotate_channels=False, facecolor='#aaaaaa', lw=0)
p.plot_campaign(CAMPAIGN, annotate_channels=False, facecolor='white', lw=1)

pl.annotate('C2', xy=(241.1, -18.3), xycoords='data',
            xytext=(40, 40), textcoords='offset points',
            size=30, zorder=99999, color='#aaaaaa',
            arrowprops=dict(arrowstyle="simple",
                            fc="#aaaaaa", ec="none",
                            connectionstyle="arc3,rad=0.0"),
            )

annotate_target(233.97117, -14.22006, "HP Lib")
annotate_target(229.98062, -25.00681, "GW Lib")
annotate_target(240.48106314, -21.98038959, "HIP 78530")
annotate_target(226.948721, -16.460728, "L5 Dwarf", ha='right')
annotate_target(232.39476389, -17.44094162, "33 Lib")


# Plot Upper Sco
import pandas as pd
df = pd.read_csv('catalogs/upper-sco.csv')
for member in df.iterrows():
    annotate_target(member[1].RA_d, member[1].DEC_d, "", size=15, color='#c0392b')
text = pl.text(240.2, -23.2, 'Upper Sco', style='italic', color='#c0392b',
               zorder=999, fontsize=30, va='center', ha='center')
text.set_path_effects([path_effects.Stroke(linewidth=4, foreground='white'),
                       path_effects.Normal()])


pl.suptitle('K2 Campaign {}'.format(CAMPAIGN), fontsize=44)
pl.xlim([242.5, 225.5])
pl.ylim([-27.5, -11.5])
p.ax.xaxis.set_major_locator(MultipleLocator(2))
p.ax.yaxis.set_major_locator(MultipleLocator(2))
pl.tight_layout()
for extension in ['png', 'eps']:
    pl.savefig('k2-c{}-field.{}'.format(CAMPAIGN, extension), dpi=100)
pl.close()
