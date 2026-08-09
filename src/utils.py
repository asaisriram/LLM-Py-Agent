import yaml
from pathlib import Path

# absolute path to the directory where main.py sits
ROOT_DIR = Path(__file__).parent.parent 

def projectConfig():
    config_path = ROOT_DIR / "projectConfig.yaml" 
    
    with open(config_path, "r") as f:
        return yaml.safe_load(f)
    
projectConfig = projectConfig()



