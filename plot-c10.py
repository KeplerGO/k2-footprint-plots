from matplotlib import pyplot as pl
from matplotlib import style
from matplotlib.ticker import MultipleLocator
import matplotlib.patheffects as path_effects
from K2fov import plot

from fieldplot import annotate_target

CAMPAIGN = 10

style.use('gray.mplstyle')
p = plot.K2FootprintPlot(figsize=(11, 11))
p.plot_campaign(1, annotate_channels=False, facecolor='#aaaaaa', lw=0)
p.plot_campaign(CAMPAIGN, annotate_channels=False, facecolor='white', lw=1)

pl.annotate('C1', xy=(179, -1), xycoords='data', ha='center',
            xytext=(-20, 40), textcoords='offset points',
            size=30, zorder=99999, color='#aaaaaa',
            arrowprops=dict(arrowstyle="simple",
                            fc="#aaaaaa", ec="none",
                            connectionstyle="arc3,rad=0.0"),
            )

annotate_target(187.27789633, 2.05240632, "3C 273")
annotate_target(180.44154, -3.76128, "PG 1159", ha='right')

# Comet 67P/Churyumov–Gerasimenko
ra = [183.52782, 183.88735, 184.25304, 184.62468, 185.00206, 185.38496, 185.96925]
dec = [2.26594, 2.06734, 1.86721, 1.66563, 1.46267, 1.25842, 0.94979]
pl.plot(ra, dec, lw=4, zorder=1500, c='#2980b9', ls='dashed')
text = pl.text(184.5, 1.4, '67P', zorder=1999, style='italic',
               fontsize=22, va='center', color='#2980b9')
text.set_path_effects([path_effects.Stroke(linewidth=4, foreground='white'),
                       path_effects.Normal()])

# Plot nearby galaxies
import pandas as pd
df = pd.read_csv('catalogs/c10-galaxies.csv')
for member in df.iterrows():
    annotate_target(member[1].ra, member[1].dec, "", size=5, color='#27ae60')
text = pl.text(186, -4, 'Galaxies', style='italic', color='#27ae60',
               zorder=999, fontsize=30, va='center', ha='center')
text.set_path_effects([path_effects.Stroke(linewidth=4, foreground='white'),
                       path_effects.Normal()])


pl.suptitle('K2 Campaign {}'.format(CAMPAIGN), fontsize=44)
pl.xlim([194.5, 178.5])
pl.ylim([-11.8, 5.])
p.ax.xaxis.set_major_locator(MultipleLocator(2))
p.ax.yaxis.set_major_locator(MultipleLocator(2))
pl.tight_layout()
for extension in ['png', 'eps']:
    pl.savefig('k2-c{}-field.{}'.format(CAMPAIGN, extension), dpi=100)
pl.close()
