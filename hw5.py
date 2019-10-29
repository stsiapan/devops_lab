#!/usr/bin/env python

from platform import python_version
from pip._internal.operations.freeze import freeze
from distutils.sysconfig import get_python_lib
import os
import json
import yaml
import sys
import pip

list_of_modules = []
for _ in freeze():
    list_of_modules.append(_)
my_dict = {'version': python_version(),
           'python executable location ': sys.executable,
           'pip location': pip.__path__,
           'PYTHONPATH': os.environ['PYTHONPATH'],
           'installed packages': list_of_modules,
           'site-packages location': get_python_lib(),
           }
with open('out.json', 'w') as file:
    json.dump(my_dict, file, indent=4)
with open('out.yaml', 'w') as file:
    yaml.dump(my_dict, file, indent=4)
