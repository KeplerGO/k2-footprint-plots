from matplotlib import pyplot as pl
from matplotlib import style
from matplotlib.ticker import MultipleLocator
import matplotlib.patheffects as path_effects
from K2fov import plot
from astropy.coordinates import SkyCoord
import astropy.units as u
from fieldplot import annotate_target
import numpy as np
CAMPAIGN = 3

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

import pandas as pd
df=pd.read_csv('catalogs/neptune_c3.csv')

c=SkyCoord(np.asarray(df.ra,dtype=str),np.asarray(df.dec,dtype=str),unit=(u.hourangle,u.deg))
pl.plot(c.ra.deg, c.dec.deg, lw=4, zorder=500, c='#2980b9')
text = pl.text(339, -9.5, 'Neptune', zorder=999, style='italic',
               fontsize=22, va='center', color='#2980b9')
text.set_path_effects([path_effects.Stroke(linewidth=4, foreground='white'),
                       path_effects.Normal()])


pl.xlim([346, 328])
pl.ylim([-20, -1])
p.ax.xaxis.set_major_locator(MultipleLocator(2))
p.ax.yaxis.set_major_locator(MultipleLocator(2))
pl.tight_layout()


ylim=p.ax.get_ylim()
xlim=p.ax.get_xlim()
import pandas as pd
df = pd.read_csv('catalogs/k2candidates.csv', comment='#')
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
