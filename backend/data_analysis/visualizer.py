"""Return visualizations of the data.
"""
import pandas as pd
import numpy as np
import plotly.graph_objs as go
import matplotlib.pyplot as plt
import matplotlib
from datetime import datetime
from typing import List, Tuple
from backend.log import write_to_log_file

matplotlib.use('webagg')


class Visualizer:
    """Class for visualizing the data.
    """

    def __init__(self, csv_path):
        """Initialize the class, generate adn clean the data frame.
        """
        self.df = pd.read_csv(csv_path)
        df = self.df
        # convert Time column to datetime data type
        df['Time'] = pd.to_datetime(df['Time'], format='%Y-%m-%d-%H-%M-%S')
        # delete row if Rem is not a valid integer or CRN is not a valid integer
        df = df[df['Rem'].apply(lambda x: x.isdigit())]
        df = df[df['CRN'].apply(lambda x: x.isdigit())]
        # transform to int
        df['Rem'] = df['Rem'].astype(int)
        df['CRN'] = df['CRN'].astype(int)
        # sort by time
        self.df = df.sort_values(by=['Time'])

    def get_plotly_fig_json(self, crn_lst: List[int] = None,
                            start_time: datetime = None,
                            end_time: datetime = None) -> str:
        """Return a plotly figure in JSON format. Useful for advanced website plotting.
        """
        src_matplotlib_fig, src_matplotlib_ax = self.get_matplotlib_plot(crn_lst, start_time, end_time)
        fig = Visualizer.matplotlib_fig_to_plotly_fig(src_matplotlib_ax)
        return fig.to_json()

    def get_matplotlib_plot(self, crn_lst: List[int] = None,
                            start_time: datetime = None,
                            end_time: datetime = None) -> Tuple[plt.Figure, plt.Axes]:
        """Return a matplotlib figure.

        If crn_lst is not given, return an empty figure.
        # """
        if crn_lst is None:
            crn_lst = []
        df = self._get_data_frame(crn_lst, start_time, end_time)
        colors = Visualizer._get_color_lst(crn_lst)
        groups = df.groupby('CRN')
        # Create a list of Scatter objects, one for each group
        fig, ax = plt.subplots(figsize=(10, 6))
        for i, (name, group) in enumerate(groups):
            ax.plot(group['Time'], group['Rem'], color=colors[i], label=name)
        ax.legend()
        ax.set_title('Course Enrollment Trend')
        ax.set_xlabel('Time')
        ax.set_ylabel('Remaining Seats')
        return fig, ax

    def _get_data_frame(self, crn_lst: List[int] = None,
                        start_time: datetime = None,
                        end_time: datetime = None) -> pd.DataFrame:
        """Read the data based on the given CRN list, start time and end time
        """
        df = self.df.copy()
        if crn_lst is not None:
            df = df[df['CRN'].isin(crn_lst)]
        if start_time:
            df = df[df['Time'] >= start_time]
        if end_time:
            df = df[df['Time'] <= end_time]
        return df

    @staticmethod
    def _get_color_lst(crn_lst: List[int] = None) -> List[str]:
        """Return a list of colors based on the number of CRN.
        """
        # Generate a colormap with the number of colors equal to the number of groups
        cmap = plt.get_cmap('viridis')
        colors = [cmap(i) for i in np.linspace(0, 1, len(crn_lst))]
        return colors

    @staticmethod
    def matplotlib_fig_to_plotly_fig(ax):
        fig = go.Figure()
        for i, data in enumerate(ax.lines):
            fig.add_trace(go.Scatter(x=data.get_xdata(), y=data.get_ydata(), name=f"Line {i + 1}"))
        # update layout based on the setting of the matplotlib figure
        fig.update_layout(
            title=ax.get_title(),
            xaxis_title=ax.get_xlabel(),
            yaxis_title=ax.get_ylabel(),
            legend_title=ax.get_legend().get_title().get_text())
        return fig

    @staticmethod
    def crn_lst_valid(crn_lst: List[int]) -> bool:
        """Return True if the given CRN list is valid, False otherwise.

        crn_lst is valid if
            - it is empty
            - it contains only integers
            - no repeated CRN

        If any error, write to log and print it console
        """
        if crn_lst is None:
            return True
        if not all(isinstance(crn, int) for crn in crn_lst):
            print('CRN list contains non-integer values')
            return False
        if len(crn_lst) != len(set(crn_lst)):
            print('CRN list contains repeated CRN')
            return False
        return True

