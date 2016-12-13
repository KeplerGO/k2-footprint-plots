from matplotlib import pyplot as pl
from matplotlib import style
from matplotlib.ticker import MultipleLocator
import matplotlib.patheffects as path_effects
from K2fov import plot

from fieldplot import annotate_target

CAMPAIGN = 8

style.use('gray.mplstyle')
p = plot.K2FootprintPlot(figsize=(11, 11))
p.plot_campaign(CAMPAIGN, annotate_channels=False, facecolor='white', lw=1)

# Plot Uranus
ra = [16.41021, 16.14871, 15.95146, 15.82737, 15.78226, 15.81879, 15.93655, 16.13242, 16.43159]
dec = [6.29616, 6.19422, 6.11846, 6.07251, 6.05868, 6.07797, 6.13011, 6.21367, 6.33902]
pl.plot(ra, dec, lw=4, zorder=500, c='#2980b9')
text = pl.text(16.9, 5.7, 'Uranus', zorder=999, style='italic',
               fontsize=22, va='center', color='#2980b9')
text.set_path_effects([path_effects.Stroke(linewidth=4, foreground='white'),
                       path_effects.Normal()])

annotate_target(16.2258, 2.1333, "IC 1613", extended=True)

pl.suptitle('K2 Campaign {}'.format(CAMPAIGN), fontsize=44)
pl.xlim([25, 8])
pl.ylim([-3, 15.])
p.ax.xaxis.set_major_locator(MultipleLocator(2))
p.ax.yaxis.set_major_locator(MultipleLocator(2))
pl.tight_layout()
for extension in ['png', 'eps']:
    pl.savefig('k2-c{}-field.{}'.format(CAMPAIGN, extension), dpi=100)
pl.close()
