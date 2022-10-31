from typing import Dict

from StructuralShapes.RolledShapes.rolled_shape import AISC_TYPE, AISC_EDI_STD_NOMENCLATURE, AISC_MANUAL_LABEL, AISC_T_F


class CSVRolledShapeGetterAISC15:
    """
    Retrieves AISC Steel Construction Manual, 15th Edition rolled shape data from CSV formatted file
    """

    def __init__(self, file_path: str):
        self.__file_path = file_path

    def get_data(self, shape_name: str) -> Dict:
        """
        Gets the rolled shape data from the CSV formatted file
        :param shape_name: Shape name that matches the EDI_Standard_Nomenclature name from AISC Shapes Database
        :return: Dictionary containing all shape data
        """
        return self.__get_csv_data(shape_name)

    def __get_csv_data(self, shape_name: str) -> Dict:
        csv_separator = ','
        header = []
        data = []

        with open(self.__file_path, 'r') as f:
            for line in f:
                split = line.split(csv_separator)
                if split[0] == AISC_TYPE:  # header row
                    header = split
                else:  # data row
                    if shape_name == split[1]:
                        data = split
                        break

        if not data:
            raise ValueError('The requested shape was not found in the AISC Shapes Database')

        properties = self.__build_properties_dictionary(data, header)

        return properties

    def __build_properties_dictionary(self, data, header) -> Dict:
        properties = {}

        for i in range(len(data)):
            if not data[i].strip() == '':
                # Most values in table should be floats, but there are a few that should be strings
                if header[i] == AISC_TYPE or \
                        header[i] == AISC_EDI_STD_NOMENCLATURE or \
                        header[i] == AISC_MANUAL_LABEL or \
                        header[i] == AISC_T_F:
                    properties[header[i]] = str(data[i])
                else:
                    properties[header[i]] = float(data[i])

        return properties
