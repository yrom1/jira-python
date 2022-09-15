import datetime as dt

import matplotlib
import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd
import requests
from matplotlib import font_manager
from mypandas import MyPandas

from main import COUNTS, DAYS

FONTSIZE = requests.get(
    "https://raw.githubusercontent.com/yrom1/yrom1/main/FONTSIZE"
).text
# FONT_FILENAME = "SFMono-Regular.ttf"
# FONT = FONT_FILENAME[:-4]
# FONTSIZE = 9
# BLUE = "#0969da"
# BLACK = "#444444"
DATE_FORMAT = r"%Y-%m-%d"
DPI = 300
GRID_ALPHA = 0.05
ASPECT_RATIO = 0.20
# FONT_ENTRY = font_manager.FontEntry(fname="SFMono-Regular.otf", name="SFMono-Regular")
# font_manager.fontManager.ttflist.insert(0, FONT_ENTRY)
# matplotlib.rcParams["font.family"] = FONT_ENTRY.name


# def fixed_aspect_ratio(ratio):
#     # https://stackoverflow.com/a/37340384/13660563
#     """
#     Set a fixed aspect ratio on matplotlib plots
#     regardless of axis units
#     """
#     xvals, yvals = plt.gca().axes.get_xlim(), plt.gca().axes.get_ylim()
#     xrange = xvals[1] - xvals[0]
#     yrange = yvals[1] - yvals[0]
#     plt.gca().set_aspect(ratio * (xrange / yrange), adjustable="box")


def format_dates(dates: list[str]):
    return [dt.datetime.strptime(date, DATE_FORMAT) for date in dates]


def save_plot(x, y):
    # https://olgabotvinnik.com/blog/prettyplotlib-painlessly-create-beautiful-matplotlib/
    # plt.style.use("grayscale")
    # mpl.rcParams["font.family"] = FONT
    # spines_to_remove = ["top", "right"]
    matplotlib.rc("font", **{"size": FONTSIZE})
    from matplotlib.figure import figaspect

    w, h = figaspect(ASPECT_RATIO)
    fig, ax = plt.subplots(1, figsize=(w, h))

    # for spine in spines_to_remove:
    # ax.spines[spine].set_visible(False)
    # ax.xaxis.set_ticks_position("none")
    # ax.yaxis.set_ticks_position("none")
    # spines_to_keep = ["bottom", "left"]
    # for spine in spines_to_keep:
    # ax.spines[spine].set_linewidth(0.5)
    # ax.spines[spine].set_color(BLACK)
    # ax.xaxis.label.set_color(BLACK)
    # ax.tick_params(axis="x", colors=BLACK)
    # plt.xticks(fontsize=FONTSIZE)
    # ax.yaxis.label.set_color(BLACK)
    # ax.tick_params(axis="y", colors=BLACK)
    # plt.yticks(fontsize=FONTSIZE)
    ax.bar(x, y, color="blue")
    # plt.gcf().autofmt_xdate()
    # fixed_aspect_ratio(ASPECT_RATIO)
    # plt.grid(True, color=BLACK, alpha=GRID_ALPHA)

    ax.xaxis.set_major_formatter(
        mpl.dates.ConciseDateFormatter(ax.xaxis.get_major_locator())
    )

    plt.ylabel(
        "# Completed Issues"
        # , fontsize=FONTSIZE
    )
    with open("ISSUES_DONE_TODAY", "r") as f:
        ISSUES_DONE_TODAY = int(f.read())

    JIRA_TITLE = f"{ISSUES_DONE_TODAY} {'Issue' if ISSUES_DONE_TODAY == 1 else 'Issues'} Completed Today in LIFE Jira Project"
    with open("JIRA_TITLE", "w") as f:
        f.write(JIRA_TITLE)
    plt.title(
        JIRA_TITLE,
        # color=BLACK,
        # fontsize=FONTSIZE,
    )
    plt.savefig("Jira_hustle_graph.png", bbox_inches="tight", dpi=DPI, transparent=True)


if __name__ == "__main__":
    from main import COUNTS, DAYS

    df = pd.DataFrame({"date": DAYS, "value": COUNTS})
    df.to_json("plot.json")
    # save_plot(format_dates(DAYS), COUNTS)
    query = """
    SELECT SUM(value)
    FROM df
    WHERE month(date) = month(now());
    """
    with open("ISSUES_DONE_THIS_MONTH", "w") as f:
        f.write(
            str(int(MyPandas("mysql://root:root@localhost")(query, locals()).values[0]))
        )
