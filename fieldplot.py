"""Helper functions for creating K2 field plots."""
from matplotlib import pyplot as pl
import matplotlib.patheffects as path_effects
from matplotlib.patches import Ellipse


def annotate_target(ras, decs, texts, ha='left',
                    extended=False, globular=False, padding=0.22, fontsize=22, **kwargs):
    if not hasattr(ras, '__iter__'):
        ras = [ras]
        decs = [decs]
        texts = [texts]

    if extended:
        for ra, dec in zip(ras, decs):
            padding = 1.82 * padding
            el = Ellipse((ra, dec), width=0.5, height=0.18,
                         facecolor='#888888', lw=2.)
            pl.axes().add_artist(el)
    else:
        pl.plot(ras, decs, **kwargs)
    if ha == 'left':
        padding = -padding
    for ra, dec, text in zip(ras, decs, texts):
        text = pl.text(ra + padding, dec, text, zorder=kwargs['zorder']+1,
                       fontsize=fontsize, va='center', ha=ha)
        text.set_path_effects([path_effects.Stroke(linewidth=4, foreground='white'),
                               path_effects.Normal()])
