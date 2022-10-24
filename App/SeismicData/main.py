import string
from datetime import date

from Seismic.ResponseSpectra.ground_motion_data_aashto2009 import GroundMotionDataAASHTO2009
from Seismic.ResponseSpectra.ground_motion_data_getter_aashto2009 import GroundMotionDataGetterAASHTO2009
from Seismic.ResponseSpectra.design_response_spectrum_plotter_aashto2009 import DesignSpectrumPlotterAASHTO2009
from Seismic.config_reader import read_config


CONFIG_FILE = 'seismic_config.json'


def get_seismic_query_data():
    lat = input('Latitude: ')
    long = input('Longitude: ')
    site_class = input('Site Class: ')
    request_title = input('Title: ')

    query = GroundMotionDataGetterAASHTO2009(read_config(CONFIG_FILE))
    return GroundMotionDataAASHTO2009(query.get_ground_motion_data(lat, long, site_class, request_title))


def seismic_data_main():
    try:
        data = get_seismic_query_data()

        user_input = ''
        while user_input.lower() != 'q':
            print()
            print('Select an action:')
            print('\t1. Display seismic data')
            print('\t2. Plot design spectral acceleration curve')
            print('\nType \'q\' to exit\n')
            user_input = input('>> ')
            handle_user_input(user_input, data)
    except ValueError as e:
        print(e.args[1])


def handle_user_input(user_input: string, data: GroundMotionDataAASHTO2009):
    if user_input == '1':
        seismic_data_console_report(data)
    elif user_input == '2':
        plotter = DesignSpectrumPlotterAASHTO2009(data)
        plotter.plot()
    elif user_input == 'q':
        pass
    else:
        print('\nPlease select a valid option or type \'q\' to exit')


def seismic_data_console_report(data: GroundMotionDataAASHTO2009):
    print('\nSeismic data retrieved from USGS:')
    print('Query URL: {0}'.format(data.url_request))
    print('PGA: {0}'.format(data.peak_ground_acceleration))
    print('SD1: {0}'.format(data.design_one_second_spectral_acceleration))
    print('Seismic Design Category {0}'.format(data.seismic_design_category.upper()))
