"""Helper functions for creating K2 field plots."""
from matplotlib import pyplot as pl
import matplotlib.patheffects as path_effects
from matplotlib.patches import Ellipse


def annotate_target(ra, dec, text, ha='left', size=120, color='black', extended=False):
    if extended:
        padding = -0.4
        el = Ellipse((ra, dec), width=0.5, height=0.18, zorder=900,
                     facecolor='#888888', edgecolor=color, lw=2.)
        pl.axes().add_artist(el)
    else:
        padding = -0.22
        pl.scatter(ra, dec, zorder=900, marker='o', lw=0, s=size, c=color)
    if ha == 'right':
        padding = -padding
    text = pl.text(ra + padding, dec, text, zorder=999, fontsize=22, va='center', ha=ha, color=color)
    text.set_path_effects([path_effects.Stroke(linewidth=4, foreground='white'),
                           path_effects.Normal()])
