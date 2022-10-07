import string
import urllib.request
import json


class GroundMotionDataGetterAASHTO2009:
    """
    Retrieves USGS seismic ground motion data from USGS website
    """

    __valid_site_classes = ['A', 'B', 'C', 'D', 'E']

    def __init__(self, config):
        self.__web_query_url = config['USGSWebQuery']['AASHTO-2009']

    def get_ground_motion_data(self, latitude: float, longitude: float, site_class: string, title=""):
        """
        Queries USGS data for design response spectrum values.
        :param latitude: project latitude
        :param longitude: project longitude
        :param site_class: soil site class based on subsurface investigation
        :param title: optional project title
        :return: json string with seismic data
        """
        self.__check_site_class(site_class.upper())

        request_url = self.__web_query_url.format(latitude, longitude, site_class.upper(), title)
        with urllib.request.urlopen(request_url) as url:
            data = json.loads(url.read().decode())

        return data

    def __check_site_class(self, site_class: string):
        """
        The AASHTO 2009 Guide Specifications specify site classes A, B, C, D, and E
        :param site_class:
        """
        if not site_class.upper() in self.__valid_site_classes:
            raise ValueError('Site class undefined by AASHTO 2009 Guide Specifications')
