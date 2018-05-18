from matplotlib import pyplot as pl
from matplotlib import style
from matplotlib.ticker import MultipleLocator
import matplotlib.patheffects as path_effects
from K2fov import plot
from astropy.coordinates import SkyCoord
import astropy.units as u
from fieldplot import annotate_target
import numpy as np
import pandas as pd


CAMPAIGN = 1000

style.use('wendy.mplstyle')
colors = pl.rcParams["axes.prop_cycle"].by_key()["color"]

p = plot.K2FootprintPlot(figsize=(11, 11))
campaigns = np.arange(0, CAMPAIGN+1)
p.plot_campaign(CAMPAIGN, annotate_channels=False, facecolor='white',
                lw=1, edgecolor=colors[5], zorder=2)

df = pd.read_csv("catalogs/kepler-confirmed-planets.csv")
pl.scatter(df.ra, df.dec, zorder=99, s=5)
text = pl.text(285.5, 36.8, 'Black dots show\nconfirmed planets', zorder=999, style='italic',
               fontsize=16, va='center', ha='left')
text.set_path_effects([path_effects.Stroke(linewidth=1, foreground='white'),
                       path_effects.Normal()])

annotate_target(301.5643971, +44.4568869, "Tabby's Star", marker='.', zorder=5)
annotate_target(290.2208, +37.7717, "NGC 6791", extended=True, zorder=5)
annotate_target(295.3250, +40.1867, "NGC 6819", extended=True, zorder=5)
annotate_target(294.3208, +46.3883, "NGC 6811", extended=True, zorder=5)

annotate_target(285.679429, +50.241319, "Kepler-10b", zorder=5)
annotate_target(289.075729, +51.757433, "Kepler-16b", zorder=5)
annotate_target(298.652713, +43.955017, "Kepler-186f", zorder=5)

pl.xlim([303, 279])
pl.ylim([36.01, 53.99])
p.ax.xaxis.set_major_locator(MultipleLocator(2))
p.ax.yaxis.set_major_locator(MultipleLocator(2))
pl.tight_layout()


for extension in ['png', 'eps']:
    output_fn = 'output/kepler-field-notitle.{}'.format(extension)
    print('Writing {}'.format(output_fn))
    pl.savefig(output_fn, dpi=100)

pl.suptitle('Kepler field', fontsize=44)
for extension in ['png', 'eps']:
    output_fn = 'output/kepler-field.{}'.format(extension)
    print('Writing {}'.format(output_fn))
    pl.savefig(output_fn, dpi=100)

pl.close()
