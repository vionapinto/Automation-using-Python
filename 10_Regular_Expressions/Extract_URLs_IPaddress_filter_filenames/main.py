# # Extracting URLs:

with open('urls.txt', 'r') as file:
    content = file.read()

print(content)

# # http://google.com
# # https://example.com
# # http://www.wikipedia.com
# # http://pythonhow.com
# # https://python.org


import re

pattern = re.compile("https?://(?:www.)?[^ \n]+\.com")
matches = pattern.findall(content)
print(matches)

# # ['http://google.com',
# #  'https://example.com',
# #  'http://www.wikipedia.com',
# #  'http://pythonhow.com']


# # Extracting IP address:

with open('ips.txt', 'r') as file:
    content = file.read()
print(content)

# # 912.131.120.111
# # 912.131.134.000
# # 912.131.129.129


import re

pattern = re.compile("[0-9]{3}\.[0-9]{3}\.12[0-9]{1}\.[0-9]{3}")
matches = pattern.findall(content)
print(matches)



# ## Filter Filenames

from pathlib import Path 

root_dir = Path('files')
filenames = root_dir.iterdir()
filenames_str = [filename.name for filename in filenames]
print(filenames_str)

# # ['Nov-12.txt',
# #  'billy_Nov-13.txt',
# #  'november-14.txt',
# #  'nov-20.txt',
# #  'Nov-22.txt',
# #  'November-24.txt',
# #  'Oct-17.txt']

import re

pattern = re.compile("nov[a-z]*-(?:[1-9]|1[0-9]|20).txt", re.IGNORECASE)
matches = [filename for filename in filenames_str if pattern.findall(filename)]
print(matches)

# # ['Nov-12.txt', 'billy_Nov-13.txt', 'november-14.txt', 'nov-20.txt']
