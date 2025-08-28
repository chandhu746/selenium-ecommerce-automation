import json
import os

def load_test_data():

    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    config_path = os.path.join(project_root, "config", "config.json")

    with open(config_path, "r") as f:
        data = json.load(f)

    return data["data"]
