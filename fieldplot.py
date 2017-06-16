"""Helper functions for creating K2 field plots."""
from matplotlib import pyplot as pl
import matplotlib.patheffects as path_effects
from matplotlib.patches import Ellipse


def annotate_target(ra, dec, text, ha='left', size=120, color='black',
                    extended=False, globular=False, padding=0.22, zorder=999):
    if extended:
        padding = 1.82 * padding
        el = Ellipse((ra, dec), width=0.5, height=0.18, zorder=zorder-1,
                     facecolor='#888888', edgecolor=color, lw=2.)
        pl.axes().add_artist(el)
    elif globular:
        pl.scatter(ra, dec, zorder=zorder-1, marker='o', lw=1.7, s=size, edgecolor=color, color="None")
        pl.scatter(ra, dec, zorder=zorder-1, marker='+', lw=1.7, s=size, c=color)
    else:
        pl.scatter(ra, dec, zorder=zorder-1, marker='o', lw=0, s=size, c=color)
    if ha == 'left':
        padding = -padding
    text = pl.text(ra + padding, dec, text, zorder=zorder, fontsize=22, va='center', ha=ha, color=color)
    text.set_path_effects([path_effects.Stroke(linewidth=4, foreground='white'),
                           path_effects.Normal()])
