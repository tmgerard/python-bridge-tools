class GroundMotionDataAASHTO2009:
    """
    Stores seismic data retrieved from USGS website
    """
    def __init__(self, seismic_data):
        if seismic_data['request']['status'] == "error":
            raise ValueError('Seismic request invalid')

        self.__data = seismic_data['response']['data']
        self.__input_parameters = seismic_data['request']['parameters']
        self.__url_request = seismic_data['request']['url']

    @property
    def latitude(self):
        """
        The latitude input for the seismic data
        """
        return self.__input_parameters['latitude']

    @property
    def longitude(self):
        """
        The longitude input for the seismic data
        """
        return self.__input_parameters['longitude']

    @property
    def site_class(self):
        """
        The site class input for the seismic data based on the site subsurface investigation.
        :return:
        """
        return self.__input_parameters['siteClass']

    @property
    def url_request(self):
        """
        The url sent to obtain seismic data
        """
        return self.__url_request

    @property
    def title(self):
        """
        The project title input for the seismic data
        """
        return self.__input_parameters['title']

    @property
    def peak_ground_acceleration(self):
        """
        The mapped horizontal peak ground acceleration (PGA) in units of g
        """
        return self.__data['pga']

    @property
    def pga_site_coefficient(self):
        """
        Site coefficient (Fpga) for pga from Table 3.4.2.3-1 of the AASHTO Seismic Guide Specifications
        """
        return self.__data['fpga']

    @property
    def design_peak_ground_acceleration(self):
        """
        The design peak ground acceleration (As = Fpga * Pga)
        """
        return self.__data['as']

    @property
    def short_period_spectral_acceleration(self):
        """
        The mapped short-period (0.2 second) spectral acceleration (Ss) in units of g
        """
        return self.__data['ss']

    @property
    def ss_site_coefficient(self):
        """
        The site coefficient (Fa) for the Ss from Table 3.4.2.3-1 of the AASHTO Seismic Guide Specifications
        """
        return self.__data['fa']

    @property
    def design_short_period_spectral_acceleration(self):
        """
        The design short period spectral acceleration (Sds = Fa * Ss)
        """
        return self.__data['sds']

    @property
    def one_second_spectral_acceleration(self):
        """
        The mapped one-second spectral acceleration (S1)
        """
        return self.__data['s1']

    @property
    def s1_site_coefficient(self):
        """
        The site coefficient (fv) for S1 from Table 3.4.2.3-1 of the AASHTO Seismic Guide Specifications
        :return:
        """
        return self.__data['fv']

    @property
    def design_one_second_spectral_acceleration(self):
        """
        The design once second spectral acceleration (Sd1)
        """
        return self.__data['sd1']

    @property
    def seismic_design_category(self):
        """
        The seismic design category from Table 3.5-1 of the AASHTO Seismic Guide Specifications
        """
        return self.__data['sdc']

    @property
    def ts(self):
        """
        The ratio of Sd1 over Sds (equation 3.4.1-6) required for construction of the design response spectrum
        """
        return self.__data['ts']

    @property
    def t0(self):
        """
        The Ts value times 0.2 (equation 3.4.1-5) used for construction of the design response spectrum
        """
        return self.__data['t0']

    @property
    def two_period_design_spectrum(self):
        """
        The two-period design response spectrum
        """
        return self.__data['twoPeriodDesignSpectrum']
