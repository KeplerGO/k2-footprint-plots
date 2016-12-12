"""Helper functions for creating K2 field plots."""
from matplotlib import pyplot as pl
import matplotlib.patheffects as path_effects


def annotate_target(ra, dec, text, ha='left', size=120, color='black'):
    padding = -0.22
    if ha == 'right':
        padding = -padding
    pl.scatter(ra, dec, zorder=900, marker='o', lw=0, s=size, c=color)
    text = pl.text(ra + padding, dec, text, zorder=999, fontsize=22, va='center', ha=ha, color=color)
    text.set_path_effects([path_effects.Stroke(linewidth=4, foreground='white'),
                           path_effects.Normal()])
