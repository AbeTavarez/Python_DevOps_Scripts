#!/usr/bin/env python3

import subprocess

# * Running basic methods
subprocess.run(['date'])

subprocess.run(['sleep', '2'])

# * run ping command
# subprocess.run(['ping', 'www.google.com'])

# * Return Error Message
result = subprocess.run(['ls', 'no_such_file_or_dir'])
print('error msg --->', result.returncode)

# * Capturing output

output_result = subprocess.run(['host', '8.8.8.8'], capture_output=True)
print(output_result)
print(output_result.returncode)
print(output_result.stdout.decode().split())

# * Capturing -> STDOUT and STDERR

result_2 = subprocess.run(['rm', 'no_such_file'], capture_output=True)

print(result_2.returncode)
print(result_2.stdout)
print(result_2.stderr)
