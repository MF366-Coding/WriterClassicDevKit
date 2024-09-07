NONE = NO_PERMS = 0
READ = 1
READ_WRITE = 2
YES = True
NO = False

class Permissions:
    def __init__(self):
        self._perms = {
            "editor": 0,
            "listeners": 0,
            "settings": 0,
            "callhistory": 0,
            "forcequit": False,
            "requestdata": 0
        }

    def apply_by_dict(self, perms_dict: dict[str, int | bool]):
        self._perms = perms_dict

    @property
    def editor_perms(self) -> int:
        return self._perms["editor"]

    @editor_perms.setter
    def editor_perms(self, value: int):
        if isinstance(value, bool):
            value = int(value)

        self._perms["editor"] = value

    @property
    def listener_perms(self) -> int:
        return self._perms["listeners"]

    @listener_perms.setter
    def listener_perms(self, value: int):
        if isinstance(value, bool):
            value = int(value)

        self._perms["listeners"] = value

    @property
    def settings_perms(self) -> int:
        return self._perms["settings"]

    @settings_perms.setter
    def settings_perms(self, value: int):
        if isinstance(value, bool):
            value = int(value)

        self._perms["settings"] = value

    @property
    def callhistory_perms(self) -> int:
        return self._perms["callhistory"]

    @callhistory_perms.setter
    def callhistory_perms(self, value: int):
        if isinstance(value, bool):
            value = int(value)

        self._perms["callhistory"] = value

    @property
    def requestdata_perms(self) -> int:
        return self._perms["requestdata"]

    @requestdata_perms.setter
    def requestdata_perms(self, value: int):
        if isinstance(value, bool):
            value = int(value)

        self._perms["requestdata"] = value

    @property
    def forcequit_perms(self) -> bool:
        return self._perms["forcequit"]

    @forcequit_perms.setter
    def forcequit_perms(self, value: bool):
        self._perms["forcequit"] = value

class Project:
    def __init__(self, name: str, description: str, permissions: Permissions | dict[str, int | bool], icon: str | None = None, proj_id: int | None = None):
        self._name = name
        self._description = description

        if isinstance(permissions, dict):
            self._permissions = Permissions()
            self._permissions.apply_by_dict(permissions)

        else:
            self._permissions = permissions

        self._icon = icon
        self.__project_id = proj_id


