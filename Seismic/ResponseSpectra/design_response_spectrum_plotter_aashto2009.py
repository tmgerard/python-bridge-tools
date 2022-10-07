from matplotlib.pyplot import plot, show, title, xlabel, ylabel, annotate, scatter

from Seismic.ResponseSpectra.ground_motion_data_aashto2009 import GroundMotionDataAASHTO2009


class DesignSpectrumPlotterAASHTO2009:

    def __init(self, seismic_data: GroundMotionDataAASHTO2009):
        self.__data = seismic_data

    def plot(self):
        """
        Plots design response spectrum from points array in USGS web query output
        """
        period = [i[0] for i in self.__data.two_period_design_spectrum]
        acceleration = [i[1] for i in self.__data.two_period_design_spectrum]
        plot(period, acceleration)
        title('Response Spectrum - {0}'.format(self.__data.title.replace("_", " ")))
        xlabel('Period')
        ylabel('Acceleration')

        # label pga and sd1
        scatter([0.0, 1.0], [self.__data.design_peak_ground_acceleration,
                             self.__data.design_one_second_spectral_acceleration])
        annotate('As = {0}'.format(self.__data.design_peak_ground_acceleration),
                 (0.0, self.__data.design_peak_ground_acceleration),
                 textcoords="offset points", xytext=(5, -5), ha='left')
        annotate('sd1 = {0}'.format(self.__data.design_one_second_spectral_acceleration),
                 (1.0, self.__data.design_one_second_spectral_acceleration),
                 textcoords="offset points", xytext=(5, 5), ha='left')
        show()
