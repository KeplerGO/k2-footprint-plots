from matplotlib import pyplot as pl
from matplotlib import style
from matplotlib.ticker import MultipleLocator
import matplotlib.patheffects as path_effects
import numpy as np
from K2fov import plot

from fieldplot import annotate_target

CAMPAIGN = 1

style.use('gray.mplstyle')
p = plot.K2FootprintPlot(figsize=(11, 11))
p.plot_campaign(1, annotate_channels=False, facecolor='#aaaaaa', lw=0)
p.plot_campaign(CAMPAIGN, annotate_channels=False, facecolor='white', lw=1)

pl.xlim([182, 166])
pl.ylim([-8, 10])
p.ax.xaxis.set_major_locator(MultipleLocator(2))
p.ax.yaxis.set_major_locator(MultipleLocator(2))
pl.tight_layout()

ylim=p.ax.get_ylim()
xlim=p.ax.get_xlim()
import pandas as pd
df=pd.read_csv('catalogs/k2candidates.csv',comment='#')
for ra,dec,name in zip(df.ra,df.dec,df.pl_name):
	if (ra>np.min(xlim)) and (ra<=np.max(xlim)) and (dec>np.min(ylim)) and (dec<=np.max(ylim)):
		annotate_target(ra, dec, name, padding=0.2, zorder=9e99, fontsize=16, size=60)


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

