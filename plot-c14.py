from matplotlib import pyplot as pl
from matplotlib import style
from K2fov import plot

from fieldplot import annotate_target

CAMPAIGN = 14

style.use('gray.mplstyle')
p = plot.K2FootprintPlot(figsize=(11, 11))
#p.plot_ecliptic()
p.plot_campaign(CAMPAIGN, annotate_channels=False, facecolor='white', lw=1)

annotate_target(164.120271, +07.014658, "Wolf 359")
annotate_target(160.602432, +07.435026, "WASP-104")
annotate_target(160.990554, +11.703611, "M95")
annotate_target(161.690600, +11.819939, "M96", ha='right')
annotate_target(161.956667, +12.581631, "M105")
annotate_target(158.20279865, +09.30658596, r'$\mathrm{\rho}$ Leo')

pl.suptitle('K2 Campaign {}'.format(CAMPAIGN), fontsize=44)
pl.xlim([168, 153])
pl.ylim([-1, 15.9])
pl.tight_layout()
pl.savefig('k2-c{}-field.png'.format(CAMPAIGN), dpi=100)
pl.close()
