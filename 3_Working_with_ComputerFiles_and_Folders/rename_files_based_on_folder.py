"""Now files are:
new-abc.txt
new-def.txt
new-ghi.txt
"""

from pathlib import Path

root_dir = Path('Pathlib_Library')
#file_paths = root_dir.iterdir()
file_paths = root_dir.glob("**/*") # use this instead.

for path in file_paths:
  if path.is_file():
    parent_folder = path.parts[-2]
    new_filename = parent_folder + '-' + path.name
    print(new_filename)
    new_filepath = path.with_name(new_filename)
    path.rename(new_filepath)

""" Files renamed to :
Pathlib_Library-new-abc.txt
Pathlib_Library-new-def.txt
Pathlib_Library-new-ghi.txt
"""