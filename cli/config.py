import json
import os

class Config:
    def __init__(self):
        self.level = self._load_level()

    def _load_level(self):
        # Construct the absolute path to the config file
        current_dir = os.path.dirname(os.path.abspath(__file__))
        config_path = os.path.join(current_dir, '..', 'templates', 'default_chat.cfg')
        
        try:
            with open(config_path, 'r') as f:
                config_data = json.load(f)
                return config_data.get('level', 0)
        except (FileNotFoundError, json.JSONDecodeError):
            # Return a default value if the file is not found or invalid
            return 0

# Create a single instance of the config to be used throughout the app
config = Config()
