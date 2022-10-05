import unittest

from App.BridgeGrades.Input.project_information import ProjectInfo
from App.BridgeGrades.Input.parse_project_info import parse_project_info


class TestParseProjectInfo(unittest.TestCase):
    info_str = '020475 Bridge Grade for Highway 83 over UPRR'

    def test_parse_project_info(self):
        expected = ProjectInfo('020475', 'Bridge Grade for Highway 83 over UPRR')
        actual = parse_project_info(self.info_str)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
