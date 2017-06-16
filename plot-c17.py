from matplotlib import pyplot as pl
from matplotlib import style
from matplotlib.ticker import MultipleLocator
import matplotlib.patheffects as path_effects
from K2fov import plot

from fieldplot import annotate_target

CAMPAIGN = 17

style.use('gray.mplstyle')
p = plot.K2FootprintPlot(figsize=(11, 11))
p.plot_campaign(6, annotate_channels=False, facecolor='#aaaaaa', lw=0)
p.plot_campaign(CAMPAIGN, annotate_channels=False, facecolor='white', lw=1)

pl.annotate('C6', xy=(211, -7.7), xycoords='data',
            xytext=(-40, 40), textcoords='offset points',
            size=30, zorder=99999, color='#aaaaaa',
            arrowprops=dict(arrowstyle="simple",
                            fc="#aaaaaa", ec="none",
                            connectionstyle="arc3,rad=0.0"),
            )

# Plot C6 galaxies
import pandas as pd
df = pd.read_csv('catalogs/c6-kegs.csv')
pl.scatter(df.ra, df.dec, lw=0, facecolor='#27ae60', s=3, zorder=99)
#for member in df.iterrows():
#    annotate_target(member[1].ra, member[1].dec, "", size=5, color='#c0392b')

text = pl.text(203.5, -8.2, 'Galaxies', style='italic', color='#27ae60',
               zorder=999, fontsize=30, va='center', ha='center')
text.set_path_effects([path_effects.Stroke(linewidth=4, foreground='white'),
                       path_effects.Normal()])

annotate_target(201.29824736, -11.16131949, "Spica", padding=0.5, zorder=9e4)
annotate_target(208.77375, -5.44247222, "K2-99")
annotate_target(207.34954167, -12.2845, "K2-110")
#annotate_target(207.655875, -6.80402778, "Qatar-2")

pl.suptitle('K2 Campaign {}'.format(CAMPAIGN), fontsize=44)
pl.xlim([212.9, 195.5])
pl.ylim([-16., 1.2])
p.ax.xaxis.set_major_locator(MultipleLocator(2))
p.ax.yaxis.set_major_locator(MultipleLocator(2))
pl.tight_layout()
for extension in ['png', 'eps']:
    pl.savefig('k2-c{}-field.{}'.format(CAMPAIGN, extension), dpi=100)
pl.close()
