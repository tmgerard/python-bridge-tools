import os

from StructuralShapes.RolledShapes.rolled_shape import *
from StructuralShapes.RolledShapes.i_shape import IShape
from StructuralShapes.RolledShapes.csv_rolled_shape_getter import CSVRolledShapeGetterAISC15
from Config.config_reader import read_config


CONFIG_FILE = '../../Config/rolled_shape_config.json'


def create_rolled_shape(shape_name: str):
    """
    Creates a rolled shape object based on data from the AISC Rolled Shapes Database
    """
    file_name = read_config(CONFIG_FILE)['RolledShapes']['CSV_File_Path']
    file_path = os.path.join(os.path.dirname(__file__), file_name)
    getter = CSVRolledShapeGetterAISC15(file_path)

    return __create_shape_object(shape_name, getter)


def __create_shape_object(shape_name: str, getter: CSVRolledShapeGetterAISC15):
    data = getter.get_data(shape_name)
    type = data[AISC_TYPE]

    if type == 'W' or type == 'M' or type == 'S' or type == 'HP':  # I-Shape Section
        return IShape(data)
    else:
        return RolledShape(data)
