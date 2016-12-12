from matplotlib import pyplot as pl
from matplotlib import style
from matplotlib.ticker import MultipleLocator
import matplotlib.patheffects as path_effects
from K2fov import plot

from fieldplot import annotate_target

CAMPAIGN = 13

style.use('gray.mplstyle')
p = plot.K2FootprintPlot(figsize=(11, 11))
#p.plot_ecliptic()
p.plot_campaign(4, annotate_channels=False, facecolor='#aaaaaa', lw=0)
p.plot_campaign(CAMPAIGN, annotate_channels=False, facecolor='white', lw=1)

pl.annotate('C4', xy=(63.9, 25.3), xycoords='data', ha='center',
            xytext=(-40, 40), textcoords='offset points',
            size=30, zorder=99999, color='#aaaaaa',
            arrowprops=dict(arrowstyle="simple",
                            fc="#aaaaaa", ec="none",
                            connectionstyle="arc3,rad=0.0"),
            )


# Plot the Hyades cluster
import pandas as pd
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

# NGC 1817
pl.scatter(78.0625, +16.69, zorder=899, marker='o', lw=2, s=400,
           facecolor='black', alpha=0.5, edgecolor='None', label='M67')
text = pl.text(78.0625 + 0.3, +16.69, 'NGC 1817', zorder=999, ha='right',
              fontsize=22, va='center', color='black')
text.set_path_effects([path_effects.Stroke(linewidth=4, foreground='white'),
                       path_effects.Normal()])

# NGC 1746
pl.scatter(75.9583, +23.77, zorder=899, marker='o', lw=2, s=400,
           facecolor='black', alpha=0.5, edgecolor='None', label='M67')
text = pl.text(75.9583 + 0.3, +23.77, 'NGC 1746', zorder=999, ha='right',
              fontsize=22, va='center', color='black')
text.set_path_effects([path_effects.Stroke(linewidth=4, foreground='white'),
                       path_effects.Normal()])


annotate_target(68.98016279, +16.50930235, "Aldebaran", ha='right')
annotate_target(69.31157942, +18.54303399, "SZ Tau", ha='right')
annotate_target(70.73241667, 18.95816667, "Gliese 176", ha='right')
annotate_target(67.910154, +18.232681, "HL Tau")
annotate_target(69.824150, +22.350967, "LkCa 15", ha='right')

pl.suptitle('K2 Campaign {}'.format(CAMPAIGN), fontsize=44)
pl.xlim([82, 63.5])
pl.ylim([12.5, 29.9])
p.ax.xaxis.set_major_locator(MultipleLocator(2))
p.ax.yaxis.set_major_locator(MultipleLocator(2))
pl.tight_layout()
pl.savefig('k2-c{}-field.png'.format(CAMPAIGN), dpi=100)
pl.close()
