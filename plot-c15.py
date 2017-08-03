from matplotlib import pyplot as pl
from matplotlib import style
from matplotlib.ticker import MultipleLocator
import matplotlib.patheffects as path_effects
from K2fov import plot

from fieldplot import annotate_target

CAMPAIGN = 15

style.use('gray.mplstyle')
p = plot.K2FootprintPlot(figsize=(11, 11))
#p.plot_ecliptic()
p.plot_campaign(2, annotate_channels=False, facecolor='#aaaaaa', lw=0)
p.plot_campaign(CAMPAIGN, annotate_channels=False, facecolor='white', lw=1)

pl.annotate('C2', xy=(241.1, -18.3), xycoords='data',
            xytext=(40, 40), textcoords='offset points',
            size=30, zorder=99999, color='#aaaaaa',
            arrowprops=dict(arrowstyle="simple",
                            fc="#aaaaaa", ec="none",
                            connectionstyle="arc3,rad=0.0"),
            )

annotate_target(233.97117, -14.22006, "HP Lib (CV)")
annotate_target(229.98062, -25.00681, "GW Lib (CV)")
annotate_target(240.48106314, -21.98038959, "HIP 78530")
annotate_target(226.948721, -16.460728, "L5 Dwarf", ha='right')
annotate_target(232.39476389, -17.44094162, "33 Lib (CV)")
annotate_target(240.08335535, -22.62170643, "δ Sco")
annotate_target(240.033579, -23.189292, "K2-38")
annotate_target(229.35167, -21.01011, "NGC 5897", ha='right', extended=True)

# Asteroid Ryugu
import numpy as np
ryugu_ra = np.array([220.78934,  221.53776,  222.42765,  223.44588,  224.58094,
                    225.82275,  227.16255,  228.59279,  230.10692,  231.69931,
                    233.36513,  235.10022,  236.90099,  238.76437,  240.68768,
                    242.66862,  244.70517,  246.79554,  248.93813,  251.13152,
                    253.37435,  255.66538,  258.00339])
ryugu_dec = np.array([-14.54573, -14.12125, -13.80579, -13.58672, -13.45223, -13.39143,
                   -13.39434, -13.45184, -13.55566, -13.69824, -13.87271, -14.07278,
                   -14.29266, -14.52705, -14.77101, -15.01996, -15.26963, -15.51599,
                   -15.75526, -15.98385, -16.19835, -16.39553, -16.57228])
pl.plot(ryugu_ra[7:14], ryugu_dec[7:14], lw=3, zorder=500, c='#2980b9')
text = pl.text(237.5, -13.9, 'Ryugu', zorder=999, style='italic',
               fontsize=22, va='center', color='#2980b9')
text.set_path_effects([path_effects.Stroke(linewidth=4, foreground='white'),
                       path_effects.Normal()])

# Plot Upper Sco
import pandas as pd
df = pd.read_csv('catalogs/upper-sco.csv')
for member in df.iterrows():
    annotate_target(member[1].RA_d, member[1].DEC_d, "", size=15, color='#c0392b')
text = pl.text(240.2, -20.5, 'Upper Sco', style='italic', color='#c0392b',
               zorder=999, fontsize=30, va='center', ha='center')
text.set_path_effects([path_effects.Stroke(linewidth=4, foreground='white'),
                       path_effects.Normal()])


pl.suptitle('K2 Campaign {}'.format(CAMPAIGN), fontsize=44)
pl.xlim([242.5, 225.5])
pl.ylim([-27.5, -11.5])
p.ax.xaxis.set_major_locator(MultipleLocator(2))
p.ax.yaxis.set_major_locator(MultipleLocator(2))
pl.tight_layout()
for extension in ['png', 'eps']:
    pl.savefig('k2-c{}-field.{}'.format(CAMPAIGN, extension), dpi=100)
pl.close()
