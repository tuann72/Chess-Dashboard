import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from settings import *


class BarFigure:
    def __init__(self, root, title, data):
        # settings up data
        self.bar_fig, self.ax = plt.subplots()
        self.root = root
        self.title = title

        # configuring
        self.ax.bar(GRAPH_X_AXIS, data, color=COLORS)
        self.ax.set_title(self.title, color="#FFFFFF")
        self.ax.set_xlabel(X_AXIS_LABEL, color="#FFFFFF")
        self.ax.set_ylabel(Y_AXIS_LABEL, color="#FFFFFF")
        self.ax.tick_params(axis="x", colors="#FFFFFF")
        self.ax.tick_params(axis="y", colors="#FFFFFF")
        self.ax.set_facecolor("#4D4D4D")
        self.bar_fig.set_facecolor("#4D4D4D")

        # placing
        self.bar_canvas = FigureCanvasTkAgg(self.bar_fig, self.root)
        self.bar_canvas.get_tk_widget().place(relx=0.5, rely=0.5, anchor="center")


class PIFigure:
    def __init__(self, root, data):
        # setting up data
        self.pi_fig, self.pi_ax = plt.subplots(figsize=(6, 4))
        self.pi_ax.pie(
            data, labels=PI_LABELS, colors=COLORS, autopct="%1.1f%%", startangle=90
        )
        self.root = root
        self.pi_ax.set_facecolor("#4D4D4D")

        # placing
        self.pi_canvas = FigureCanvasTkAgg(self.pi_fig, self.root)
        self.pi_canvas.get_tk_widget().place(relx=0.5, rely=0.35, anchor="center")
