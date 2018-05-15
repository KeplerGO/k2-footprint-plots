# -*- coding: utf-8 -*-
from matplotlib import pyplot as pl
from matplotlib import style
from matplotlib.ticker import MultipleLocator
import matplotlib.patheffects as path_effects
from astropy.coordinates import SkyCoord
import astropy.units as u
from K2fov import plot

from fieldplot import annotate_target

CAMPAIGN = 2

style.use('gray.mplstyle')
p = plot.K2FootprintPlot(figsize=(11, 11))
#p.plot_campaign(11, annotate_channels=False, facecolor='#aaaaaa', lw=0)
#p.plot_campaign(15, annotate_channels=False, facecolor='#aaaaaa', lw=0)

p.plot_campaign(CAMPAIGN, annotate_channels=False, facecolor='white', lw=1)

#pl.annotate('C11', xy=(255.25, -16.75), xycoords='data', ha='center',
#            xytext=(40, 40), textcoords='offset points',
#            size=30, zorder=99999, color='#aaaaaa',
#            arrowprops=dict(arrowstyle="simple",
#                            fc="#aaaaaa", ec="none",
#                            connectionstyle="arc3,rad=0.0"),
#            )


#pl.annotate('C15', xy=(239, -17.), xycoords='data', ha='center',
#            xytext=(-30, 40), textcoords='offset points',
#            size=30, zorder=99999, color='#aaaaaa',
#            arrowprops=dict(arrowstyle="simple",
#                            fc="#aaaaaa", ec="none",
#                            connectionstyle="arc3,rad=0.0"),
#            )



# Plot Upper Sco
import pandas as pd
df = pd.read_csv('catalogs/upper-sco.csv')
for member in df.iterrows():
    annotate_target(member[1].RA_d, member[1].DEC_d, "", size=15, color='#c0392b')
text = pl.text(240.2, -20.5, 'Upper Sco', style='italic', color='#c0392b',
               zorder=999, fontsize=30, va='center', ha='center')
text.set_path_effects([path_effects.Stroke(linewidth=4, foreground='white'),
                       path_effects.Normal()])


c=SkyCoord('16 23 35.22','-26 31 32.7',unit=(u.hourangle,u.deg))
annotate_target(c.ra.deg,c.dec.deg, "M4", extended=True)

c=SkyCoord('16 17 02.41','-22 58 33.9',unit=(u.hourangle,u.deg))
annotate_target(c.ra.deg,c.dec.deg, "M80", extended=True)

c=SkyCoord('16 25 35.11766','-23 26 49.8150',unit=(u.hourangle,u.deg))
annotate_target(c.ra.deg,c.dec.deg, u"ρ Oph", extended=True)

annotate_target(233.97117, -14.22006, "HP Lib (CV)")
annotate_target(229.98062, -25.00681, "GW Lib (CV)")
annotate_target(240.48106314, -21.98038959, "HIP 78530")
annotate_target(226.948721, -16.460728, "L5 Dwarf", ha='right')
annotate_target(232.39476389, -17.44094162, "33 Lib (CV)")
annotate_target(240.08335535, -22.62170643, u"δ Sco")
annotate_target(240.033579, -23.189292, "K2-38")
annotate_target(229.35167, -21.01011, "NGC 5897", ha='right', extended=True)

pl.xlim([256, 237])
pl.ylim([-31, -14])
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
