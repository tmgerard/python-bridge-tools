import json
import string
import pkg_resources


def read_config(config_file: string):
    """
    Read JSON config file
    :param config_file: JSON formatted config file
    :return: Config dictionary
    """
    config = pkg_resources.resource_string(__name__, config_file)
    return json.loads(config)
