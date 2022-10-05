class ProjectInfo:
    """
    Store for project information
    """
    def __init__(self, project_number: str, description: str):
        self.project_number = project_number
        self.description = description

    def __eq__(self, other: 'ProjectInfo') -> bool:
        return self.project_number == other.project_number and self.description == other.description
