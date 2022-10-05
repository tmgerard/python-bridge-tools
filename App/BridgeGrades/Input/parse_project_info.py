import re

from .project_information import ProjectInfo


__PROJECT_INFO_REGEX = r'(?P<project_number>\w*)\s*(?P<description>.*\s*)'

def parse_project_info(info: str) -> ProjectInfo:
    match = re.match(__PROJECT_INFO_REGEX, info)
    if not match:
        raise ValueError(f'Cannot parse project information')

    return ProjectInfo(
        match.group("project_number"),
        match.group("description")
    )
