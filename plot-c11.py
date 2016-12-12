from matplotlib import pyplot as pl
from matplotlib import style
from matplotlib.ticker import MultipleLocator
import matplotlib.patheffects as path_effects
from K2fov import plot

from fieldplot import annotate_target

CAMPAIGN = 11

style.use('gray.mplstyle')
p = plot.K2FootprintPlot(figsize=(11, 11))
#p.plot_ecliptic()
p.plot_campaign(2, annotate_channels=False, facecolor='#aaaaaa', lw=0)
p.plot_campaign(9, annotate_channels=False, facecolor='#aaaaaa', lw=0)
p.plot_campaign(CAMPAIGN, annotate_channels=False, facecolor='white', lw=1)

pl.annotate('C2', xy=(252.7, -17.7), xycoords='data', ha='center',
            xytext=(-20, 40), textcoords='offset points',
            size=30, zorder=99999, color='#aaaaaa',
            arrowprops=dict(arrowstyle="simple",
                            fc="#aaaaaa", ec="none",
                            connectionstyle="arc3,rad=0.0"),
            )
pl.annotate('C9', xy=(268.2, -29.4), xycoords='data', ha='center',
            xytext=(20, -60), textcoords='offset points',
            size=30, zorder=99999, color='#aaaaaa',
            arrowprops=dict(arrowstyle="simple",
                            fc="#aaaaaa", ec="none",
                            connectionstyle="arc3,rad=0.0"),
            )

# Enceladus
ra = [250.70991, 251.33324, 251.67648, 252.16695, 252.24086, 252.31723, 252.41537, 252.50826, 252.58352,
      252.67133, 252.77610, 252.86679]
dec = [-20.78633, -20.89085, -20.94270, -21.01640, -21.02371, -21.03990, -21.05554, -21.06268, -21.07266,
       -21.09061, -21.10378, -21.11041]
pl.plot(ra, dec, lw=4, zorder=500, c='#2980b9', ls='dashed')
text = pl.text(251.3, -22.2, 'Saturn\nTitan\nEnceladus', zorder=999, style='italic',
               fontsize=22, va='center', color='#2980b9', ha='right')
text.set_path_effects([path_effects.Stroke(linewidth=4, foreground='white'),
                       path_effects.Normal()])


annotate_target(260.14296371, -19.33374974, "HD 156846")
#annotate_target(256.52290757, -26.58056313, "BF Oph")
annotate_target(268.118363, -26.703469, "V767 Sgr")
annotate_target(255.03962888, -24.98907067, "26 Oph")
annotate_target(258.83743307, -26.60282143, "36 Oph", ha='right')
annotate_target(259.79908, -18.51625, "M9")
annotate_target(255.65704, -26.26794, "M19")
annotate_target(257.54342, -26.58172, "NGC 6293")
annotate_target(260.99437, -26.35342, "NGC 6355", ha='right')
annotate_target(267.02083, -24.78000, "Terzan 5")

pl.suptitle('K2 Campaign {}'.format(CAMPAIGN), fontsize=44)
pl.xlim([269.5, 251.])
pl.ylim([-32, -15])
p.ax.xaxis.set_major_locator(MultipleLocator(2))
p.ax.yaxis.set_major_locator(MultipleLocator(2))
pl.tight_layout()
pl.savefig('k2-c{}-field.png'.format(CAMPAIGN), dpi=100)
pl.close()
