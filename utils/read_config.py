import json,os

def load_test_data(site="rahulshetty"):
    config_path = os.path.join("config", f"{site}.json")
    with open(config_path) as f:
        data = json.load(f)

        if isinstance(data, dict):
            return [data]
        return data
