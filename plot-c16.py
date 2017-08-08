from matplotlib import pyplot as pl
from matplotlib import style
from matplotlib.ticker import MultipleLocator
import matplotlib.patheffects as path_effects
from K2fov import plot

from fieldplot import annotate_target

CAMPAIGN = 16

style.use('gray.mplstyle')
p = plot.K2FootprintPlot(figsize=(11, 11))
#p.plot_ecliptic()
p.plot_campaign(5, annotate_channels=False, facecolor='#aaaaaa', lw=0)
p.plot_campaign(CAMPAIGN, annotate_channels=False, facecolor='white', lw=1)

pl.annotate('C5', xy=(127, 24), xycoords='data', ha='center',
            xytext=(0, 40), textcoords='offset points',
            size=30, zorder=99999, color='#aaaaaa',
            arrowprops=dict(arrowstyle="simple",
                            fc="#aaaaaa", ec="none",
                            connectionstyle="arc3,rad=0.0"),
            )

annotate_target(127.578771, +22.235908, "K2-34")

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

# Earth
ra = [136.64098, 137.61928, 138.59537, 139.56929, 140.54105,
      141.51069, 142.47824, 143.44371, 144.40715, 159.56868]
dec = [16.84930, 16.56961, 16.28518, 15.99608, 15.70240,
       15.40423, 15.10166, 14.79476, 14.48364, 9.00822]
pl.plot(ra, dec, lw=5, zorder=500, c='#2980b9', ls='dashed')
text = pl.text(139, 15.8, 'Earth', zorder=999, style='italic',
               fontsize=24, va='center', color='#2980b9')
text.set_path_effects([path_effects.Stroke(linewidth=4, foreground='white'),
                       path_effects.Normal()])



pl.suptitle('K2 Campaign {}'.format(CAMPAIGN), fontsize=44)
pl.xlim([142, 125.5])
pl.ylim([11.3, 27])
p.ax.xaxis.set_major_locator(MultipleLocator(2))
p.ax.yaxis.set_major_locator(MultipleLocator(2))
pl.tight_layout()
for extension in ['png', 'eps']:
    pl.savefig('k2-c{}-field.{}'.format(CAMPAIGN, extension), dpi=100)
pl.close()
