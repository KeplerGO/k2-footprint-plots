from matplotlib import pyplot as pl
from matplotlib import style
from matplotlib.ticker import MultipleLocator
import matplotlib.patheffects as path_effects
from K2fov import plot

from fieldplot import annotate_target

CAMPAIGN = 19

style.use('gray.mplstyle')
p = plot.K2FootprintPlot(figsize=(11, 11))
#p.plot_ecliptic()
p.plot_campaign(3, annotate_channels=False, facecolor='#aaaaaa', lw=0)
p.plot_campaign(12, annotate_channels=False, facecolor='#bbbbbb', lw=0)
p.plot_campaign(CAMPAIGN, annotate_channels=False, facecolor='white', lw=1)

pl.annotate('C3', xy=(344, -11), xycoords='data',
            xytext=(-60, -60), textcoords='offset points',
            size=30, zorder=99999, color='#aaaaaa',
            arrowprops=dict(arrowstyle="simple",
                            fc="#aaaaaa", ec="none",
                            connectionstyle="arc3,rad=0.0"),
            )
pl.annotate('C12', xy=(355., -11.2), xycoords='data',
            xytext=(-60, -60), textcoords='offset points',
            size=30, zorder=99999, color='#bbbbbb',
            arrowprops=dict(arrowstyle="simple",
                            fc="#bbbbbb", ec="none",
                            connectionstyle="arc3,rad=0.0"),
            )

annotate_target(346.62233, -5.04144, "TRAPPIST-1")
annotate_target(351.77015194, -1.28627266, "GJ 9827")

#annotate_target(348.9490380, -10.8496960, "K2-YYY")

# Neptune
import pandas as pd
df = pd.read_csv('catalogs/coordinates_neptune_around_minimum_motion.csv')
pl.plot(df.ra, df.dec, lw=4, zorder=500, c='#2980b9')
text = pl.text(347.8, -6.2, 'Neptune', zorder=999, style='italic',
               fontsize=22, va='center', color='#2980b9')
text.set_path_effects([path_effects.Stroke(linewidth=4, foreground='white'),
                       path_effects.Normal()])

# 2P/Encke
import numpy as np
encke_ra = np.array([ 352.76322,  352.85889,  352.94177,  353.01157,  353.06801,
                      353.1108 ,  353.13966,  353.15432,  353.15449,  353.13992,
                      353.11035,  353.06552,  353.00521,  352.92918,  352.83723,
                      352.72917])
encke_dec = np.array([-2.61381, -2.54609, -2.48333, -2.42564, -2.37315, -2.32596,
                      -2.2842 , -2.24799, -2.21744, -2.19267, -2.17377, -2.16087,
                      -2.15407, -2.15345, -2.15912, -2.17115])
pl.plot(encke_ra, encke_dec, lw=4, zorder=500, c='#2980b9')
text = pl.text(352.6, -2.4, '2P/Encke', zorder=999, style='italic',
               fontsize=22, va='center', color='#2980b9')
text.set_path_effects([path_effects.Stroke(linewidth=4, foreground='white'),
                       path_effects.Normal()])

pl.suptitle('K2 Campaign {}'.format(CAMPAIGN), fontsize=44)
pl.xlim([356.5, 339.])
pl.ylim([-13.5, 5.5])
p.ax.xaxis.set_major_locator(MultipleLocator(2))
p.ax.yaxis.set_major_locator(MultipleLocator(2))
pl.tight_layout()
for extension in ['png', 'eps']:
    pl.savefig('k2-c{}-field.{}'.format(CAMPAIGN, extension), dpi=100)
pl.close()
