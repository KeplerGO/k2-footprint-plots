from matplotlib import pyplot as pl
from matplotlib import style
from matplotlib.ticker import MultipleLocator
import matplotlib.patheffects as path_effects
from K2fov import plot
from astropy.coordinates import SkyCoord
import astropy.units as u
from fieldplot import annotate_target
import numpy as np


CAMPAIGN = 0

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


c=SkyCoord('06 08 54.0','+24 20 00',unit=(u.hourangle,u.deg))
annotate_target(c.ra.deg,c.dec.deg, "M35", extended=True)

c=SkyCoord('06 55 00.9','+18 01 14',unit=(u.hourangle,u.deg))
annotate_target(c.ra.deg,c.dec.deg, "NGC 2304", extended=True)


pl.xlim([107, 89])
pl.ylim([12.5, 30])
p.ax.xaxis.set_major_locator(MultipleLocator(2))
p.ax.yaxis.set_major_locator(MultipleLocator(2))
pl.tight_layout()



ylim=p.ax.get_ylim()
xlim=p.ax.get_xlim()
import pandas as pd
df=pd.read_csv('catalogs/k2candidates.csv',comment='#')
for ra,dec,name in zip(df.ra,df.dec,df.pl_name):
	if (ra>np.min(xlim)) and (ra<=np.max(xlim)) and (dec>np.min(ylim)) and (dec<=np.max(ylim)):
		annotate_target(ra,dec,name)



df=pd.read_csv('catalogs/jupiter_c0.csv')

c = SkyCoord(np.asarray(df.ra,dtype=str), np.asarray(df.dec,dtype=str), unit=(u.hourangle,u.deg))
pl.plot(c.ra.deg, c.dec.deg, lw=4, zorder=500, c='#2980b9')
text = pl.text(104, 24, 'Jupiter', zorder=999, style='italic',
               fontsize=22, va='center', color='#2980b9')
text.set_path_effects([path_effects.Stroke(linewidth=4, foreground='white'),
                       path_effects.Normal()])

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
