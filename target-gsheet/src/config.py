import argparse
import sys
import json
from datetime import datetime
from datetime import timedelta


def access_config():
    """retrieve the config & state items from config.json & state.json"""

    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--config', help='Config file')
    args = parser.parse_args()

    if args.config:
        with open(args.config) as config_input:
            config = json.load(config_input)
    else:
        print("Missing config")
        sys.exit(1)

    return config


def get_config_item(item):
    config_items = access_config()
    return config_items[item]