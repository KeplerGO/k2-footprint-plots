from matplotlib import pyplot as pl
from matplotlib import style
from matplotlib.ticker import MultipleLocator
import matplotlib.patheffects as path_effects
from K2fov import plot

from fieldplot import annotate_target

CAMPAIGN = 7

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


# Plot Pluto
ra = [284.29952, 284.14349, 284.02927, 283.96645,
      283.94460, 283.97556, 284.06026, 284.19801, 284.47543]
dec = [-20.95824, -20.99379, -21.02622, -21.05229, -
       21.07735, -21.09791, -21.11365, -21.12435, -21.13067]
pl.plot(ra, dec, lw=4, zorder=500, c='#2980b9')
text = pl.text(284.9, -21.5, 'Pluto', zorder=999, style='italic',
               fontsize=22, va='center', color='#2980b9')
text.set_path_effects([path_effects.Stroke(linewidth=4, foreground='white'),
                       path_effects.Normal()])

annotate_target(283.77517, -22.70147, "NGC 6717", extended=True)

pl.suptitle('K2 Campaign {}'.format(CAMPAIGN), fontsize=44)
pl.xlim([297, 279])
pl.ylim([-31.5, -14.1])
p.ax.xaxis.set_major_locator(MultipleLocator(2))
p.ax.yaxis.set_major_locator(MultipleLocator(2))
pl.tight_layout()
for extension in ['png', 'eps']:
    pl.savefig('k2-c{}-field.{}'.format(CAMPAIGN, extension), dpi=100)
pl.close()
