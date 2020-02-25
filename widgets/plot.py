from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
from matplotlib.animation import FuncAnimation
from PyQt5.QtWidgets import QSizePolicy, QWidget, QHBoxLayout, QVBoxLayout, QPushButton
import seaborn as sns

sns.set_style("darkgrid")

class Plotting(FigureCanvas):
    
    def __init__(self, parent=None):
        self.x, self.y = 0, 0
        self.fig = Figure()
        self.fig.patch.set_visible(False)
        
        self.ax = self.fig.add_subplot(111)
        self.ax.spines["right"].set_visible(False)
        self.ax.spines["top"].set_visible(False)
        self.ax.spines["left"].set_visible(False)
        self.ax.spines["bottom"].set_visible(False)
        
        self.ax.grid(color='white', linestyle='-', linewidth=0.1, axis='x', alpha=0.2)
        self.ax.grid(color='white', linestyle='-', linewidth=0.1, axis='y', alpha=0.2)
        self.ax.tick_params(axis='x', color = 'white')
        self.ax.patch.set_visible(False)
        
        

        FigureCanvas.__init__(self, self.fig)
        self.setParent(parent)
        FigureCanvas.setSizePolicy(self, QSizePolicy.Expanding,
                                         QSizePolicy.Expanding
                                         )

    def plot(self, x, y, title=""):
        self.ax.set_title(title)
        self.ax.plot(x, y, alpha = 0.1)
        self.ax.fill_between(x, y, alpha=0.1)
        self.draw()

    def plot_scatt(self,x ,y, title=""):
        self.ax.set_title(title)
        self.ax.scatter(x, y)
        self.draw()






