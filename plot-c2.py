# -*- coding: utf-8 -*-
from matplotlib import pyplot as pl
from matplotlib import style
from matplotlib.ticker import MultipleLocator
import matplotlib.patheffects as path_effects
from astropy.coordinates import SkyCoord
import astropy.units as u
from K2fov import plot
import pandas as pd
import numpy as np

from fieldplot import annotate_target
style.use('wendy.mplstyle')
colors = pl.rcParams["axes.prop_cycle"].by_key()["color"]
CAMPAIGN = 2

p = plot.K2FootprintPlot(figsize=(11, 11))
p.plot_campaign(CAMPAIGN, annotate_channels=False, facecolor='white',
                edgecolor=colors[5], lw=1, zorder=1)

df = pd.read_csv('catalogs/upper-sco.csv')
annotate_target(np.asarray(df.RA_d), np.asarray(df.DEC_d),
                [""]*len(df), marker='.', ls='', markersize=5, zorder=2, color=colors[1])
text = pl.text(240.2, -20.5, 'Upper Sco', style='italic',
               zorder=999, fontsize=20, va='center', ha='center', color=colors[1])
text.set_path_effects([path_effects.Stroke(linewidth=4, foreground='white'),
                       path_effects.Normal()])


c = SkyCoord('16 23 35.22', '-26 31 32.7', unit=(u.hourangle, u.deg))
annotate_target(c.ra.deg, c.dec.deg, "M4", extended=True, fontsize=15)

c = SkyCoord('16 17 02.41', '-22 58 33.9', unit=(u.hourangle, u.deg))
annotate_target(c.ra.deg, c.dec.deg, "M80", extended=True, fontsize=15)

c = SkyCoord('16 25 35.11766', '-23 26 49.8150', unit=(u.hourangle, u.deg))
annotate_target(c.ra.deg, c.dec.deg, u"ρ Oph", extended=True, fontsize=15)

annotate_target(240.48106314, -21.98038959, "HIP 78530", fontsize=15,
                zorder=5, marker='.', ls='', markersize=5)
annotate_target(240.08335535, -22.62170643, u"δ Sco", fontsize=15,
                zorder=5, marker='.', ls='', markersize=5)
annotate_target(240.033579, -23.189292, "K2-38", fontsize=15,
                zorder=5, marker='.', ls='', markersize=5)

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
