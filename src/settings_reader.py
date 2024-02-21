import yaml

# Api key is stored in yaml file. Since this script is for personal use i dont care about safety that much.
# Even tho it's not safe to store this var like that. Probably.

class SettingsReader():

    def __init__(self) -> None:
        self.settings_dir = "./settings.yaml" # Hardcoded, be careful!
        self.yaml_cache = self.__read_yaml()

    # Make static
    def get_value(self, key: str = None) -> str:
        if not key:
            return None
        
        if key in self.yaml_cache:
            return self.yaml_cache[key]
    
        else:
            return None

    def set_value(self, key: str = "", value: str = "") -> None:
        if (key == "") or (value == ""):
            return

        self.yaml_cache[key] = value
        self.__write_yaml()

    def get_dir(self) -> str:
        return self.settings_dir

    def get_yaml(self):
        return self.yaml_cache

    def __read_yaml(self):
        with open(self.settings_dir, 'r') as file:
            data = yaml.safe_load(file)
            return data

    def __write_yaml(self) -> None:
        with open(self.settings_dir, 'w') as file:
            yaml.dump(self.yaml_cache, file)
