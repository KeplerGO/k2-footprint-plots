from matplotlib import pyplot as pl
from matplotlib import style
from matplotlib.ticker import MultipleLocator
import matplotlib.patheffects as path_effects
import numpy as np
from K2fov import plot
import pandas as pd

from fieldplot import annotate_target

CAMPAIGN = 1

style.use('wendy.mplstyle')
p = plot.K2FootprintPlot(figsize=(11, 11))
p.plot_campaign(CAMPAIGN, annotate_channels=False, facecolor='white',
                lw=1, edgecolor='#3498db', zorder=1)

pl.xlim([182, 166])
pl.ylim([-8, 10])
p.ax.xaxis.set_major_locator(MultipleLocator(2))
p.ax.yaxis.set_major_locator(MultipleLocator(2))
pl.tight_layout()

ylim = p.ax.get_ylim()
xlim = p.ax.get_xlim()
df = pd.read_csv('catalogs/k2candidates.csv',
                 comment='#').drop_duplicates(['pl_name']).dropna(subset=['pl_name'])
df = df[df.k2_campaign == CAMPAIGN]
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
