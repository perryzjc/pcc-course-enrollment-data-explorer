import pandas as pd
from datetime import datetime
from typing import List


class DataFrameProcessor:
    """Class for processing data frames.
    """

    def __init__(self, csv_path):
        """Initialize the class, generate and clean the data frame.
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

    def get_data_frame(self, crn_lst: List[int] = None,
                       start_time: datetime = None,
                       end_time: datetime = None) -> pd.DataFrame:
        """Return a subset of the data frame based on the given parameters.
        """
        df = self.df.copy()
        if crn_lst is not None:
            df = df[df['CRN'].isin(crn_lst)]
        if start_time:
            df = df[df['Time'] >= start_time]
        if end_time:
            df = df[df['Time'] <= end_time]
        return df

    def get_all_crn(self) -> List[int]:
        """Return a list of all CRNs in the data frame.
        """
        return self.df['CRN'].unique().tolist()
