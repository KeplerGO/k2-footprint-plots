from matplotlib import pyplot as pl
from matplotlib import style
from matplotlib.ticker import MultipleLocator
import matplotlib.patheffects as path_effects
from K2fov import plot
import pandas as pd

from fieldplot import annotate_target

CAMPAIGN = 4
style.use('wendy.mplstyle')
colors = pl.rcParams["axes.prop_cycle"].by_key()["color"]

p = plot.K2FootprintPlot(figsize=(11, 11))
p.plot_campaign(CAMPAIGN, annotate_channels=False, facecolor='white',
                edgecolor=colors[5], lw=1, zorder=1)


# Plot the Hyades cluster
df = pd.read_csv('catalogs/hyades.csv')
for member in df.iterrows():
    annotate_target(member[1].RA_d, member[1].DEC_d, "", size=15, color='#c0392b')

text = pl.text(67, 16, 'Hyades', style='italic', color='black',
               zorder=999, fontsize=30, va='center', ha='center')
text.set_path_effects([path_effects.Stroke(linewidth=4, foreground='white'),
                       path_effects.Normal()])

# Plot Pleiades
import pandas as pd
df = pd.read_csv('catalogs/pleiades.csv')
for member in df.iterrows():
    annotate_target(member[1].RA_d, member[1].DEC_d, "", size=15, color='#c0392b')

text = pl.text(52.5, 24.3, 'Pleiades', style='italic', color='black',
               zorder=999, fontsize=30, va='center', ha='center')
text.set_path_effects([path_effects.Stroke(linewidth=4, foreground='white'),
                       path_effects.Normal()])


pl.xlim([69, 50.5])
pl.ylim([10.5, 28.9])
p.ax.xaxis.set_major_locator(MultipleLocator(2))
p.ax.yaxis.set_major_locator(MultipleLocator(2))
pl.tight_layout()

for extension in ['png', 'eps']:
    output_fn = 'output/k2-c{}-field-notitle.{}'.format(CAMPAIGN, extension)
    print('Writing {}'.format(output_fn))
    pl.savefig(output_fn, dpi=100)

pl.suptitle('K2 Campaign {}'.format(CAMPAIGN), fontsize=44)
for extension in ['png', 'eps']:
    output_fn = 'output/k2-c{}-field.{}'.format(CAMPAIGN, extension)
    print('Writing {}'.format(output_fn))
    pl.savefig(output_fn, dpi=100)

pl.close()
