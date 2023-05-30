"""files are:
abc.txt
def.txt
ghi.txt
"""

from pathlib import Path

root_dir = Path('Pathlib_Library')
file_paths = root_dir.iterdir()
print(Path.cwd()) #--> where rename_files.py file is located

for path in file_paths:
  new_filename = "new-" + path.stem + path.suffix # just constructing string here, you haven't renamed yet!
  new_filepath = path.with_name(new_filename) 
  print(new_filepath)
  path.rename(new_filepath) # make sure you also rename the path, or else you will end up creating files outside the Pathlib_Library folder

"""Now files are renamed to:
new-abc.txt
new-def.txt
new-ghi.txt
"""