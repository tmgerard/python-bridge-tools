import os

from Config.config_reader import read_config
from StructuralShapes.RolledShapes.csv_rolled_shape_getter import CSVRolledShapeGetterAISC15
from StructuralShapes.RolledShapes.rolled_shape import RolledShape


CONFIG_FILE = 'rolled_shape_config.json'


def get_rolled_shape():
    try:
        shape = input('Shape Name: ').upper()
        rel_path = read_config(CONFIG_FILE)['RolledShapes']['CSV_File_Path']
        file_path = os.path.join(os.path.dirname(__file__), '..\\..\\', rel_path)
        getter = CSVRolledShapeGetterAISC15(file_path)
        rolled_shape = RolledShape(getter.get_data(shape))
        print('name: {0}  area: {1} sq. in.'.format(rolled_shape.edi_std_nomenclature, rolled_shape.area))
    except ValueError as e:
        print(e.args[1])
