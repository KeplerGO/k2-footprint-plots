from matplotlib import pyplot as pl
from matplotlib import style
from matplotlib.ticker import MultipleLocator
import matplotlib.patheffects as path_effects
from K2fov import plot

from fieldplot import annotate_target

CAMPAIGN = 6

style.use('gray.mplstyle')
p = plot.K2FootprintPlot(figsize=(11, 11))
p.plot_campaign(CAMPAIGN, annotate_channels=False, facecolor='white', lw=1)


# Plot the Ruprecht 147 cluster
import pandas as pd
df = pd.read_csv('catalogs/ruprecht147.csv')
for member in df.iterrows():
    annotate_target(member[1].RA_d, member[1].DEC_d, "", size=10, color='#c0392b')
text = pl.text(288.8 - 0.6, -16.5, 'Ruprecht 147', style='italic', color='#c0392b',
               zorder=999, fontsize=30, va='center')
text.set_path_effects([path_effects.Stroke(linewidth=4, foreground='white'),
                       path_effects.Normal()])


annotate_target(201.29824736, -11.16131949, "Spica")

pl.suptitle('K2 Campaign {}'.format(CAMPAIGN), fontsize=44)
pl.xlim([213, 197])
pl.ylim([-19, -2.5])
p.ax.xaxis.set_major_locator(MultipleLocator(2))
p.ax.yaxis.set_major_locator(MultipleLocator(2))
pl.tight_layout()
for extension in ['png', 'eps']:
    pl.savefig('k2-c{}-field.{}'.format(CAMPAIGN, extension), dpi=100)
pl.close()
