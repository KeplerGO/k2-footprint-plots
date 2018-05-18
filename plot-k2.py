from matplotlib import pyplot as pl
from matplotlib import style
from matplotlib.ticker import MultipleLocator
import matplotlib.patheffects as path_effects
import numpy as np
from K2fov import plot
import pandas as pd
import numpy as np
from glob import glob
from astropy.coordinates import SkyCoord
import astropy.units as u
from fieldplot import annotate_target
from K2fov import getKeplerFov
from K2fov.c9 import SUPERSTAMP

EXTENSIONS = ['png', 'eps']

style.use('wendy.mplstyle')
colors = pl.rcParams["axes.prop_cycle"].by_key()["color"]
xlims = [[107, 89], [182, 166], [256, 237], [346, 328],
         [69, 50.5], [139, 122.5], [213, 197], [297, 279], [25, 8],
         [279.5, 262], [194.5, 178.5], [269.5, 251.], [360, 343.], [82, 63.5],
         [168, 153], [242.5, 225.5], [142, 125.5], [212.9, 195.5], [139, 121.5], [356.5, 339.]]
ylims = [[13.5, 31], [-7.5, 10.5], [-30, -13], [-20, -1],
         [10.5, 28.9], [9.5, 25.9], [-19, -2.5], [-31.5, -14.1], [-3, 15],
         [-29.8, -12.5], [-11.8, 5.], [-32, -15], [-13.5, 5], [12.5, 29.9],
         [-1, 15.9], [-27.5, -11.5], [11.3, 27], [-16, 1.2], [8.5, 26], [-13.5, 5.5]]

cluster_fnames = glob('catalogs/*.csv')


def annotate_planets(campaign):
    if campaign == 18:
        campaign = 5
    xlim = xlims[campaign]
    ylim = ylims[campaign]
    df = pd.read_csv('catalogs/k2candidates.csv',
                     comment='#').drop_duplicates(['pl_name']).dropna(subset=['pl_name'])
    df = df[df.k2_campaign == campaign]
    df['pl_hostname'] = [' '.join(d.split(' ')[0:-1]) for d in df['pl_name']]
    df['pl_letter'] = [d.split(' ')[-1] for d in df['pl_name']]
    letters = np.asarray(df[['pl_hostname', 'pl_letter']].groupby(
        'pl_hostname')['pl_letter'].apply(lambda x: ''.join(x)))
    df = df[['pl_hostname', 'ra', 'dec']].groupby('pl_hostname').max()
    df['pl_letters'] = letters
    ra, dec = np.asarray(df.ra), np.asarray(df.dec)
    pl_names = np.asarray(['{} {}'.format(n, l) for n, l in zip(df.index, df.pl_letters)])
    ok = (ra > np.min(xlim)) & (ra <= np.max(xlim)) & (dec > np.min(ylim)) & (dec <= np.max(ylim))
    annotate_target(ra[ok], dec[ok], pl_names[ok], padding=0.2,
                    zorder=10, fontsize=16, markersize=10, ls='', marker='.', color=colors[0])


def annotate_clusters(CAMPAIGN):
    xlim = xlims[CAMPAIGN]
    ylim = ylims[CAMPAIGN]
    for f in cluster_fnames:
        label = ' '.join([a.capitalize() for a in f.split('/')[-1][:-4].split('-')])
        try:
            df = pd.read_csv(f)
            annotate_target(np.asarray(df.RA_d), np.asarray(df.DEC_d),
                            [""]*len(df), marker='.', ls='', markersize=5, zorder=2, color=colors[1])
            ok = (df.RA_d > np.min(xlim)) & (df.RA_d <= np.max(xlim)) & (
                df.DEC_d > np.min(ylim)) & (df.DEC_d <= np.max(ylim))
            if np.any(ok):
                text = pl.text(df[ok].RA_d.mean(), df[ok].DEC_d.mean(), '{}'.format(label), style='italic',
                               zorder=999, fontsize=20, va='center', ha='center', color=colors[1])
                text.set_path_effects([path_effects.Stroke(linewidth=4, foreground='white'),
                                       path_effects.Normal()])
        except:
            continue


def annotate_moving(campaign):
    fnames = glob('catalogs/*_c{}.csv'.format(campaign))
    for f in fnames:
        df = pd.read_csv(f)
        c = SkyCoord(np.asarray(df.ra, dtype=str), np.asarray(
            df.dec, dtype=str), unit=(u.deg, u.deg))
        pl.plot(c.ra.deg, c.dec.deg, lw=4, zorder=500, c=colors[2])
        text = pl.text(df.ra.mean() + 0.35, df.dec.mean() + 0.35,
                       f.split('/')[-1].split('_')[0], zorder=999, style='italic',
                       fontsize=22, va='center', color=colors[2])
        text.set_path_effects([path_effects.Stroke(linewidth=4, foreground='white'),
                               path_effects.Normal()])


def annotate_supernova(CAMPAIGN):
    xlim = xlims[CAMPAIGN]
    ylim = ylims[CAMPAIGN]
    fnames = glob('catalogs/c{}-supernovae.csv'.format(CAMPAIGN))
    for f in fnames:
        df = pd.read_csv(f)
        c = SkyCoord(df.ra, df.dec, unit=(u.hourangle, u.deg))
        df['ra'] = c.ra.deg
        df['dec'] = c.dec.deg
        annotate_target(np.asarray(df.ra), np.asarray(df.dec),
                        np.asarray(df.name), fontsize=13, marker='.', ls='', markersize=10, zorder=2, color=colors[3], colortext=True)
        ok = (df.ra > np.min(xlim)) & (df.ra <= np.max(xlim)) & (
            df.dec > np.min(ylim)) & (df.dec <= np.max(ylim))
        if np.any(ok):
            text = pl.text(df[ok].ra.mean()+1, df[ok].dec.mean()+1, 'Supernovae', style='italic',
                           zorder=999, fontsize=30, va='center', ha='center', color=colors[3])
            text.set_path_effects([path_effects.Stroke(linewidth=4, foreground='white'),
                                   path_effects.Normal()])


def annotate_extended(CAMPAIGN):
    annotate_target(283.77517, -22.70147, "NGC 6717", extended=True, zorder=5, ha='right')
    c = SkyCoord('16 23 35.22', '-26 31 32.7', unit=(u.hourangle, u.deg))
    annotate_target(c.ra.deg, c.dec.deg, "M4", extended=True, zorder=5)
    c = SkyCoord('16 17 02.41', '-22 58 33.9', unit=(u.hourangle, u.deg))
    annotate_target(c.ra.deg, c.dec.deg, "M80", extended=True, zorder=5, ha='right')
    c = SkyCoord('16 25 35.11766', '-23 26 49.8150', unit=(u.hourangle, u.deg))
    annotate_target(c.ra.deg, c.dec.deg, u"ρ Oph", extended=True, zorder=5, ha='right')
    c = SkyCoord('06 08 54.0', '+24 20 00', unit=(u.hourangle, u.deg))
    annotate_target(c.ra.deg, c.dec.deg, "M35", extended=True, zorder=5)
    c = SkyCoord('06 55 00.9', '+18 01 14', unit=(u.hourangle, u.deg))
    annotate_target(c.ra.deg, c.dec.deg, "NGC 2304", extended=True, zorder=5)
    if CAMPAIGN != 11:
        annotate_target(270.9042, -24.3867, "M8 (Lagoon Nebula)", extended=True, zorder=5)
    annotate_target(273.5583, -17.9306, "W33 (OB stars)", extended=True, zorder=5)
    annotate_target(75.9583, +23.77, "NGC 1746", extended=True, ha='right', zorder=5)
    annotate_target(78.0625, +16.69, "NGC 1817", extended=True, ha='right', zorder=5)
    annotate_target(71.4792, +19.115, "NGC 1647", extended=True, ha='right', zorder=5)
    annotate_target(160.990554, +11.703611, "M95", extended=True, zorder=5)
    annotate_target(161.690600, +11.819939, "M96", extended=True, ha='right', zorder=5)
    annotate_target(161.956667, +12.581631, "M105", extended=True, zorder=5)
    annotate_target(229.35167, -21.01011, "NGC 5897", ha='right', extended=True, zorder=5)

    annotate_target(259.79908, -18.51625, "M9", marker='d', color=colors[0], zorder=5)
    if CAMPAIGN != 2:
        annotate_target(255.65704, -26.26794, "M19", marker='d', color=colors[0], zorder=5)
    if CAMPAIGN != 2:
        annotate_target(257.54342, -26.58172, "NGC 6293", marker='d', color=colors[0], zorder=5)
    if CAMPAIGN != 9:
        annotate_target(260.99437, -26.35342, "NGC 6355", ha='right',
                        marker='d', color=colors[0], zorder=5)
    annotate_target(267.02083, -24.78000, "Terzan 5", marker='d', color=colors[0], zorder=5)

    annotate_target(260.14296371, -19.33374974, "HD 156846", color=colors[0], marker='.', zorder=5)
    if CAMPAIGN != 9:
        annotate_target(268.118363, -26.703469, "V767 Sgr", color=colors[0], marker='.', zorder=5)
    if CAMPAIGN != 2:
        annotate_target(255.03962888, -24.98907067, "26 Oph", color=colors[0], marker='.', zorder=5)
    annotate_target(258.83743307, -26.60282143, "36 Oph",
                    color=colors[0], marker='.', ha='right', zorder=5)
    annotate_target(353.616168, -1.580036, "WASP-28", color=colors[0], marker='.', zorder=5, ha='right')
    annotate_target(347.29469878, -02.26074375, "HD 218566", color=colors[0], marker='.', zorder=5)
    annotate_target(346.62233, -5.04144, "TRAPPIST-1", ha='right',
                    color=colors[0], marker='.', zorder=5)
    annotate_target(351.77015194, -1.28627266, "GJ 9827", ha='left',
                    color=colors[0], marker='.', zorder=5)
    annotate_target(348.9490380, -10.8496960, "K2-138", color=colors[0], marker='.', zorder=5)
    annotate_target(68.98016279, +16.50930235, "Aldebaran",
                    ha='right', color=colors[0], marker='.', zorder=5)
    annotate_target(201.29824736, -11.16131949, "Spica",
                    ha='left', color=colors[0], marker='.', zorder=5)
    annotate_target(69.31157942, +18.54303399, "SZ Tau", ha='right',
                    color=colors[0], marker='.', zorder=5)
    annotate_target(70.73241667, 18.95816667, "Gliese 176", color=colors[0], marker='.', zorder=5)
    annotate_target(67.910154, +18.232681, "HL Tau", color=colors[0], marker='.', zorder=5)
    annotate_target(69.824150, +22.350967, "LkCa 15", ha='right',
                    color=colors[0], marker='.', zorder=5)
    annotate_target(164.120271, +07.014658, "Wolf 359", ha='right',
                    color=colors[0], zorder=5, marker='.')
    annotate_target(160.602432, +07.435026, "WASP-104", ha='right',
                    color=colors[0], zorder=5, marker='.')
    annotate_target(158.20279865, +09.30658596,
                    r'$\mathrm{\rho}$ Leo', ha='right', color=colors[0], zorder=5, marker='.')
    annotate_target(233.97117, -14.22006, "HP Lib (CV)", color=colors[0], marker='.', zorder=5)
    annotate_target(229.98062, -25.00681, "GW Lib (CV)", color=colors[0], marker='.', zorder=5)
    annotate_target(240.48106314, -21.98038959, "HIP 78530", color=colors[0],
                    marker='.', zorder=5, ha='left')
    annotate_target(226.948721, -16.460728, "L5 Dwarf", ha='right',
                    color=colors[0], marker='.', zorder=5)
    annotate_target(232.39476389, -17.44094162, "33 Lib (CV)",
                    color=colors[0], marker='.', zorder=5)
    annotate_target(240.08335535, -22.62170643, "δ Sco", color=colors[0], marker='.', zorder=5)
    if CAMPAIGN != 16:
        annotate_target(126.61603759, +10.08037466, "HIP 41378",
                        color=colors[0], marker='.', zorder=5, ha='right')
    if CAMPAIGN != 16:
        annotate_target(133.70364554, +20.10851139, "OJ 287", ha='right', extended=True, zorder=5)
    annotate_target(187.27789633, +2.05240633, "3C 273", ha='right', extended=True, zorder=5)
    annotate_target(71.4792, +19.115, "NGC 1647", ha='right', extended=True, zorder=5)
    annotate_target(16.2258, +2.1333, "IC1613", ha='left', extended=True, zorder=5)




def annotate_microlensing():
    fov = getKeplerFov(9)
    superstamp_patches = []
    for ch in SUPERSTAMP["channels"]:
        v_col = SUPERSTAMP["channels"][ch]["vertices_col"]
        v_row = SUPERSTAMP["channels"][ch]["vertices_row"]
        radec = np.array([
            fov.getRaDecForChannelColRow(int(ch),
                                         v_col[idx],
                                         v_row[idx])
            for idx in range(len(v_col))
        ])
        patch = pl.fill(radec[:, 0], radec[:, 1],
                        lw=0, facecolor=colors[1], zorder=30)
        superstamp_patches.append(patch)
    text = pl.text(268.6, -27.6, 'Microlensing\nsuperstamp', color=colors[1],
                   zorder=999, fontsize=22, va='center', ha='left')
    text.set_path_effects([path_effects.Stroke(linewidth=4, foreground='white'),
                           path_effects.Normal()])


def _plot(CAMPAIGN=1, planets=True, clusters=True, moving=True, extended=True, microlensing=True, supernovae=False):
    p = plot.K2FootprintPlot(figsize=(11, 11))
    campaigns = np.arange(0, CAMPAIGN+1)

    for c in campaigns[0:-1]:
        p.plot_campaign(c, annotate_channels=False, facecolor=colors[5],
                        lw=1, edgecolor=colors[5], zorder=1, alpha=0.3)
    p.plot_campaign(CAMPAIGN, annotate_channels=False, facecolor='white',
                    lw=1, edgecolor=colors[5], zorder=2)

    p.ax.xaxis.set_major_locator(MultipleLocator(2))
    p.ax.yaxis.set_major_locator(MultipleLocator(2))
    pl.tight_layout()

    if planets:
        annotate_planets(CAMPAIGN)
    if moving:
        annotate_moving(CAMPAIGN)
    if extended:
        annotate_extended(CAMPAIGN)
    if microlensing:
        annotate_microlensing()
    if clusters:
        annotate_clusters(CAMPAIGN)
    if supernovae:
        annotate_supernova(CAMPAIGN)

    pl.xlim(xlims[CAMPAIGN])
    pl.ylim(ylims[CAMPAIGN])

    for extension in EXTENSIONS:
        output_fn = 'output/k2-c{:02}-field-notitle.{}'.format(CAMPAIGN, extension)
        print('Writing {}'.format(output_fn))
        pl.savefig(output_fn, dpi=100)

    pl.suptitle('K2 Campaign {}'.format(CAMPAIGN), fontsize=44)
    for extension in EXTENSIONS:
        output_fn = 'output/k2-c{:02}-field.{}'.format(CAMPAIGN, extension)
        print('Writing {}'.format(output_fn))
        pl.savefig(output_fn, dpi=100)
    pl.close()


def plot_all():
    _plot(0)
    _plot(1)
    _plot(2)
    _plot(3, extended=False)
    _plot(4)
    _plot(5)
    _plot(6)
    _plot(7)
    _plot(8)
    _plot(9)
    _plot(10)
    _plot(11, microlensing=False, clusters=False)
    _plot(12)
    _plot(13)
    _plot(14, planets=False)
    _plot(15)
    _plot(16, planets=False, supernovae=True)
    _plot(17, planets=False, supernovae=True)
    _plot(18)
    _plot(19)


if __name__ == '__main__':
    plot_all()
    