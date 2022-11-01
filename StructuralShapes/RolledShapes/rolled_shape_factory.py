import os

from StructuralShapes.RolledShapes.rolled_shape import *
from StructuralShapes.RolledShapes.i_shape import IShape
from StructuralShapes.RolledShapes.channel_shape import ChannelShape
from StructuralShapes.RolledShapes.single_angle import LShape
from StructuralShapes.RolledShapes.t_shape import TShape
from StructuralShapes.RolledShapes.csv_rolled_shape_getter import CSVRolledShapeGetterAISC15
from Config.config_reader import read_config


CONFIG_FILE = 'rolled_shape_config.json'


def create_rolled_shape(shape_name: str):
    """
    Creates a rolled shape object based on data from the AISC Rolled Shapes Database
    """
    file_name = read_config(CONFIG_FILE)['RolledShapes']['CSV_File_Name']
    file_path = os.path.join(os.path.dirname(__file__), file_name)
    getter = CSVRolledShapeGetterAISC15(file_path)

    return __create_shape_object(shape_name, getter)


def __create_shape_object(shape_name: str, getter: CSVRolledShapeGetterAISC15):
    data = getter.get_data(shape_name)
    shape_type = data[AISC_TYPE]

    if shape_type == 'W' or shape_type == 'M' or shape_type == 'S' or shape_type == 'HP':  # I-Shape Section
        return IShape(data)
    elif shape_type == 'C' or shape_type == 'MC':  # Channel Shape
        return ChannelShape(data)
    elif shape_type == 'L':  # Single angle shape
        return LShape(data)
    elif shape_type == 'WT' or shape_type == 'MT' or shape_type == 'ST':  # T-Shape Section
        return TShape(data)
    else:
        return RolledShape(data)
