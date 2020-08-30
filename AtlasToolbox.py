import numpy as np


class AtlasToolbox:
    """
    Contains useful tools for Atlas later
    """

    def get_start_stop_indices(self, time_array, plot_start, plot_stop):
        start_index = (np.fabs(time_array - plot_start)).argmin()  # index in t_pts array
        stop_index = (np.fabs(time_array - plot_stop)).argmin()  # index in t_pts array
        return start_index, stop_index
