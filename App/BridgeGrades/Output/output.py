import os

from App.BridgeGrades.Output.grade_reporter import GradeReporter


def save_to_file(grade_reporter: GradeReporter):
    """
    Saves report grade reporter text to a file
    :param grade_reporter: Grade reporter that creates output text
    """
    text = grade_reporter.create_report_string()
    file_name = grade_reporter.project_info.project_number + '-Grade Report.txt'
    __write_to_file(file_name, text)


def __write_to_file(filename, content):
    file_path = os.path.join(os.getcwd(), filename)
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)
