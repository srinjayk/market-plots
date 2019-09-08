import matplotlib.pyplot as plt
import matplotlib.style as style


def apply_common_styles():
    plt.figure(figsize=(38.4 / 2, 21.6 / 2))

    plt.rcParams['font.size'] = 20
    plt.rcParams['text.color'] = '#ffffff'

    plt.rcParams['axes.titlepad'] = 24
    plt.rcParams['axes.facecolor'] = '#222222'
    plt.rcParams['savefig.facecolor'] = '#222222'

    plt.rcParams['xtick.color'] = '#ffffff'
    plt.rcParams['xtick.major.pad'] = 13
    plt.rcParams['xtick.minor.pad'] = 13

    plt.rcParams['ytick.color'] = '#ffffff'
    plt.rcParams['ytick.major.pad'] = 13
    plt.rcParams['ytick.minor.pad'] = 13

    plt.rcParams['lines.linewidth'] = 3

    ax = plt.gca()
    ax.set_facecolor('#ffffff')


def line():
    style.use('bmh')
    apply_common_styles()


def hist():
    style.use('default')
    apply_common_styles()