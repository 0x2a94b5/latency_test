"""
Config
"""

import os
from configparser import ConfigParser

cur_dir = os.path.dirname(os.path.abspath(__file__))
file = os.path.join(cur_dir, 'config.ini')

config = ConfigParser()
config.read(file)
