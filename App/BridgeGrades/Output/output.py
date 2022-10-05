import os

from App.BridgeGrades.Output.grade_reporter import GradeReporter
import tkinter as tk
from tkinter import filedialog


def save_to_file(grade_reporter: GradeReporter):
    """
    Saves report grade reporter text to a file
    :param grade_reporter: Grade reporter that creates output text
    """

    file = filedialog.asksaveasfile(mode='w', defaultextension='.txt',
                                    initialfile=grade_reporter.project_info.project_number
                                                + '-Grade-Report')
    if file is None:    # dialog closed with "cancel"
        return

    file.write(grade_reporter.create_report_string())
    file.close()
