import yaml
from pathlib import Path

# This finds the absolute path to the directory where main.py sits
ROOT_DIR = Path(__file__).parent.parent 

def projectConfig():
    # Change "projectConfig.yaml" to "config/config.yaml" if you move it later!
    config_path = ROOT_DIR / "projectConfig.yaml" 
    
    with open(config_path, "r") as f:
        return yaml.safe_load(f)
    
projectConfig = projectConfig()



