import yaml


def load_config():
    with open("app_config.yml", "r") as file:
        config = yaml.safe_load(file)
    return config
