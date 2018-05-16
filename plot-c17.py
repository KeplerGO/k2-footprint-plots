from matplotlib import pyplot as pl
from matplotlib import style
from matplotlib.ticker import MultipleLocator
import matplotlib.patheffects as path_effects
from K2fov import plot
import numpy as np

from fieldplot import annotate_target
import pandas as pd
style.use('wendy.mplstyle')
colors = pl.rcParams["axes.prop_cycle"].by_key()["color"]
CAMPAIGN = 17

p = plot.K2FootprintPlot(figsize=(11, 11))
p.plot_campaign(6, annotate_channels=False, facecolor=colors[5],
                edgecolor=colors[5], lw=1, zorder=1)
p.plot_campaign(CAMPAIGN, annotate_channels=False, facecolor='white',
                edgecolor=colors[5], lw=1, zorder=2)

pl.annotate('C6', xy=(211, -7.7), xycoords='data',
            xytext=(-40, 40), textcoords='offset points',
            size=30, zorder=99999, color=colors[5],
            arrowprops=dict(arrowstyle="simple",
                            fc=colors[5], ec="none",
                            connectionstyle="arc3,rad=0.0"),
            )

# Planets

ylim = p.ax.get_ylim()
xlim = p.ax.get_xlim()
df = pd.read_csv('catalogs/k2candidates.csv',
                 comment='#').drop_duplicates(['pl_name']).dropna(subset=['pl_name'])
df = df[df.k2_campaign == 6]
df['pl_hostname'] = [d.split(' ')[0] for d in df['pl_name']]
df['pl_letter'] = [d.split(' ')[1] for d in df['pl_name']]
letters = np.asarray(df[['pl_hostname', 'pl_letter']].groupby(
    'pl_hostname')['pl_letter'].apply(lambda x: ''.join(x)))
df = df[['pl_hostname', 'ra', 'dec']].groupby('pl_hostname').max()
df['pl_letters'] = letters
ra, dec = np.asarray(df.ra), np.asarray(df.dec)
pl_names = np.asarray(['{} {}'.format(n, l) for n, l in zip(df.index, df.pl_letters)])
ok = (ra > np.min(xlim)) & (ra <= np.max(xlim)) & (dec > np.min(ylim)) & (dec <= np.max(ylim))
annotate_target(ra[ok], dec[ok], pl_names[ok], padding=0.2,
                zorder=10, fontsize=16, markersize=10, ls='', marker='.')


annotate_target(201.29824736, -11.16131949, "Spica",
                zorder=4, marker='o', markersize=5, color=colors[0])

pl.xlim([212.9, 195.5])
pl.ylim([-16., 1.2])
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
