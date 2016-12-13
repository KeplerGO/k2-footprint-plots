from matplotlib import pyplot as pl
from matplotlib import style
from matplotlib.ticker import MultipleLocator
import matplotlib.patheffects as path_effects
from K2fov import plot

from fieldplot import annotate_target

CAMPAIGN = 12

style.use('gray.mplstyle')
p = plot.K2FootprintPlot(figsize=(11, 11))
#p.plot_ecliptic()
p.plot_campaign(900, annotate_channels=False, facecolor='#aaaaaa', lw=0)
p.plot_campaign(CAMPAIGN, annotate_channels=False, facecolor='white', lw=1)


pl.annotate('Concept\nEngineering\nTest Field', xy=(359, -9.5), xycoords='data', ha='center',
            xytext=(30, -90), textcoords='offset points',
            size=20, zorder=99999, color='#aaaaaa',
            arrowprops=dict(arrowstyle="simple",
                            fc="#aaaaaa", ec="none",
                            connectionstyle="arc3,rad=0.0"),
            )

# Mars
ra = [337.39783, 339.20207, 341.54445, 343.97142, 346.47179,
      349.03614, 351.65659, 354.86614, 357.58887, 360.35097]
dec = [-10.99843, -10.08825, -8.91869, -7.71709, -6.48711,
       -5.23251, -3.95714, -2.40487, -1.09788, 0.21694]
pl.plot(ra, dec, lw=3, zorder=500, c='#2980b9', ls='dashed')
text = pl.text(344.6, -8.5, 'Mars', zorder=999, style='italic',
               fontsize=24, va='center', color='#2980b9')
text.set_path_effects([path_effects.Stroke(linewidth=4, foreground='white'),
                       path_effects.Normal()])

# Chiron
ra = [350.78015, 350.63320, 350.50260, 350.39154, 350.28257, 350.21294,
      350.16410, 350.13664, 350.13096, 350.14725, 350.19575, 350.26003,
      350.34877, 350.45856, 350.58923, 350.69247, 350.78611]
dec = [0.66906, 0.58728, 0.51093, 0.44190, 0.36781, 0.31381, 0.26782,
       0.23026, 0.20150, 0.18177, 0.17027, 0.17093, 0.18137, 0.20142,
       0.23096, 0.25711, 0.28239]
pl.plot(ra, dec, lw=4, zorder=500, c='#2980b9')
text = pl.text(349.9, 0.3, 'Chiron', zorder=999, style='italic',
               fontsize=22, va='center', color='#2980b9')
text.set_path_effects([path_effects.Stroke(linewidth=4, foreground='white'),
                       path_effects.Normal()])

annotate_target(353.616168, -1.580036, "WASP-28")
annotate_target(347.29469878, -02.26074375, "HD 218566")
annotate_target(346.62233, -5.04144, "TRAPPIST-1")

pl.suptitle('K2 Campaign {}'.format(CAMPAIGN), fontsize=44)
pl.xlim([360, 343.])
pl.ylim([-13.5, 5])
p.ax.xaxis.set_major_locator(MultipleLocator(2))
p.ax.yaxis.set_major_locator(MultipleLocator(2))
pl.tight_layout()
for extension in ['png', 'eps']:
    pl.savefig('k2-c{}-field.{}'.format(CAMPAIGN, extension), dpi=100)
pl.close()
