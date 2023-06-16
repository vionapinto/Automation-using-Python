# Creating and saving a text file:
content = """First text Second text"""

with open('file1.txt', 'w') as file:
  file.write(content)






# Read content from text file:
with open('file1.txt', 'r') as file:
  content = file.read()

print(content)





# Remove last character from text file:

with open('file3.csv', 'r') as file:
  content = file.read()


modified_content = content[:-1]

with open('file3.csv', 'w') as file:
  file.write(modified_content)  # last character 0 got removed






#Removing last character from multiple files:

from pathlib import Path

files_dir = Path('files')

for filepath in files_dir.iterdir():
  with open(filepath, 'r') as file:
    content = file.read()
    new_content = content[:-1]
  
  with open(filepath, 'w') as file:
    file.write(new_content)





# Replace word from multiple files

from pathlib import Path

files_dir = Path('files')

for filepath in files_dir.iterdir():
  with open(filepath, 'r') as file:
    content = file.read()
    new_content = content.replace('amount', 'units')

  with open(filepath, 'w') as file:
    file.write(new_content)




# Merge txt and csv files:

from pathlib import Path

files_dir = Path('files')

merged = ''
for filepath in files_dir.iterdir():
  with open(filepath, 'r') as file:
    content = file.read()
  merged = merged + content + '\n'


with open('merged.csv', 'w') as file:
  file.write(merged)




# Merge text files without Header

from pathlib import Path

files_dir = Path('files')

merged = ''
for index, filepath in enumerate(files_dir.iterdir()):
  with open(filepath, 'r') as file:
    content = file.readlines()
    new_content = content[1:]
  if index == 0:
    content = ''.join(content)  
    merged = merged + content + '\n'
  else:
    new_content = ''.join(new_content)
    merged = merged + new_content + '\n'


with open('merged.csv', 'w') as file:
  file.write(merged)





# Replace line in text file:

with open('merged.csv', 'r') as file:
  content = file.readlines()

content[0] = 'ID,AMOUNT,COST\n'

with open('merged.csv', 'w') as file:
  file.writelines(content)