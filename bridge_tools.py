import time
import os

from App.BridgeGrades.main import bridge_grade_main
from App.SeismicData.main import seismic_data_main


def program_welcome():
    print('Bridge Tools')


def main_loop():
    try:
        user_input = ''
        while user_input.lower() != 'q':
            program_welcome()
            print()
            print('1. Calculate Bridge Grades')
            print('2. Retrieve Design Response Spectra')
            print()
            print('Type \'q\' to exit the program')
            user_input = input('>> ')
            handle_user_input(user_input)
    except ValueError as e:
        print('n' + e.args[0])
        time.sleep(1.5)  # keep window open long enough to see error message


def handle_user_input(user_input):
    if user_input == '1':
        bridge_grades()
    elif user_input == '2':
        clear_console()
        seismic_data_main()
        clear_console()
    elif user_input == 'q':
        pass
    else:
        print('\nPlease select a valid option or type \'q\' to exit\n')


def bridge_grades():
    clear_console()
    print('Waiting for user input')
    bridge_grade_main()
    print('Returning to main menu.')
    time.sleep(1.5)
    clear_console()


def clear_console():
    if os.name == 'nt':  # windows
        os.system('cls')
    else:  # mac or linux
        os.system('clear')


if __name__ == '__main__':
    main_loop()