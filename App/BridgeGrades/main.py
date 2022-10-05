import os
import sys
import tkinter as tk
from tkinter import filedialog

parent_path = os.path.normpath(os.path.join(os.getcwd(), '..', '..'))
sys.path.append(parent_path)

from Input.input_parse import BridgeGradesInputParser
from Output.grade_reporter import GradeReporter
from Output.output import save_to_file

if __name__ == '__main__':
    try:
        root = tk.Tk()
        root.withdraw()

        file_path = filedialog.askopenfilename()

        with open(file_path, encoding='utf-8') as f:
            lines = f.readlines()

        parser = BridgeGradesInputParser()
        parser.parse_lines(lines)

        reporter = GradeReporter(parser.project_information, parser.alignment, parser.key_stations)

        save_to_file(reporter)

    except ValueError as e:
        print(e)
