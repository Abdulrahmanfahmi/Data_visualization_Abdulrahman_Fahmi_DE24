from matplotlib.ticker import FuncFormatter


def horizontal_bar_options(ax, title=None, title_pad=None, xlabel=None, ylabel=None):
    if title:
        ax.set_title(title, pad=title_pad)
    if xlabel:
        ax.set_xlabel(xlabel)
    if ylabel:
        ax.set_ylabel(ylabel)
    ax.grid(axis='x', linestyle='--', alpha=0.7)
    return ax

# Definiera thousands_formatter funktionen
def thousands_formatter(ax):
    def format_func(value, tick_number):
        return f"{int(value/1000)}K"
    ax.xaxis.set_major_formatter(FuncFormatter(format_func))
    return ax


def save_fig_from_ax(ax, **options):
    fig = ax.get_figure()
    fig.tight_layout()   
    fig.savefig(options.get("save_path", ""), dpi=options.get("dpi", 300))
    

def thousands_formatter(ax, axis="x"):
    formatter = FuncFormatter(
        lambda val, pos: f"{int(val/1000)}K" if val else f"{val:.0f}"
    )
    if axis == "x":
        ax.xaxis.set_major_formatter(formatter)
    elif axis == "y":
        ax.yaxis.set_major_formatter(formatter)
    elif axis == "both":
        ax.xaxis.set_major_formatter(formatter)
        ax.yaxis.set_major_formatter(formatter)
    return ax

