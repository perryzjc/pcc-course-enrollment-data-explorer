import plotly.graph_objs as go
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
from typing import List, Tuple
from datetime import datetime

matplotlib.use('webagg')


class Visualizer:
    """Class for visualizing the data.
    """

    def __init__(self, data_frame_processor):
        """Initialize the class, set the data frame processor.
        """
        self.df_processor = data_frame_processor

    def get_plotly_fig_json(self, crn_lst: List[int] = None,
                            start_time: datetime = None,
                            end_time: datetime = None) -> str:
        """Return a plotly figure in JSON format. Useful for advanced website plotting.
        """
        # use get_matplotlib_plot to get the figure and axes
        fig, ax = self.get_matplotlib_plot(crn_lst, start_time, end_time)
        # convert the figure to JSON
        fig = Visualizer.matplotlib_fig_to_plotly_fig(ax)
        return fig.to_json()

    def get_matplotlib_plot(self, crn_lst: List[int] = None,
                            start_time: datetime = None,
                            end_time: datetime = None) -> Tuple[plt.Figure, plt.Axes]:
        """Return a matplotlib figure.

        If crn_lst is not given, return an empty figure.
        """
        if crn_lst is None:
            crn_lst = []
        df = self.df_processor.get_data_frame(crn_lst, start_time, end_time)
        crn_lst_valid = self.df_processor.crn_lst_valid(crn_lst)
        colors = Visualizer._get_color_lst(crn_lst)
        groups = df.groupby('CRN')
        # Create a list of Scatter objects, one for each group
        fig, ax = plt.subplots(figsize=(10, 6))
        labels = []
        for i, (name, group) in enumerate(groups):
            name = str(name)
            ax.plot(group['Time'], group['Rem'], color=colors[i], label=name)
            labels.append(name)
        ax.legend(title='CRN', labels=labels)
        ax.set_title('Course Enrollment Trend')
        ax.set_xlabel('Time')
        ax.set_ylabel('Remaining Seats')
        return fig, ax

    @staticmethod
    def matplotlib_fig_to_plotly_fig(ax):
        fig = go.Figure()
        for i, data in enumerate(ax.lines):
            fig.add_trace(go.Scatter(x=data.get_xdata(), y=data.get_ydata(), name=data.get_label(), mode='lines'))
        # update layout based on the setting of the matplotlib figure
        fig.update_layout(
            title=ax.get_title(),
            xaxis_title=ax.get_xlabel(),
            yaxis_title=ax.get_ylabel(),
            legend_title=ax.get_legend().get_title().get_text(),
            showlegend=True
        )
        return fig

    @staticmethod
    def _get_color_lst(crn_lst: List[int] = None) -> List[str]:
        """Return a list of colors based on the number of CRN.
        """
        # Generate a colormap with the number of colors equal to the number of groups
        cmap = plt.get_cmap('viridis')
        colors = [cmap(i) for i in np.linspace(0, 1, len(crn_lst))]
        return colors
