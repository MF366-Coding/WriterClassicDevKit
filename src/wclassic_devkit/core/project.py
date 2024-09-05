class Project:
    def __init__(self, name: str, description: str, permissions, icon: str | None = None, **_, proj_id: int | None = None):
        self._name = name
        self._description = description
        self._permissions = permissions
        self._icon = icon
        self.__project_id = proj_id


