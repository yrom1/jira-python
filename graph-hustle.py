import matplotlib
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib import font_manager

from main import COUNTS, DAYS

FONT_FILENAME = "SFMono-Regular.ttf"
FONT = FONT_FILENAME[:-4]
FONTSIZE = 6
BLUE = "#0969da"
BLACK = "#768390"
DATE_FORMAT = r"%Y-%m-%d"
DPI = 300
GRID_ALPHA = 0.05
ASPECT_RATIO = 0.15


def fixed_aspect_ratio(ratio):
    # https://stackoverflow.com/a/37340384/13660563
    """
    Set a fixed aspect ratio on matplotlib plots
    regardless of axis units
    """
    xvals, yvals = plt.gca().axes.get_xlim(), plt.gca().axes.get_ylim()
    xrange = xvals[1] - xvals[0]
    yrange = yvals[1] - yvals[0]
    plt.gca().set_aspect(ratio * (xrange / yrange), adjustable="box")


def save_plot(x, y):
    plt.style.use("./deeplearning.mplstyle")
    fig, ax = plt.subplots(1)
    ax.bar(x, y)
    plt.gcf().autofmt_xdate()
    fixed_aspect_ratio(ASPECT_RATIO)
    plt.ylabel("# Done Issues")
    plt.title("LYFE Jira Project")
    plt.savefig("Jira_hustle_graph.png", bbox_inches="tight", dpi=DPI, transparent=True)


if __name__ == "__main__":
    save_plot(DAYS, COUNTS)
