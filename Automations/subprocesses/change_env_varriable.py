#!/usr/bin/env python3

import os
import subprocess

# * Copy enviroment variables
my_env = os.environ.copy()
# print(my_env)
print(type(my_env))  # dict

# * Add new path to the PATH variable
my_env['PATH'] = os.pathsep.join(['/opt/myapp', my_env['PATH']])

result = subprocess.run(['myapp'], env=my_env)
