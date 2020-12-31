import re

# no escaping
print(re.search(r'.com', 'welcome'))
# escaping the .
print(re.search(r'\.com', 'welcome'))
# escaping the .
print(re.search(r'\.com', 'mydomain.com'))
